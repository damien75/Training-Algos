# source Hackerrank / Algorithms / Dynamic Programming / Play with words

# input: string of length n

# goal: find the max possible product of length of 2 non overlapping palindrome subsequence in string

# illustration with example: eeegeeksforskeeggeeks
# A possible optimal solution is eee-g-ee-ksfor-skeeggeeks being eeeee the one subsequence and skeeggeeks the other one.
# We can also select eegee in place of eeeee, as both have the same length.

# idea: solution in O(n log n) time complexity
# Let L[0, n - 1] be the longest palindrome subsequence of the substring s[0 : n - 1]
# if s[0] == s[n - 1]:
#   L[0, n - 1] = 2 + L[1, n - 2]
# else:
#   L[0, n - 1] = max(L[1, n - 1], L[0, n - 2])
# Finally the result is max(L[0, i] * L[i + 1, n - 1]) for i in [0, n - 1]


def play_with_words(s: str) -> int:
    n = len(s)
    l = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        l[i][i] = 1
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if s[i] == s[j] and cl == 2:
                l[i][j] = 2
            elif s[i] == s[j]:
                l[i][j] = l[i+1][j-1] + 2
            else:
                l[i][j] = max(l[i][j-1], l[i+1][j])

    max_prod = 0
    for i in range(1, n - 1):
        max_prod = max(max_prod, l[0][i] * l[i + 1][n - 1])

    return max_prod

if __name__ == '__main__':
    # Read input from Hackerrank
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = playWithWords(s)

    fptr.write(str(result) + '\n')

    fptr.close()
    """
    example = "eeegeeksforskeeggeeks"
    print("{} should equal 50".format(play_with_words(example)))
