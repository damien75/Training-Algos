class Abbreviations:
    """
    Input : string word

    Goal: Return the list of all possible abbreviations of the word

    Idea: Use a recursive call to a function to get the abbreviation of a word,
    given the current position we're at in the string, our current abbreviation and the count
    for the last character in our current abbreviation

    complexity: O(2^n) because we see each possible case once in time and 0(2^n) in space
    """
    def __init__(self, word: str):
        self.word = word
        self.res = []

    def get_all_abbreviations(self, pos: int, curr: str, count: int):
        if pos == len(self.word):
            if count > 0:
                curr += str(count)
            self.res.append(curr)
        else:
            # in this case we want to abbreviate char at position pos
            self.get_all_abbreviations(pos + 1, curr, count + 1)

            # in this case we don't
            if count > 0:
                curr += str(count)
            curr += self.word[pos]
            self.get_all_abbreviations(pos + 1, curr, 0)
        return self.res
