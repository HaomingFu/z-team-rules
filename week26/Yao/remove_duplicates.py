#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def removeDuplicate(self, A):
        d = {}
        res = []
        for each in A:
            if not each in d:
                d[each]=1
                res.append(each)
            elif d[each] == 1:
                d[each] = 2
                res.append(each)
        A = res
        return A

if __name__ == "__main__":
    s = Solution()
    li = [1, 1, 1, 2 ]
    print(s.removeDuplicate(li))
