from typing import Set


class ConcatenationInSet(object):
    """
    Source CareerCup / Facebook

    Input: set of strings s and string word

    Goal: return if word is a concatenation of keys in set

    Idea: look if word in set, if not look at word with one less letter
    """
    def check_if_word_can_be_obtained_from_key_concatenation(self, s: Set[str], word: str) -> bool:
        i = len(word)
        while i > 0:
            if word[:i] in s:
                if i < len(word):
                    return self.check_if_word_can_be_obtained_from_key_concatenation(s , word[i:])
                else:
                    return True
            i -= 1
        return False
