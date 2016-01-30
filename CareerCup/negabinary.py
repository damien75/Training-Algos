#source CareerCup / Facebook

#input: integer a

#goal: return a in base -2 (negabinary)

#idea: build the string progressively from the rest that we have and the current position in the negabinary
#case 0: if rest == 0: break and return result
#case 1: if rest % 2 == 0:
    #case 1.a: if currPos % 2 == 0: add 1 to the left of result and rest = (rest - 2)/2
    #case 1.b: add 1 to the left of result and rest = (rest + 2^currPos)/2
#case 2: add 0 to the left of result


def negabinary(a):
    rest = a
    a = str(a)
    currPos = 0
    result = ""
    while rest != 0:
        if rest % 2 != 0:
            result = "1" + result
            if currPos % 2 == 0:
                rest -= 1
            else:
                rest += 1
            rest /= 2
        else:
            result = "0" + result
            rest /= 2
        currPos += 1
    return result or 0

print negabinary(-15)
print negabinary(2)
print negabinary(13)
