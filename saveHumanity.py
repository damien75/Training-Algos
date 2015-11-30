#Source Hackerrank / Algorithms / Strings

#input: 2 strings

#goal: Check if a substring of the 1st string can have at most 1 difference with 2nd string

#idea: do a binary search to look for the potential 1 difference between the strings

#complexity: O(n log(n))

def BSAreSimilar(s , t):
    assert(len(s) == len(t))
    if s == t:
        return True
    else:
        l = 0
        r = len(s)
        while l <= r:
            m = (l + r)/2
            leftSimilar = s[l:m] == t[l:m]
            rightSimilar = s[m + 1:r] == t[m + 1:r]
            middleSimilar = s[m] == t[m]
            if leftSimilar and rightSimilar:
                return True
            elif leftSimilar and middleSimilar:
                l = m + 1
            elif rightSimilar and middleSimilar:
                r = m
            else:
                return False

def findSimilarities(p , v):
    match = False
    indices = []
    for j in range(len(p) - len(v) + 1):
        if BSAreSimilar(p[j : j + len(v)] , v):
            match = True
            indices.append(j)
    if match:
        for i in indices:
            print i,
        print
    else:
        print "No Match!"

#Read the input from Hackerrank
"""t = input()
for i in range(t):
    p , v = raw_input().split()
    match = False
    indices = []
    for j in range(len(p) - len(v) + 1):
        if BSAreSimilar(p[j : j + len(v)] , v):
            match = True
            indices.append(j)
    if match:
        for i in indices:
            print i,
        print
    else:
        print "No Match!"""

#Custom Inputs
findSimilarities("abbab" , "ba")
findSimilarities("hello" , "world")
findSimilarities("banana" , "nan")
