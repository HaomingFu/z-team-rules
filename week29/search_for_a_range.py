#!/usr/bin/env python
# encoding: utf-8

class Solution:

    def searchRange(self, A, target):
        if len(A) < 0:
            return [-1, -1]
        res = self.binarySearch(0, len(A)-1, A, target)
        if res == -1:
            return [-1, -1]

        res1= res
        while res1 != -1:
            low = res1
            res1 = self.binarySearch(0, res1-1, A, target)
        res2 = res
        while res2 != -1:
            high = res2
            res2 = self.binarySearch(res2+1,len(A)-1, A, target)

        return [low, high]


    def binarySearch(self, low, high, li, s):
        while high >= low:
            mid = (low + high) // 2
            if li[mid] > s:
                high = mid-1
            elif li[mid] < s:
                low = mid + 1
            else:
                return mid
        return -1



instance = Solution()
A = [1,1,1,1,1,1,2,3,4,4,5,5,5,6,7,8,8,8,8]
target = 8
print(instance.searchRange(A, target))
#print(binarySearch(0, len(A)-1,A, 7))




