#From: https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
# Date: August 4
# Status:  Accepted
class Solution:
    # @param a string
    # @param return an integer
    def lengthOfLongestSubstring(self, s):
        strLen = len(s)
        if strLen < 2:
            return  strLen
        d = 1
        maxLen = 1
        dist = dict()
        dist[s[0]] = 0
        for i in range(1, strLen):
            if  s[i] not in dist or dist[s[i]] < i -d:
                d = d + 1
            else:
                d = i - dist[s[i]]
            dist[s[i]] = i
            if d > maxLen:
                maxLen = d
        return maxLen

s = Solution()
print(s.lengthOfLongestSubstring('abcda'))
