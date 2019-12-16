from logging import getLogger
from typing import List, Tuple


class FlightSchedule(object):
    """
    You are given an unordered list of flights with layovers, and you need to return the list of flights in order
    """
    def __init__(self):
        self.logger = getLogger(f'{__name__}.{__class__.__qualname__}')

    def order_itinerary(self, flights: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        if len(flights) == 0:
            return []
        departure_cities = set(map(lambda x: x[0], flights))
        departure_city_map = dict(map(lambda x: (x[0], x), flights))
        arrival_cities = set(map(lambda x: x[1], flights))
        departure_arrival_difference = departure_cities.difference(arrival_cities)
        if len(departure_arrival_difference) != 1:
            msg = f'The difference of the sets between departure and arrival city is not equal to 1,' \
                  f'therefore there is a missing flight in the input - diff: {departure_arrival_difference}'
            self.logger.warning(msg)
            raise ValueError(msg)
        departure_city = departure_arrival_difference.pop()
        ordered_journey = []

        while len(ordered_journey) < len(flights):
            journey = departure_city_map[departure_city]
            ordered_journey.append(journey)
            departure_city = journey[1]

        return ordered_journey
