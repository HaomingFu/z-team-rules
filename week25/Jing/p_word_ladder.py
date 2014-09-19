"""
From: https://oj.leetcode.com/problems/word-ladder/
Author: Jing Zhou
Date: Sep 18, 2014
Thought: BFS seach
Tags: BFS, graph, word laddar, queue
"""



class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if len(dict) == 0:
            return 0
        wordsQueue = collections.deque()
        wordsQueue.append((start, 1))
        dict.add(end)
        while(wordsQueue):
            cur, curDistance = wordsQueue.popleft()
            for i in range(len(cur)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = cur[:i]+j+cur[i+1:]
                    if newWord == end:
                        return curDistance + 1
                    if newWord in dict:
                        wordsQueue.append((newWord, curDistance + 1))
                        dict.remove(newWord)
        return 0
