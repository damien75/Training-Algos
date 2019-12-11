from unittest import TestCase

from CareerCup.burst_balloons import BurstBalloons


class BurstBalloonsTest(TestCase):
    def setUp(self) -> None:
        self.instance = BurstBalloons()

    def test_maximize_burst_output1(self):
        """
        That's an optimal strategy and you can get (summing up) 1652 coins with it.

        At each step you choose the least local minimum among all local minimums.
        That helps make the balloons with higher value advance, and so gain bigger product later.

        burst 0, get 3*0*2 coins -> 8, 5, 6, 9, 3, 2, 4, 1, 7
        burst 1, get 4*1*7 coins -> 8, 5, 6, 9, 3, 2, 4, 7
        burst 2, get 3*2*4 coins -> 8, 5, 6, 9, 3, 4, 7
        burst 3, get 9*3*4 coins -> 8, 5, 6, 9, 4, 7
        burst 4, get 9*4*7 coins -> 8, 5, 6, 9, 7
        burst 5, get 8*5*6 coins -> 8, 6, 9, 7
        burst 6, get 8*6*9 coins -> 8, 9, 7
        burst 9, get 8*9*7 coins -> 8, 7
        burst 7, get 8*7*1 coins -> 8
        burst 8, get 1*8*1 coins
        """
        values = [8, 5, 6, 9, 3, 0, 2, 4, 1, 7]

        self.assertEqual(1652, self.instance.maximize_value_collected(values))

    def test_maximize_burst_output2(self):
        """
        There's no local minimum, so you should choose a triple with maximum product and burst the middle balloon

        burst 8, get 7*8*9 coins -> 1, 2, 3, 4, 5, 6, 7, 9
        burst 7, get 6*7*9 coins -> 1, 2, 3, 4, 5, 6, 9
        burst 6, get 5*6*9 coins -> 1, 2, 3, 4, 5, 9
        burst 5, get 4*5*9 coins -> 1, 2, 3, 4, 9
        burst 4, get 3*4*9 coins -> 1, 2, 3, 9
        burst 3, get 2*3*9 coins -> 1, 2, 9
        burst 2, get 1*2*9 coins -> 1, 9
        burst 1, get 1*1*9 coins -> 9
        burst 9, get 1*9*1 coins
        """
        # example 2

        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.assertEqual(1530, self.instance.maximize_value_collected(values))
