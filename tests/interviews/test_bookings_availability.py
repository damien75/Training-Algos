from unittest import TestCase

from interviews.bookings_availabilities import BookingAvailabilities


class BricksGameTest(TestCase):
    def setUp(self) -> None:
        self.instance = BookingAvailabilities()

    def test_get_next_availability(self):
        self.assertEqual(self.instance.booking_start_date('0:2 3:5 7:14', 1, 4), 5)
        self.assertEqual(self.instance.booking_start_date('0:3 3:6 7:14', 2, 4), 14)
        self.assertEqual(self.instance.booking_start_date('0:2 5:6 7:14', 1, 3), 3)

        text = ['code', 'doce', 'asd']
        sorted_letters_text = list(map(sorted, text))
        print(sorted_letters_text)
