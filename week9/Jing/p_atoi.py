"""
From: http://oj.leetcode.com/problems/string-to-integer-atoi/
Author: Jing Zhou
Date: May 10, 2014
Thought: too easy...
"""
class Solution:
    # @return an integer
    def atoi(self, str):
        new_str = str.strip()
        end = ""
        for i, val in enumerate(new_str):
            if val in ['+', '-'] and i == 0:
                end += val
            elif val.isdigit():
                end += val
            else:
                break
        if end in ['+', '-']:
            end = ""
        end = int(end) if end else 0
        if end > 2147483647:
            return 2147483647
        if end < -2147483648:
            return -2147483648
        return end
