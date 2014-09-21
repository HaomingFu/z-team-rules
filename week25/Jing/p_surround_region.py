"""
From: https://oj.leetcode.com/problems/surrounded-regions/
Author: Jing Zhou
Date: Sep 21, 2014
Thought: DFS problem. not hard...
Tags: graph, dfs, matrix
"""



class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board) <= 1 or len(board[0]) <= 1:
            return board
        visited = set()
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if (i == 0 or j == 0 or i == row-1 or j == col-1) and board[i][j] == "O" and (i, j) not in visited:
                    visited.add((i, j))
                    self.DFS(i, j, row, col, visited, board)
        for i in range(1, row - 1):
            for j in range(1, col-1):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"

    def DFS(self, i, j, row, col, visited, board):
        stack = []
        stack.append((i,j))
        while stack:
            i,j = stack.pop()
            for m in [-1,1]:
                if 0 <= i+m < row and board[i+m][j] == "O" and (i+m, j) not in visited:
                    visited.add((i+m, j))
                    stack.append((i+m, j))
                if 0 <= j+m < col and board[i][j+m] == "O" and (i, j+m) not in visited:
                    visited.add((i, j+m))
                    stack.append((i, j+m))
