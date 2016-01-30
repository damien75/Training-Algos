#Faster way to sort m-bit integers, if m small
#n = len(array)
#The complexity will be O(m*n)

#idea: we sort for each pass of x in range(maxLen), the int by its least significant digit

originalList = [170, 45, 75, 90, 802, 2, 24, 66]

#After 1st path:

bins = [[170 , 90] , [] , [802 , 2] , [] , [24] , [45 , 75] , [66] , [] , [] , []]

#then the queue:

queue = [170 , 90 , 802 , 2 , 24 , 45 , 75 , 66]

#After 2nd path:

bins = [[802 , 2] , [] , [24] , [] , [45] , [] , [66] , [170 , 75] , [] , [90]]

#then the queue:

queue = [802 , 2 , 24 , 45 , 66 , 170 , 75 , 90]

#After 3rd path:

bins = [[2 , 24 , 45 , 66 , 75] , [170] , [] , [] , [] , [] , [] , [] , [802] , []]

#then the queue:

queue = [2 , 24 , 45 , 66 , 75 , 170 , 802]

def radixSort(originalList , n , maxLen):
    queue = originalList
    for x in range(maxLen):
        bins = [[] for i in range(n)]
        for y in queue:
            bins[(y/10**x)%n].append(y)
        queue = []
        for section in bins:
            queue.extend(section)
    return queue

if __name__ == "__main__":
    import random
    import timeit
    a = [random.randint(0,10000) for i in xrange(1000000)]
    t = timeit.Timer('radixSort(a, 10, 5)', 'from __main__ import radixSort, a')
    print t.timeit(number=1)
