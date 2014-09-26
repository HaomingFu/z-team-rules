"""
From: http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
Author: Jing Zhou
Date: Sep 25, 2014
Thought: A nice dynamic programming problem
Tags: DP, dynamic programming
"""




def lis(array):
    lis = [1 for val in array]
    pre_dict = {}
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                pre_dict[i] = j

    max_index = lis.index(max(lis))
    key = max_index
    res = []
    res.append(array[key])
    while key in pre_dict:
        key = pre_dict[key]
        res.append(array[key])

    res.reverse()
    return max(lis), res


print(lis([10, 22, 9, 33, 21, 50, 41, 60]))
