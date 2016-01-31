#input : string word

#goal: Return the list of all possible abbreviations of the word

#idea: Use a recursive call to a function to get the abbreviation of a word,
#given the current position we're at in the string, our current abbreviation and the count
#for the last character in our current abbreviation

#complexity: O(2^n) because we see each possible case once in time and 0(2^n) in space

class Abbreviations:
    def __init__(self , word):
        self.word = word
        self.res = []

    def getAllAbbreviations(self , pos , curr , count):
        if pos == len(self.word):
            if count > 0:
                curr += str(count)
            self.res.append(curr)
        else:
            #in this case we want to abbreviate char at position pos
            self.getAllAbbreviations(pos + 1 , curr , count + 1)

            #in this case we don't
            if count > 0:
                curr += str(count)
            curr += word[pos]
            self.getAllAbbreviations(pos + 1 , curr , 0)
        return self.res

#Example:
word = "word"
result = ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
abbr = Abbreviations(word)
print abbr.getAllAbbreviations(0 , '' , 0)
