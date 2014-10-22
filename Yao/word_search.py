#!/usr/bin/env python
# encoding: utf-8

class Solution:

    def exist(self, board, word):
        if len(word)< 1 or len(board) < 1:
            return False
        m, n= len(board), len(board[0])
        startv = []
        for ix in range(0, m):
            for jx in range(0, n):
                if board[ix][jx] == word[0]:
                    startv.append((ix,jx))

        for start in startv:
            if self.find(start[0], start[1], word, board,[], m, n):
                return True
        return False

    def find(self, ix, jx, word, board, visited, m,n):
        print("ix = %d, jx = %d" % (ix, jx))
        print(visited)
        if len(word) == 1:
            return board[ix][jx]==word[0]
        if board[ix][jx]!=word[0]:
            return False

        visited.append((ix,jx))
        if jx < n-1 and (ix,jx+1) not in visited and board[ix][jx+1] == word[1]:
            if self.find(ix,jx+1,word[1:],board,visited, m,n):
                return True
        if jx > 0 and (ix, jx-1) not in visited and board[ix][jx-1] == word[1]:
            if self.find(ix, jx-1, word[1:], board, visited, m, n):
                return True

        if ix < m-1 and (ix+1, jx) not in visited and board[ix+1][jx] == word[1]:
            if self.find(ix+1, jx, word[1:], board, visited, m, n):
                return True
        if ix > 0 and (ix-1, jx) not in visited and board[ix-1][jx] == word[1]:
            if self.find(ix-1, jx, word[1:], board, visited, m, n):
                return True
        return False



board = ["abce", "sfes", "adee"]
word3 = "abceseeefs"
s = Solution()
print(s.exist(board, word3))
