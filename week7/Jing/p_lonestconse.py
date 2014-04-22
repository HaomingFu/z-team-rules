"""
From: http://oj.leetcode.com/problems/longest-consecutive-sequence/
Author: Jing Zhou
Date: April 21, 2014
Complexity: O(n)
Hardness: not very hard but the use of set is not very obvious
"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        seqSet = set()
        maximum = 1
        for i in num:
            seqSet.add(i)
        for j in num:
            count,k,m  = 1, 1, -1
            while(j+k in seqSet):
                seqSet.remove(j+k)
                count += 1
                k += 1
            while j+m in seqSet:
                seqSet.remove(j+m)
                count += 1
                m -= 1
            if count > maximum:
                maximum = count
        return maximum
