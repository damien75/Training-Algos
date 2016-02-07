#input : 2 strings: word and pattern

#goal: Find out if word follows the pattern

#idea: Use a hashtable to store the associated letters to a letter in the pattern
#and a set to store all the associated letters we have already seen

#complexity: O(n^2) in time in the worst case and O(n) in space

class PatternRecognition:
    def __init__(self , pattern , word):
        self.pattern = pattern
        self.word = word
        self.s = set() #this will keep track of the combination of letters seen
        self.h = {} #this will keep track of the combination of letters associated with each letter in the pattern

    def wordFollowsPattern(self , wordIndex = 0 , patternIndex = 0):
        if wordIndex == len(self.word) and patternIndex == len(self.pattern):
            return True #we get to the end of word and pattern at the same time ==> MATCH
        elif wordIndex == len(self.word) or patternIndex == len(self.pattern):
            return False #mismatch in length ==> FAIL
        else:
            key = self.pattern[patternIndex]
            for i in range(wordIndex + 1 , len(self.word)): #for each possible length of substring
                cur = self.word[wordIndex : i]
                if cur not in self.s and key not in self.h: #if we have not alredy seen this association, try it
                    self.h[key] = cur
                    self.s.add(cur)
                    if self.wordFollowsPattern(i + 1 , patternIndex + 1): #if this works down the line, return True
                        return True
                    self.s.remove(cur) #else remove this unsuccessful try
                    self.h.pop(key)
                elif cur in self.s and self.h[key] == cur: #if we have already seen this, keep checking the rest
                    if self.wordFollowsPattern(i + 1 , patternIndex + 1):
                        return True
            return False

#Examples:
pattern = "abab"
str = "redblueredblue"
rec = PatternRecognition(pattern , str)
print rec.wordFollowsPattern() , "should be" , True
pattern = "aaaa"
str = "asdasdasdasd"
rec = PatternRecognition(pattern , str)
print rec.wordFollowsPattern() , "should be" , True
pattern = "aabb"
str = "xyzabcxzyabc"
rec = PatternRecognition(pattern , str)
print rec.wordFollowsPattern() , "should be" , False
