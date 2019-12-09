from typing import Optional


class BookingAvailabilities(object):
    """
    X wants to help guests plan their stay
    by finding check-in and check-out dates that accommodate a desired length of stay.

    X determines availability based on existing bookings,
    in this case, we’re serializing them as colon-separated pairs of integers.
    The first integer is a check-in date, and the second is a check-out date.
    Each integer represents an offset since Jan 1, 2019.
    E.g. '0:1' represents a booking where the check-in date is Jan 1st 2019,
    and the check-out date is Jan 2nd 2019.

    Directions
    Implement a method, booking_start_date(string bookings, int stay_length, int current_date)
    that will return the first day that can accommodate a booking of length stay_length.

    Examples:
    Input: bookings: '0:2 3:5 7:14', stay_length: 1, current_date: 4
    Output: 5

    Input: bookings: '0:3 3:6 7:14', stay_length: 2, current_date: 4
    Output: 14

    Input: bookings: '0:2 5:6 7:14', stay_length: 1, current_date: 3
    Output: 3

    Rules:
    Input is well-formed
    Bookings will not overlap
    Bookings are sorted in order of check-in date
    Only dates later than or equal to current date should be returned
    """
    @staticmethod
    def booking_start_date(bookings: str, stay_length: int, current_date: int) -> int:
        """
        :return: 1st available date for desired stay_length
        """
        bookings_tuple = list(
            map(lambda s: tuple(map(int, s.split(':'))), bookings.split(' ')))  # [(0, 2), (3, 5), ...]
        if current_date > bookings_tuple[-1][1]:
            return current_date
        else:
            found_match: Optional[int] = None
            for i in range(0, len(bookings_tuple) - 1):
                last_day_prev_booking = bookings_tuple[i][1]
                first_day_next_booking = bookings_tuple[i + 1][0]

                possible_first_day = current_date if last_day_prev_booking < current_date else last_day_prev_booking

                if first_day_next_booking - possible_first_day >= stay_length:
                    found_match = possible_first_day
                    break
            if found_match is None:
                found_match = bookings_tuple[-1][1]
            return found_match
