#source: Careercup / Google / http://www.careercup.com/question?id=5719829237465088

#input: array of size N with values
#if we burst balloon at position i, we add to the output values[i - 1]*values[i]*values[i + 1]
#And the value at position i is removed, values at positions i - 1 and i + 1 are now adjacent
#values all the way to the left and all the way to the right are 1, so that when the last balloon bursts
#the output will see its value increased by the value of the last balloon.

#goal: burst balloons 1 by 1 to maximize the output

#idea: look at all the local minimums, and burst the smallest one first, until we burst all the balloons

import heapq

def findBestMaximum(values):
    assert(len(values) > 3)
    if len(values) == 4:
        if values[1] > values[2]:
            return values[2] , 2
        else:
            return values[1] , 1
    maximum = []
    for i in range(1 , len(values) - 1):
        heapq.heappush(maximum , (-values[i - 1] * values[i] * values[i + 1] , i))
    return values[maximum[0][1]] , maximum[0][1]

def findBestMinimum(values):
    assert(len(values) >= 3)
    if len(values) == 3:
        return values[1] , 1
    else:
        minima = []
        for i in range(2 , len(values) - 2):
            if values[i - 1] > values[i] and values[i + 1] > values[i]:
                heapq.heappush(minima , (values[i] , i))
        if len(minima) == 0:
            return findBestMaximum(values)
        else:
            return minima[0]

def maximizeValueCollected(values):
    values = [1] + values
    values.append(1) #add 1 on both extremities
    output = 0
    while len(values) > 2:
        bestMinima , i = findBestMinimum(values)
        output += values[i - 1]*bestMinima*values[i + 1]
        values.pop(i)
    return output

#example 1
values = [8, 5, 6, 9, 3, 0, 2, 4, 1, 7]

print maximizeValueCollected(values) == 1652

"""burst 0, get 3*0*2 coins -> 8, 5, 6, 9, 3, 2, 4, 1, 7
burst 1, get 4*1*7 coins -> 8, 5, 6, 9, 3, 2, 4, 7
burst 2, get 3*2*4 coins -> 8, 5, 6, 9, 3, 4, 7
burst 3, get 9*3*4 coins -> 8, 5, 6, 9, 4, 7
burst 4, get 9*4*7 coins -> 8, 5, 6, 9, 7
burst 5, get 8*5*6 coins -> 8, 6, 9, 7
burst 6, get 8*6*9 coins -> 8, 9, 7
burst 9, get 8*9*7 coins -> 8, 7
burst 7, get 8*7*1 coins -> 8
burst 8, get 1*8*1 coins"""

#That's an optimal strategy and you can get (summing up) 1652 coins with it.

#At each step you choose the least local minimum among all local minimums.
#That helps make the balloons with higher value adjanced, and so gain bigger product later.

#example 2

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print maximizeValueCollected(values) == 1530

#There's no local minimum, so you should choose a triple with maximum product and burst the middle balloon:

"""burst 8, get 7*8*9 coins -> 1, 2, 3, 4, 5, 6, 7, 9
burst 7, get 6*7*9 coins -> 1, 2, 3, 4, 5, 6, 9
burst 6, get 5*6*9 coins -> 1, 2, 3, 4, 5, 9
burst 5, get 4*5*9 coins -> 1, 2, 3, 4, 9
burst 4, get 3*4*9 coins -> 1, 2, 3, 9
burst 3, get 2*3*9 coins -> 1, 2, 9
burst 2, get 1*2*9 coins -> 1, 9
burst 1, get 1*1*9 coins -> 9
burst 9, get 1*9*1 coins"""

#That will bring you 1530 coins total.
