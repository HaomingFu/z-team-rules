"""
Problem: http://oj.leetcode.com/problems/pascals-triangle-ii/
Author: Jing Zhou
Solution idea came from the internet
Date: 11/4/2014
Idea: keep only one list, change it to next row from the previous row
"""
def getRow(rowIndex):
    res = []
    for i in xrange(rowIndex+1):
        for j in xrange(i-1, 0, -1):
            res[j] = res[j] + res[j-1]
        res.append(1)
    return res

for i in xrange(10):
    print(getRow(i))
