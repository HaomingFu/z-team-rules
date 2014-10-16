#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def sortColors(self, A):
        mid = low = 0
        high = len(A) - 1
        while A[high] == 2 and high >-1:
            high -= 1
        while mid <= high:
            if A[mid] == 0:
                A[mid], A[low] = A[low], A[mid]
                low += 1
                mid += 1
            elif A[mid] ==  2:
                A[mid], A[high] = A[high], A[mid]
                high -= 1
            else:
                mid += 1

if __name__ == "__main__":
    s = Solution()
    A = [1, 0]
    s.sortColors(A)
    print(A)

