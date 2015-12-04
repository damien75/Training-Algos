#source Hackerrank / Algorithms / Dynamic Programming / The Longest Common Subsequence

#input: 2 arrays A and B

#goal: find longest common subsequence

#idea: keep track of the subsequences we have seen so far => LCS(i , j) will be
#the longest subsequence from A[0..i] and B[0..j]
#We define LCS(i , j) as follows:
#if i == 0 or j == 0: LCS(i , j) = 0
#elif A[i] == A[j]: LCS(i , j) = LCS(i - 1 , j - 1) + A[i]
#else: LCS(i , j) = max(LCS(i - 1 , j) , LCS(i , j - 1))

def LCS(A , B):
    lcs = [[[]]*(len(B) + 1) for _ in range(len(A) + 1)]

    for i in range(1 , len(A) + 1):
        for j in range(1 , len(B) + 1):
            if A[i - 1] == B[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [A[i - 1]]
            else:
                if len(lcs[i - 1][j]) > len(lcs[i][j - 1]):
                    lcs[i][j] = lcs[i - 1][j]
                else:
                    lcs[i][j] = lcs[i][j - 1]
    return lcs[-1][-1]

#Read input from Hackerrank
"""n , m = map(int , raw_input().split())
A = map(int , raw_input().split())
B = map(int , raw_input().split())
print " ".join(str(el) for el in LCS(A , B))
"""

#Custom Inputs
if __name__ == "__main__":
    n = 5
    m = 6
    A = [1 , 2 , 3 , 4 , 1]
    B = [3 , 4 , 1 , 2 , 1 , 3]
    print " ".join(str(el) for el in LCS(A , B))

    A = ['G' , 'A' , 'C']
    B = ['A' , 'G' , 'C' , 'A' , 'T']
    print " ".join(str(el) for el in LCS(A , B))
