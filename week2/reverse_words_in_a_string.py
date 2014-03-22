"""
Jing 3/20, 2014
http://oj.leetcode.com/problems/reverse-words-in-a-string/
"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join([word for word in reversed(s.split())])
