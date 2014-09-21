"""
From: https://oj.leetcode.com/problems/word-break-ii/
Author: Jing Zhou
Date: Sep 21, 2014
Thought: used the build path routine again
Tags: DFS, word, break, DP
"""



class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        res = []
        def buildPath(path, index):
            if index == -1:
                path_copy = path[:]
                path_copy.reverse()
                res.append(" ".join(path_copy))
                return
            else:
                for neighbor in marks[index]:
                    path.append(neighbor[1])
                    buildPath(path, neighbor[0])
                    path.pop()

        wordDict = set(dict)
        indicator = [False]*len(s)
        marks = {}
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    if i == 0 or indicator[i-1]:
                        indicator[j-1] = True
                        if j-1 not in marks:
                            marks[j-1] = set([(i-1,s[i:j])])
                        else:
                            marks[j-1].add((i-1, s[i:j]))
        if not indicator[-1]:
            return []
        buildPath([], len(s)-1)
        return res
