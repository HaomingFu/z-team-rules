"""
Author: Jing Zhou
From: http://www.geeksforgeeks.org/printing-longest-common-subsequence/
Date: Sept. 26, 2014
Problem: Given two sequences, print the longest subsequence present in both of them
"""
def lcs(a, b):
    len_a = len(a)
    len_b = len(b)
    DP = [[0]*(len_b+1) for _ in range(len_a+1)]
    for i in range(len_a+1):
        for j in range(len_b+1):
            if i == 0 or j == 0:
                DP[i][j] = 0
            elif a[i-1] == b[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
    i, j = len_a, len_b
    res = []
    while i >0 and j >0:
        if a[i-1] == b[j-1]:
            res.append(a[i-1])
            i -= 1
            j -= 1
        elif a[i-1] > b[j-1]:
            i -= 1
        else:
            j -= 1
    res.reverse()
    return DP[len_a][len_b], "".join(res)

print(lcs("AGGTAB", "GXTXAYB"))
