#Source Hackerrank / Algorithms / Search / Missing Numbers

#input: arrays A and B containing number in a 100 range

#goal: return the numbers that are not present the same number of times in both arrays

#idea: go through array A, store every number in a hashtable to count them, then dicrease while going through B
#complexity linear in the length of the array


def showMissingNumbers(A , B):
    count = {}
    for u in A:
        if u in count:
            count[u] += 1
        else:
            count[u] = 1

    for v in B:
        if v in count:
            count[v] -= 1
        else:
            count[v] = -1

    missingNb = []
    for u in count:
        if count[u] != 0:
            missingNb.append(u)

    for u in missingNb:
        print u,
    print

#Read the input from Hackerrank
"""n = input()
A = map(int , raw_input().split())
m = input()
B = map(int , raw_input().split())
showMissingNumbers(A , B)"""

#Custom Inputs
showMissingNumbers([203 , 204 , 205 , 206 , 207 , 208 , 203 , 204 , 205 , 206] ,
[203 , 204 , 204 , 205 , 206 , 207 , 205 , 208 , 203 , 206 , 205 , 206 , 204])
