"""
From: https://oj.leetcode.com/problems/sudoku-solver/
Author: Jing Zhou
Date: Sep 16, 2014
Thought: Very similar N-queens. backtracking problem.
Tags: backtracking, recursion, soduku
"""



class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    digits = "948732651"
    def solveSudoku(self, board):
        self.helper(board, 0, 0)

    def helper(self, board, i, j):
        if j >= 9:
            return self.helper(board, i+1, 0)
        if i == 9:
            return True
        if board[i][j] == ".":
            for k in self.digits:
                board[i][j] = k
                if self.isvalid(board, i, j):
                    if self.helper(board, i, j+1):
                        return True
                board[i][j] = "."
        else:
            return self.helper(board, i, j+1)
        return False

    def isvalid(self, board, i, j):
        for m in range(9):
            if m != i and board[m][j] == board[i][j]:
                return False
            if m != j and board[i][m] == board[i][j]:
                return False
        for row in range(i/3*3, i/3*3+3):
            for col in range(j/3*3, j/3*3+3):
                if (row != i or col != j) and board[row][col] == board[i][j]:
                    return False
        return True
