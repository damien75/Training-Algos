#Source Hackerrank / Algorithms / Implementation / Grid Search

#input: 2 grids: one small and one bigger

#goal: Check if small grid is in the big one

#idea: look for the first line of the small grid in the big one
#in that case get the index of the correspondance and check if the following lines match

def readGrid(): #from Hackerrank
    n , m = raw_input().split()
    n , m = int(n) , int(m)
    grid = ["" for x in range(n)]
    for i in range(n):
        grid[i] = raw_input()
    return grid

def findPatternInGrid(bigGrid , smallGrid):
    found = False
    for lineIndex in range(len(bigGrid)):
        if smallGrid[0] in bigGrid[lineIndex]:
            startIndex = bigGrid[lineIndex].index(smallGrid[0])
            currLine = lineIndex
            foundHere = True
            for line in smallGrid[1:]:
                currLine += 1
                if line not in bigGrid[currLine] or bigGrid[currLine].index(line) != startIndex:
                    foundHere = False
                    break
            if foundHere:
                return "YES"
                found = True
        if found:
            break
    if not found:
        return "NO"

#Read the input from Hackerrank
"""t = input()
for i in range(t):
    bigGrid = readGrid()
    smallGrid = readGrid()
    print findPatternInGrid(bigGrid , smallGrid)"""

#Custom Inputs
bigGrid = ["7283455864",
"6731158619",
"8988242643",
"3830589324",
"2229505813",
"5633845374",
"6473530293",
"7053106601",
"0834282956",
"4607924137"]
smallGrid = ["9505",
"3845",
"3530"]
print findPatternInGrid(bigGrid , smallGrid) == "YES"
bigGrid = ["400453592126560",
"114213133098692",
"474386082879648",
"522356951189169",
"887109450487496",
"252802633388782",
"502771484966748",
"075975207693780",
"511799789562806",
"404007454272504",
"549043809916080",
"962410809534811",
"445893523733475",
"768705303214174",
"650629270887160"]
smallGrid = ["99" , "99"]
print findPatternInGrid(bigGrid , smallGrid) == "NO"
