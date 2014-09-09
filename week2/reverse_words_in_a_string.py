"""
Jing 3/20, 2014
http://oj.leetcode.com/problems/reverse-words-in-a-string/
"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1]) # This is the fastest
        #return ' '.join(reversed(s.split())) #second best
        #this one also passed the test but not very good
        #return ' '.join([word for word in reversed(s.split())])
