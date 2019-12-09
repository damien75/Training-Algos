from unittest import TestCase

from interviews.mud_wall import MudWall


class MudWallTest(TestCase):
    def setUp(self) -> None:
        self.instance = MudWall()

    def test_mud_wall_max_height_for_wall_1(self):
        """
        Wall 1

                    7
                    7
                  M 7
                M M 7
              4 M M 7
            M 4 M M 7
          2 M 4 M M 7
        1 2 M 4 M M 7
        1 2 M 4 M M 7
        1 2 M 4 M M 7
        1 2 M 4 M M 7
        """
        stone_segment_positions = [1, 2, 4, 7]
        stone_segment_height = [4, 5, 7, 11]
        self.assertEqual(self.instance.max_height(stone_segment_positions, stone_segment_height), 9)

    def test_mud_wall_max_height_for_wall_2(self):
        """
        Wall 2

                M
        1 M   M M M
        1 M 3 M M M 7
        1 M 3 M M M 7
        1 M 3 M M M 7
        """
        stone_segment_positions = [1, 3, 7]
        stone_segment_height = [4, 3, 3]
        self.assertEqual(self.instance.max_height(stone_segment_positions, stone_segment_height), 5)

    def test_mud_wall_max_height_for_wall_3(self):
        """
        Wall 3

                  M
                M M M
              M M M M M
            M M M M M M M
          2 M M M M M M M M
        1 2 M M M M M M M M 11
        """
        stone_segment_positions = [1, 2, 11]
        stone_segment_height = [1, 2, 1]
        self.assertEqual(self.instance.max_height(stone_segment_positions, stone_segment_height), 6)

    def test_mud_wall_max_height_for_wall_4(self):
        """
        Wall 4

                    M
                  M M M
                M M M M M
              M M M M M M M
        1   M M M M M M M M 11
        1 2 M M M M M M M M 11
        """
        stone_segment_positions = [1, 2, 11]
        stone_segment_height = [2, 1, 2]
        self.assertEqual(self.instance.max_height(stone_segment_positions, stone_segment_height), 6)

    def test_mud_wall_max_height_for_wall_5(self):
        """
        Wall 5

                      M
                    M M M
                  M M M M M
                M M M M M M 11
              M M M M M M M 11
        1   M M M M M M M M 11
        1 2 M M M M M M M M 11
        """
        stone_segment_positions = [1, 2, 11]
        stone_segment_height = [2, 1, 4]
        self.assertEqual(self.instance.max_height(stone_segment_positions, stone_segment_height), 7)

    def test_mud_wall_max_height_for_wall_6(self):
        """
        Wall 6

                            11
                            11
                          M 11
                        M M 11
                      M M M 11
                    M M M M 11
                  M M M M M 11
                M M M M M M 11
              M M M M M M M 11
        1   M M M M M M M M 11
        1 2 M M M M M M M M 11
        """
        stone_segment_positions = [1, 2, 11]
        stone_segment_height = [2, 1, 11]
        self.assertEqual(self.instance.max_height(stone_segment_positions, stone_segment_height), 9)
