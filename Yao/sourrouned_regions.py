#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def solve(self, board):
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        m, n = len(board), len(board[0])
        startV = []
        for i in range(0,m):
            if board[i][0]=='O':
                startV.append((i,0))
            if board[i][n-1] == 'O':
                startV.append((i, n-1))
        for j in range(0, n):
            if board[0][j]=='O':
                startV.append((0,j))
            if board[m-1][j]=='O':
                startV.append((m-1,j))
        for i in range(0, m):
            board[i] = list(board[i])
        for start in startV:
            if board[start[0]][start[1]]=='O':
                self.move(start[0], start[1], m, n, board)

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j]=='K':
                    board[i][j] = 'O'
                elif board[i][j]=='O':
                    board[i][j] = 'X'
        for i in range(0, m):
            board[i] = "".join(board[i])

    def move(self, x, y, m, n, board):
        last = [(x,y)]
        while last:
            current = []
            for each in last:
                x, y = each[0], each[1]
                if board[x][y] == 'O':
                    board[x][y] = 'K'
                    if y < n-1 and board[x][y+1]=='O':
                        current.append((x,y+1))
                    if y > 0 and board[x][y-1]=='O':
                        current.append((x, y-1))
                    if x < m-1 and board[x+1][y]=='O':
                        current.append((x+1, y))
                    if x > 0 and board[x-1][y]=='O':
                        current.append((x-1, y))
            last = current


s = Solution()
board = ['XXXX', 'XOOX', 'XXOX', 'XOXX']
s.solve(board)
print(board)
