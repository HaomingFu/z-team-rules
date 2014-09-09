"""
From: http://oj.leetcode.com/problems/two-sum/
Author: Jing Zhou
Date: April 20, 2014
Idea: use a hash table/dictionary
Complexity: O(n)
Hardness: easy
"""

def twoSum(num, target):
    dic = {}
    for i, val in enumerate(num):
        print(i, val)
        if target - val in dic:
            return (dic[target-val], i+1)
        if val not in dic:
            dic[val] = i+1
    return ()

def test():
    print(twoSum([3, 2, 4], 6))

test()
