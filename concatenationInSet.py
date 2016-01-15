#source CareerCup / Facebook

#input: set of strings s and string word

#goal: return if word is a concatenation of keys in set

#idea: look if word in set, if not look at word with one less letter

def checkIfWordCanBeObtainedFromKeyConcatenation(s , word):
    i = len(word)
    while i > 0:
        if word[:i] in s:
            if i < len(word):
                return checkIfWordCanBeObtainedFromKeyConcatenation(s , word[i:])
            else:
                return True
        i -= 1
    return False

s = {"world" , "hello" , "super" , "hell"}
print checkIfWordCanBeObtainedFromKeyConcatenation(s , "helloworld")
print checkIfWordCanBeObtainedFromKeyConcatenation(s , "superman")
print checkIfWordCanBeObtainedFromKeyConcatenation(s , "hellohello")
