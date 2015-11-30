#Source Hackerrank / Algorithms / Sorting / Bigger is Greater

#input : string s

#goal: from this string, reorganize character to have the smallest lexicographically greater string than s
#i.e. we need to switch letters as far on the right as possible

#idea: look at possible indices where we could swap the letters
#if we can, then do it and return the string with right part sorted

def swap(tab , i1 , i2):
    temp = tab[i1]
    tab[i1] = tab[i2]
    tab[i2] = temp

def nextString(s):
    s = list(s)
    left = len(s) - 2
    while left >= 0:
        right = len(s) - 1
        while right > left:
            if s[left] < s[right]:
                swap(s , left , right)
                s[left + 1:] = sorted(s[left + 1:]) #need to sort the rest of the string to get the smallest
                return "".join(s)
            right -= 1
        left -= 1
    return "no answer"

#Read the input from Hackerrank
"""t = input()
for _ in range(t):
    s = raw_input()
    print nextString(s)"""

#Custom Inputs
print nextString("ab") == "ba"
print nextString("bb") == "no answer"
print nextString("hefg") == "hegf"
print nextString("dhck") == "dhkc"
print nextString("dkhc") == "hcdk"
