"""
From: https://oj.leetcode.com/problems/valid-sudoku/
Author: Jing Zhou
Date: May 20, 2014
Thought: There should be a easier solution, will look at it later
"""



class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            numbers = []
            for j in range(9):
                if board[i][j] != '.':
                    numbers.append(board[i][j])
            if len(set(numbers)) != len(numbers):
                return False
        for j in range(9):
            numbers = []
            for i in range(9):
                if board[i][j] != '.':
                    numbers.append(board[i][j])
            if len(set(numbers)) != len(numbers):
                return False
        for i in range(3):
            for j in range(3):
                numbers = []
                for k in range(3*i, 3*i+3):
                    for m in range(3*j, 3*j+3):
                        if board[k][m] != '.':
                            numbers.append(board[k][m])
                if len(set(numbers)) != len(numbers):
                    return False
        return True
