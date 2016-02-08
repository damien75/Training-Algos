#input : integer array of length n + 1 containing integers in range(n)

#goal: Find the duplicate

#idea: Run a first time 2 pointers with different speed until they meet in the cycle,
#then run again with same speed so that they meet at the beginning of the cycle

#complexity: O(n) in time and O(1) in space!!!

#Example:
ar = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 8]

#step 1:
#slow => 1 , fast => 2
#step 2:
#slow => 2 , fast => 4
#step 3:
#slow => 3 , fast => 6
#step 4:
#slow => 4 , fast => 8
#step 5:
#slow => 5 , fast => 10
#step 6:
#slow => 6 , fast => 12
#step 7:
#slow => 7 , fast => 9
#step 8:
#slow => 8 , fast => 11
#step 9:
#slow => 9 , fast => 8
#step 10:
#slow => 10 , fast => 10 <-- they meet, but not necessarily at the entry of the loop

#Say slow has done k steps and fast 2k, and the entry of the cycle was at distance n
#During the second loop, suppose find does k steps,
#then slow will have done 2k steps and they have to meet again, as before
#They were both moving at the same speed, so if they met before we would have stopped,
#and that would have been the entry, else if they meet only at 2k then this is the entry point


def findDuplicate(ar):
    fast = slow = find =0
    slow = ar[slow]
    fast = ar[ar[fast]]
    while fast != slow: #First loop
        slow = ar[slow]
        fast = ar[ar[fast]]
    while find != slow: #Second loop
        find = ar[find]
        slow = ar[slow]
    return find

print findDuplicate(ar) , "should be" , 8
