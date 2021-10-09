import ast
import bisect
import logging
import sys

from datetime import datetime
from copy import deepcopy
from signal import signal, SIGINT
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser(object):
    def __init__(self, driver_path: str, url: str, contract_address: str):
        self.__driver_path = driver_path
        self.__common_url = url
        self.__contract_address = contract_address
        self.__top_price = [[] * 50]
        self.__options = Options()
        self.__options.headless = True
        self.__driver = webdriver.Chrome(options=self.__options, executable_path=DRIVER_PATH)
        self.__tx_seen = set()

    def __enter__(self):
        signal(SIGINT, self._sigint_handler)
        self.track_tx()

    def __exit__(self, type, value, traceback):
        logging.info('Exiting session...')

        self._do_cleanup()

    def _do_cleanup(self):
        self.__driver.quit()
        logging.info(self.top_price)

    def _sigint_handler(self, signal_received, frame):
        logging.info(f"{signal_received} handled")

        self.__exit__(None, None, None)
        sys.exit(0)

    @property
    def top_price(self) -> str:
        result = ""
        for i, p_list in enumerate(self.__top_price):
            result += f"{i}: {p_list}\n"
        return result

    def track_tx(self):
        """
        Track tx happening with given contract and keeps list of biggest tx amount by hour
        """
        start_tsp = int(datetime.utcnow().replace(minute=0, hour=0, second=0, microsecond=0).timestamp())
        while True:
            tx_found = []
            new_tx_seen = set()
            try:
                self.__driver.get(f"{self.__common_url}/address/{self.__contract_address}")
                val = self.__driver.find_elements_by_xpath(
                    "//*[@id=\"root\"]/section/section/article[4]/section/div[1]/table/tbody/tr"
                    "/td/span/div/a")
                for el in val:
                    tx = el.get_attribute('href').split("/")[-1]
                    if tx in self.__tx_seen:
                        break
                    else:
                        new_tx_seen.add(tx)
                        tx_found.append(tx)
            except Exception as e:
                logging.warning(f"Caught exception: {e} - retrying")
            if len(new_tx_seen) > 0:
                logging.info(f"Found {len(new_tx_seen)} new transactions")
                self.__tx_seen = deepcopy(new_tx_seen)
                new_tx_seen.clear()
            no_price = 0
            # tx_found = ["7D8E453D978488ABB586CEA476198E9E577ED4B6B338988C33A9FFC449908754"] + tx_found
            for tx in tx_found:
                tx_url = f"{self.__common_url}/tx/{tx}"
                try:
                    self.__driver.get(tx_url)
                    amount_str = self.__driver.find_element_by_xpath(
                        "//*[@id=\"root\"]/section/section/div/div[10]/div[2]/div[1]/"
                        "section[1]/p").text
                    amount_dict = ast.literal_eval(amount_str)
                    amount = float(amount_dict["amount"]) / 1000000
                except Exception as e:
                    no_price += 1
                    logging.debug(f"skipping {tx_url} - {e}")
                else:
                    logging.info(f"""Found spent {amount} {amount_dict["denom"]}""")
                    slot_idx = int(datetime.utcnow().replace(
                        minute=0, hour=0, second=0, microsecond=0).timestamp()) - start_tsp
                    cur_top = self.__top_price[slot_idx]
                    if len(cur_top) <= 10 or amount > cur_top[-1]:
                        bisect.insort(cur_top, amount)
                        if len(cur_top) > 10:
                            cur_top = cur_top[1:]
                        self.__top_price[slot_idx] = cur_top
            logging.info(f"top 10: {self.__top_price} - no price {no_price} - sleeping 10sec")
            sleep(10)


if __name__ == "__main__":
    DRIVER_PATH = '/Users/damien/Downloads/chromedriver'
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    fileHandler = logging.FileHandler("terra.log", encoding="utf-8")
    fileHandler.setLevel(logging.DEBUG)
    rootLogger.addHandler(handler)
    rootLogger.addHandler(fileHandler)
    b = Browser(DRIVER_PATH, "https://finder.terra.money/columbus-5", "terra1eek0ymmhyzja60830xhzm7k7jkrk99a60q2z2t")
    with b:
        logging.info("Browser session started")
