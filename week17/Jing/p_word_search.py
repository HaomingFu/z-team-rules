"""
From: https://oj.leetcode.com/problems/word-search/
Author: Jing Zhou
Date: Jul 12, 2014
Thought: A search. keep a visted list and here, the use of copying a list is quite important.
References:
    1. http://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list-in-python
"""



class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not board:
            return True if not word else False
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = []
                if self.search(word, visited, board, i, j):
                    return True
        return False
    def search(self, word, visited, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if (i,j) not in visited and word[0] == board[i][j]:
            if len(word) == 1:
                return True
            visited.append((i,j))
            # Note here the use of visited[:] to copy the list. Or else, the visited list would be changed in the second or
            return self.search(word[1:], visited[:], board, i-1, j) or self.search(word[1:], visited[:], board, i+1, j) or self.search(word[1:], visited[:], board, i, j-1) or self.search(word[1:], visited[:], board, i, j+1)
        return False
