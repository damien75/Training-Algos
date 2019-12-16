from unittest import TestCase

from interviews.flight_schedule import FlightSchedule


class FlightScheduleTest(TestCase):
    def setUp(self) -> None:
        self.instance = FlightSchedule()

    def test_order_schedule(self):
        self.assertListEqual([('CDG', 'EWR'), ('EWR', 'ORD'), ('ORD', 'SFO'), ('SFO', 'YUL')],
                             self.instance.order_itinerary(
                                 [('ORD', 'SFO'), ('CDG', 'EWR'), ('SFO', 'YUL'), ('EWR', 'ORD')]))

    def test_empty_list(self):
        self.assertListEqual([], self.instance.order_itinerary([]))

    def test_loop_itinerary(self):
        with self.assertRaises(KeyError):
            self.instance.order_itinerary(
                [('ORD', 'LAX'), ('MEX', 'ORD'), ('ORD', 'SFO'), ('CDG', 'EWR'), ('LAX', 'MEX'), ('SFO', 'YUL'),
                 ('EWR', 'ORD')])
