from typing import Callable, Optional, List, Tuple


class CelebrityGraph(object):
    """
    There are N people labeled 1 to N. A given person i may or may not know
    person j, and vice-versa.

    The celebrity C is defined as:
    * Everyone knows her: knows(i, C) == True for all i
    * She knows no one else: knows(C, i) == False for all i != C
    """
    def __init__(self, n: int, knows: Callable[[int, int], bool]):
        """
        :param n: the number of people
        :param knows: a function from (i, j) -> boolean indicating if person i knows person j
        """
        self.n = n
        self.knows = knows

    def find_celeb(self) -> Optional[int]:
        """
        :return: The celebrity if there is one or None
        Idea:
            map1: key <-- person known
            values: list[people who know that person]

            map2: key <-- person in question
            values: list[people they know]

            for start in range(len(p)):
                for end in range(len(p)):
                    if start != end:
                        edges.append((start, end))

            for e in edges:
                map1[e._start] = either [e._end] else .append(_e.end)

            for k, v in map1.items():
                if len(v) == N and len(map2[k]) == 0:
                    CELEBRITY

            return None
        """
        edges: List[Tuple[int, int]] = []
        for start in range(1, self.n + 1):
            for end in range(1, self.n + 1):
                if start != end and self.knows(start, end):
                    edges.append((start, end))

        who_people_know_map = {}  # key: person, values: people known by key
        known_people_map = {}  # key: person known, values: people who know this key

        for e in edges:
            if e[0] in who_people_know_map:
                who_people_know_map[e[0]].append(e[1])
            else:
                who_people_know_map[e[0]] = [e[1]]

            if e[1] in known_people_map:
                known_people_map[e[1]].append(e[0])
            else:
                known_people_map[e[1]] = [e[0]]

        for key, values in known_people_map.items():
            if len(values) == self.n - 1 and len(who_people_know_map.get(key, [])) == 0:
                return key

        return None
