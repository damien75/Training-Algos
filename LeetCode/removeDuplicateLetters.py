#input : string s of length n

#goal: Remove duplicate letters from s and return smallest lexicographical solution without reordering s

#idea: use a stack to add the letters, and keep track of the nb of letters we will still see after our current position
#when I get to a new letter:
#   if I have already seen it --> continue
#   else: if its lexicographical order is greater than the last one --> add it to the stack
#           else: try to see if the count of the letter on top of the stack allows us to remove element

#complexity: O(n^2) in the worst case in time and O(n) in space

def removeDuplicateLettersFrom(s):
    count = {}  #using hashtables and not arrays because we have no information regarding the letters in string
    visited = {}
    stack = []
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
            visited[c] = False
    for c in s:
        count[c] -= 1
        if visited[c]:
            continue
        else:
            while len(stack) > 0 and stack[-1] > c and count[stack[-1]] > 0:
                visited[stack[-1]] = False
                stack.pop()
            stack.append(c)
            visited[c] = True
    return "".join(stack)

print removeDuplicateLettersFrom("bcabc") , "should be:" , "abc"
print removeDuplicateLettersFrom("cbacdcbc") , "should be:" , "acdb"
