import ast
import bisect
import sys

from datetime import datetime
from signal import signal, SIGINT

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser(object):
    def __init__(self, driver_path: str, url: str, contract_address: str):
        self.__driver_path = driver_path
        self.__common_url = url
        self.__contract_address = contract_address
        self.__top_price = [[] * 44]
        self.__options = Options()
        self.__options.headless = True
        self.__driver = webdriver.Chrome(options=self.__options, executable_path=DRIVER_PATH)
        self.__stored_exception = None

    def __enter__(self):
        signal(SIGINT, self._sigint_handler)
        self.track_tx()

    def __exit__(self, type, value, traceback):
        print('Exiting session...')

        self._do_cleanup()

    def _do_cleanup(self):
        print(self.top_price)

    def _sigint_handler(self, signal_received, frame):
        print('Ctrl + C handler called')

        self.__exit__(None, None, None)
        sys.exit(0)

    @property
    def stored_exception(self):
        return self.__stored_exception

    @property
    def top_price(self) -> str:
        result = ""
        for p_list in self.__top_price:
            result += f"{p_list}\n"
        return result

    def track_tx(self):
        """
        Track tx happening with given contract and keeps list of biggest tx amount by hour
        """
        start_tsp = int(datetime.utcnow().replace(minute=0, hour=0, second=0, microsecond=0).timestamp())
        tx_found = []
        last_tx_seen = ""
        while True:
            try:
                self.__driver.get(f"{self.__common_url}/address/{self.__contract_address}")
                try:
                    val = self.__driver.find_elements_by_xpath(
                        "//*[@id=\"root\"]/section/section/article[4]/section/div[1]/table/tbody/tr"
                        "/td/span/div/a")
                    for el in val:
                        tx = el.get_attribute('href').split("/")[-1]
                        if tx == last_tx_seen:
                            print("nothing new")
                            break
                        else:
                            tx_found.append(tx)
                except Exception as e:
                    print(f"Caught exception: {e} - retrying")
                print(f"Found {len(tx_found)} new txs")
                no_price = 0
                tx_found = ["7D8E453D978488ABB586CEA476198E9E577ED4B6B338988C33A9FFC449908754"] + tx_found
                for tx in tx_found:
                    tx_url = f"{self.__common_url}/tx/{tx}"
                    self.__driver.get(tx_url)
                    try:
                        amount_str = self.__driver.find_element_by_xpath(
                            "//*[@id=\"root\"]/section/section/div/div[10]/div[2]/div[1]/"
                            "section[1]/p").text
                        amount_dict = ast.literal_eval(amount_str)
                    except Exception as e:
                        no_price += 1
                        print(f"Caught exception: {e} for url {tx_url}")
                    else:
                        print(f"""Found spent {amount_dict["amount"]} {amount_dict["denom"]}""")
                        bisect.insort(self.__top_price[int(datetime.utcnow().replace(
                            minute=0, hour=0, second=0, microsecond=0).timestamp()) - start_tsp],
                                      float(amount_dict["amount"]) / 1000000)
                print(f"top 10: {self.__top_price} - no price {no_price}")
            except KeyboardInterrupt:
                self.__stored_exception = sys.exc_info()


if __name__ == "__main__":
    DRIVER_PATH = '/Users/damien/Downloads/chromedriver'
    b = Browser(DRIVER_PATH, "https://finder.terra.money/columbus-5", "terra1eek0ymmhyzja60830xhzm7k7jkrk99a60q2z2t")
    with b:
        print("Browser session started")
