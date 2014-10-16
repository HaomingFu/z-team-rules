#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        low, high = 0, n-1
        while low <= high:
            mid = (low + high) // 2
            if mid == low:
                break
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                low = mid
            else:
                high = mid
        for i in matrix[mid]:
            if i == target:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [
            [1, 3, 5, 7,],
            [23, 30, 34, 50]
            ]
    matrix2 = [[1]]
    target = 23
    print(s.searchMatrix(matrix, target))
