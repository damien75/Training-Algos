class PatternRecognition:
    """
    Input : 2 strings: word and pattern

    Goal: Find out if word follows the pattern

    Idea: Use a hashtable to store the associated letters to a letter in the pattern
    and a set to store all the associated letters we have already seen

    complexity: O(n^2) in time in the worst case and O(n) in space
    """

    def __init__(self, pattern: str, word: str):
        self.pattern = pattern
        self.word = word
        self.s = set()  # this will keep track of the combination of letters seen
        self.h = {}  # this will keep track of the combination of letters associated with each letter in the pattern

    def word_follows_pattern(self, word_index: int = 0, pattern_index: int = 0) -> bool:
        if word_index == len(self.word) and pattern_index == len(self.pattern):
            return True  # we get to the end of word and pattern at the same time ==> MATCH
        elif word_index == len(self.word) or pattern_index == len(self.pattern):
            return False  # mismatch in length ==> FAIL
        else:
            key = self.pattern[pattern_index]
            for i in range(word_index + 1, len(self.word)):  # for each possible length of substring
                cur = self.word[word_index: i]
                if cur not in self.s and key not in self.h:  # if we have not alredy seen this association, try it
                    self.h[key] = cur
                    self.s.add(cur)
                    if self.word_follows_pattern(i + 1, pattern_index + 1):  # if this works down the line, return True
                        return True
                    self.s.remove(cur)  # else remove this unsuccessful try
                    self.h.pop(key)
                elif cur in self.s and self.h[key] == cur:  # if we have already seen this, keep checking the rest
                    if self.word_follows_pattern(i + 1, pattern_index + 1):
                        return True
            return False
