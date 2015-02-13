#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        res = []
        hashMap = dict()
        mymap = {'A':0, 'B':1, 'C':2,'D':3}
        sum = 0
        for ix in range(len(s)):
            sum = (sum*4 + mymap[s[ix]]) & 0xFFFFF
            if ix < 9:
                continue
            piece = s[ix-9:ix+1]
            hashMap[sum] = hashMap.get(sum, 0) + 1
            if hashMap[sum] == 2:
                res.append(piece)
        return res

s = Solution()

print(s.findRepeatedDnaSequences('G'))
