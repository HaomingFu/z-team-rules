#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def getPermutation(self, n, k):
        nums = [i+1 for i in range(n)]
        res =""
        k -= 1
        perm = 1
        for i in range(1, n+1):
            perm *= i

        for ix in range(0, n):
            perm /= (n-ix)
            index = k / perm
            res += str(nums[index])
            nums.pop(index)
            k = k % perm
        return res


s = Solution()
print(s.getPermutation(3, 1))

