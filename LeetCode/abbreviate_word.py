from logging import getLogger
from typing import List


class Abbreviations:
    """
    Input : dictionary of n strings and query with string word

    Goal: Find out if the abbreviation of the query word is unique in the dictionary
    abbreviation is done as follows:
    word --becomes--> <first letter><nb of letters in the middle><last letter>
    for example,
    a) it                      --> it    (no abbreviation)
         1
    b) d|o|g                   --> d1g
                  1    1  1
         1---5----0----5--8
    c) i|nternationalizatio|n  --> i18n
                  1
         1---5----0
    d) l|ocalizatio|n          --> l10n

    Idea: Keep a hashtable of the abbreviated words and a list of the corresponding originals
    For each query, the result will be given in constant time

    complexity: O(n) in time to build the hashtable and O(n) in space
    """
    def __init__(self, words: List[str]):
        self.logger = getLogger(f'{__name__}.{__class__.__qualname__}')
        self.words = words
        self.h = self.build_hash_table()

    @staticmethod
    def abbreviated(word: str):
        assert (len(word) >= 2)
        if len(word) == 2:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]

    def build_hash_table(self):
        h = {}
        for word in self.words:
            abbr = self.abbreviated(word)
            if abbr in h:
                h[abbr].append(word)
            else:
                h[abbr] = [word]
        self.logger.info(f'Build hash table for abbreviated words: {h}')
        return h

    def is_unique(self, word: str) -> bool:
        return self.abbreviated(word) not in self.h
