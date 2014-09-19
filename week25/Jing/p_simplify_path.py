"""
From: https://oj.leetcode.com/problems/simplify-path/
Author: Jing Zhou
Date: Sep 15, 2014
Thought: Used a stack and very easy to pass...
Tags: stack, string, python
"""



class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        pathEle = path.split("/")
        stack = []
        for ele in pathEle:
            if ele == "..":
                if stack:
                    stack.pop()
            elif ele and ele != ".":
                stack.append(ele)
        if not stack:
            return "/"
        else:
            return "/"+"/".join(stack)
