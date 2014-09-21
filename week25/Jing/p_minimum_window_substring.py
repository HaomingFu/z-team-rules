"""
From: https://oj.leetcode.com/problems/minimum-window-substring/
Author: Jing Zhou
Date: Sep 21, 2014
Thought: Two dictionaries and keep a invariant
Tags: string substring optimal
"""



class Solution:
    # @return a string
    def minWindow(self, S, T):
        if not T:
            return ""
        need_to_find = {}
        for char in T:
            if char not in need_to_find:
                need_to_find[char] = 1
            else:
                need_to_find[char] += 1
        has_find = {char: 0 for char in need_to_find}
        length_s, length_T = len(S), len(T)
        i = j = count = 0
        min_keep, max_keep = 0, -1
        min_sub_length = float('inf')
        while i < length_s:
            if S[i] in need_to_find:
                if has_find[S[i]] < need_to_find[S[i]]:
                    count += 1
                has_find[S[i]] += 1
                if count == length_T:
                    while S[j] not in need_to_find:
                            j += 1
                    while has_find[S[j]] > need_to_find[S[j]]:
                        has_find[S[j]] -= 1
                        j += 1
                        while S[j] not in need_to_find:
                            j += 1
                    if i-j < min_sub_length:
                        min_sub_length = i-j
                        min_keep, max_keep = j, i
            i += 1
        return S[min_keep: max_keep+1] if count == length_T else ""
