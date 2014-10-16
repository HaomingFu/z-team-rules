#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def permute(self, num):
        if not num:
            return []
        n = len(num)
        res = []
        li = []
        visited = [False]*n
        self.dfs(num, visited, 0, res, li)
        return res

    def dfs(self, num, visited, index, res, li):
        n = len(num)
        if index == n:
            res.append(li)
            return

        for ix in range(0, n):
            if not visited[ix]:
                visited[ix] = True
                li.append(num[ix])
                self.dfs(num, visited, index + 1, res, li)
                visited[ix] = False
                li.remove(num[ix])

if __name__ == "__main__":
    s = Solution()
    num = [1, 2, 3]
    print(s.permute(num))
