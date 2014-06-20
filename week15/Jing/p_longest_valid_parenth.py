"""
From: https://oj.leetcode.com/problems/longest-valid-parentheses/
Author: Jing Zhou
Date: Jun 19, 2014
Thought: Made use of a stack in this problem. And the index in the stack and current string
"""



class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if not s:
            return 0
        maxl = i = t = 0
        st = []
        while i < len(s):
            if s[i] == '(':
                st.append(('(', i))
            else:
                if not st:
                    t = i+1
                if st:
                    tmp = st[-1]
                    st.pop()
                    if tmp[0] == '(':
                        if st:
                            maxl = max(maxl, i-st[-1][1])
                        else:
                            maxl = max(maxl, i-t+1)
            i += 1
        return maxl
