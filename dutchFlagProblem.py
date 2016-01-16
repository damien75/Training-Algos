#input: integer array, int low, int high

#goal: put all values lower than low on left, all values higher than high on right, in a single pass

#idea: have 2 pointers for the left and right limits and one pointer looking at
#elements not yet seen in the middle

def swap(ar , i , j):
    temp = ar[i]
    ar[i] = ar[j]
    ar[j] = temp

def partition(ar , low , high):
    left , right = 0 , len(ar) - 1
    mid = left
    while mid <= right:
        if ar[mid] < low:
            swap(ar , mid , left)
            mid += 1
            left += 1
        elif ar[mid] > high:
            swap(ar , mid , right)
            right -= 1
        else:
            mid += 1
    return ar

print partition([ 3, 1, 4, 9, 8, 2, 6, 9, 0 ] , 4 , 8)
