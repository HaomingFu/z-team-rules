# https://oj.leetcode.com/problems/single-number-ii/
# Date: May 23, 2014
# status:  Accepted


# But with extra space, linear time

class Solution:
    # @param A, a list of integer
    # @return an integer
    def signleNumber(self, A):
        d = {}
        for i in A:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                if d[i] ==3:
                    d.pop(i)
        return [i for i in d][0]
