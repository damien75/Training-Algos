from logging import getLogger
from logging.config import fileConfig
from os.path import dirname, realpath
from typing import Iterator

fileConfig(fname=f'{realpath(dirname(dirname(__file__)))}/resources/logging.ini', disable_existing_loggers=False)


class MudWall(object):
    """
    A wall is described as a segment consisting of successive stone or mud layers.

    Here is an example, where mud is M and stone S

                  M
          M     S M S
        M M M S S M S
      S M M M S S M S
    M S M M M S S M S
    -----------------
    1 2 3 4 5 6 7 8 9

    Build mud walls by placing mud between stone walls positioned on a number line.
    The height of a mud segment cannot exceed 1 unit above an adjacent stick or mud segment.

    Given the placement of a number of stone segments and their heights, determine the maximum height segment of mud
    that can be built. If no mud segment can be built, return 0
    """
    def __init__(self):
        self.logger = getLogger(f'{__name__}.{__class__.__qualname__}')

    def max_height_between_2_walls(self, left_height: int, right_height: int, gap_size: int) -> int:
        """
        if left_height == right_height:  # we build a pyramid shape perfectly centered where the max will be
            max = (gap_size + 1) // 2 = ceil(gap_size / 2)
        else:  # we try to have the mud segments go up from low extremity to high extremity. If we can reach the same height then same strategy as before
        if too narrow --> min + gap_size
        if just narrow enough then gap = diff --> max = min + (gap + diff) / 2
        else --> max + gap_remaining / 2 = min + diff + gap_remaining / 2
        gap_remaining = gap - diff
            max = min(left_height, right_height) + (gap_size + abs(right_height - left_height)) // 2 - 1
        :param left_height:
        :param right_height:
        :param gap_size:
        :return:
        """
        self.logger.debug(f'Finding max height for gap of {gap_size} between 2 walls: {left_height} and {right_height}')
        height_diff = abs(right_height - left_height)
        min_height = min(left_height, right_height)
        if gap_size < height_diff:
            return min_height + gap_size
        else:
            return min_height + (gap_size + height_diff + 1) // 2

    def max_height(self, stone_wall_positions: Iterator[int], stone_wall_heights: Iterator[int]) -> int:
        final_max = 0
        stone_wall_heights = iter(stone_wall_heights)
        stone_wall_positions = iter(stone_wall_positions)
        try:
            left_wall_height = next(stone_wall_heights)
            left_wall_position = next(stone_wall_positions)
        except StopIteration as s_err:
            self.logger.error(f'Received empty iterators - {s_err}')
            return final_max

        for right_wall_position, right_wall_height in zip(stone_wall_positions, stone_wall_heights):
            final_max = max(final_max, self.max_height_between_2_walls(left_wall_height, right_wall_height,
                                                                       right_wall_position - left_wall_position - 1))
            left_wall_height = right_wall_height
            left_wall_position = right_wall_position
        return final_max
