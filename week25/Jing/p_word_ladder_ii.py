"""
From: https://oj.leetcode.com/problems/word-ladder-ii/
Author: Jing Zhou
Date: Sep 18, 2014
Thought: This one is hard... 2 sets
Tags: word, ladder, BFS
"""



class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        if len(dict) == 0:
            return 0
        def buildPath(path, word):
            if len(prevDict[word])==0:
                path.append(word); currPath=path[:]
                currPath.reverse(); res.append(currPath)
                path.pop();
                return
            path.append(word)
            for prev in prevDict[word]:
                buildPath(path, prev)
            path.pop()
        level = set()
        nextLevel = set()
        level.add(start)
        dict.add(end)
        res = []
        levelWords = set()
        prevDict = {string: [] for string in dict}
        while True:
            #dict = dict.difference(level)
            for item in level:
                dict.remove(item)
            for cur in level:
                for i in range(len(cur)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if cur[i] != j:
                            newWord = cur[:i]+j+cur[i+1:]
                            if newWord in dict:
                                nextLevel.add(newWord)
                                prevDict[newWord].append(cur)
            if not nextLevel:
                return res
            if end in nextLevel:
                    break
            level.clear()
            level, nextLevel = nextLevel, level
        buildPath([], end)
        return res
