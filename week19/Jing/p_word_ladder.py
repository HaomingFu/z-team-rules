"""
From: https://oj.leetcode.com/problems/word-ladder/
Author: Jing Zhou
Date: Jul 30, 2014
Thought: This can be seen as a graph problem and can use BFS to solve
Tags: BFS, string, graph
"""




class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if len(dict) == 0:
            return 0
        dict = set(dict)
        #dict.add(end)
        wordsQueue = collections.deque()
        length = collections.deque()
        wordsQueue.append(start)
        length.append(1)
        while(wordsQueue):
            cur = wordsQueue.popleft()
            curDistance = length.popleft()
            for i in range(len(cur)):
                for j in range(ord('a'), ord('z')+1):
                    newWord = cur[:i]+chr(j)+cur[i+1:]
                    if newWord == end:
                        return curDistance + 1
                    if newWord in dict:
                        wordsQueue.append(newWord)
                        length.append(curDistance+1)
                        dict.remove(newWord)
        return 0
