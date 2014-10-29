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
        visited.append((ix,jx))
        print("ix = %d, jx = %d" % (ix, jx))
        print(visited)
        if len(word) == 1:
            return board[ix][jx]==word[0]
        if board[ix][jx]!=word[0]:
            return False

        if jx < n-1 and (ix,jx+1) not in visited:
            if self.find(ix,jx+1,word[1:],board,visited, m,n):
                return True
            else:
                visited.remove((ix,jx+1))
        if jx > 0 and (ix, jx-1) not in visited:
            if self.find(ix, jx-1, word[1:], board, visited, m, n):
                return True
            else:
                visited.remove((ix, jx-1))

        if ix < m-1 and (ix+1, jx) not in visited:
            if self.find(ix+1, jx, word[1:], board, visited, m, n):
                return True
            else:
                visited.remove((ix+1, jx))
        if ix > 0 and (ix-1, jx) not in visited:
            if self.find(ix-1, jx, word[1:], board, visited, m, n):
                return True
            else:
                visited.remove((ix-1, jx))
        return False



board = ["abce", "sfes", "adee"]
word3 = "abceseeefs"
board2 = ['ab', 'cd']
word2 = 'acdb'
s = Solution()
print(s.exist(board2, word2))

