#!/usr/bin/env python
# encoding: utf-8

class Solution:

    def findMin(self, num):
        n = len(num)
        return self.binarySearch(num, 0, n - 1)

    def binarySearch(self, num, low, high):
        if low == high:
            return num[low]
        if high - low == 1:
            return min(num[low], num[high])
        mid = (low + high)//2
        if num[mid] > num[low]:
            return min(num[low], self.binarySearch(num, mid+1, high))
        elif num[mid] < num[low]:
            return self.binarySearch(num, low, mid)
        else:
            return min(self.binarySearch(num,low, mid), self.binarySearch(num, mid + 1, high))

s = Solution()
num = [4]
print(s.findMin(num))

