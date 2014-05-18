"""
From:
Author: Jing Zhou
Date: May 16, 2014
Thought: quite easyyyy, just used a dictionary
"""


class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dic = {}
        for aStr in strs:
            if "".join(sorted(aStr)) not in dic:
                dic["".join(sorted(aStr))] = [aStr]
            else:
                dic["".join(sorted(aStr))].append(aStr)
        return [j for i, val in dic.items() if len(val) > 1 for j in val]
