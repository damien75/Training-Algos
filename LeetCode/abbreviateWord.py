#input : dictionary of n strings and query with string word

#goal: Find out if the abbreviation of the query word is unique in the dictionary
#abbreviation is done as follows:
#word --becomes--> <first letter><nb of letters in the middle><last letter>
#for example,
#a) it                      --> it    (no abbreviation)
#     1
#b) d|o|g                   --> d1g
#              1    1  1
#     1---5----0----5--8
#c) i|nternationalizatio|n  --> i18n
#              1
#     1---5----0
#d) l|ocalizatio|n          --> l10n

#idea: Keep a hashtable of the abbreviated words and a list of the corresponding originals
#For each query, the result will be given in constant time

#complexity: O(n) in time to build the hashtable and O(n) in space

def abbreviated(word):
    assert(len(word) >= 2)
    if len(word) == 2:
        return word
    else:
        return word[0] + str(len(word) - 2) + word[-1]

def buildHashTable(words):
    h = {}
    for word in words:
        abbr = abbreviated(word)
        if abbr in h:
            h[abbr].append(word)
        else:
            h[abbr] = [word]
    print h
    return h

class Abbreviations:
    def __init__(self, words):
        self.h = buildHashTable(words)

    def isUnique(self , word):
        return abbreviated(word) not in self.h


#Example:
words = ["deer", "door", "cake", "card" ]

abbr = Abbreviations(words)
print abbr.isUnique("dear") , "should be" , False
print abbr.isUnique("cart") , "should be" , True
print abbr.isUnique("cane") , "should be" , False
print abbr.isUnique("make") , "should be" , True
