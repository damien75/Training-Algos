#Source Hackerrank / Algorithms / Sorting / Quicksort In-Place

#input: array of integers

#goal: Return sorted array of integers, printing the array at each step of the partitioning method

class QuickSort:
    def __init__(self , ar):
        self.ar = ar

    def swap(self , i , j):
        temp = self.ar[i]
        self.ar[i] = self.ar[j]
        self.ar[j] = temp

    def partition(self , l , r):
        index = l
        for i in range(l , r - 1):
            if self.ar[i] <= self.ar[r - 1]:
                self.swap(i , index)
                index += 1
        self.swap(r - 1 , index)
        return index

    def quickSort(self , l , r):
        if r - l > 1:
            pos = self.partition(l , r)
            self.printEl(0 , len(self.ar))
            self.quickSort(l , pos)
            self.quickSort(pos + 1 , r)

    def printEl(self , l , r):
        for i in range(l , r):
            print self.ar[i],
        print

#Read the input from Hackerrank
"""m = input()
ar = [int(i) for i in raw_input().strip().split()]
sAr = QuickSort(ar)
sAr.quickSort(0 , len(ar))"""

#Custom Inputs
ar = [1 , 3 , 9 , 8 , 2 , 7 , 5]
sAr = QuickSort(ar)
sAr.quickSort(0 , len(ar))
