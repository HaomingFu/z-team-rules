# From: https://oj.leetcode.com/problems/triangle/
# Status: AC
# Date: Sep. 24, 2014
class Solution:
    # @triangle, a list of lists of integer
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return None
        num = len(triangle)
        if num==1:
            return triangle[0][0]
        for i in range(1, num):
            n = len(triangle[i])
            for ix in range(0, n):
                if ix==0:
                    triangle[i][ix] = triangle[i-1][0]+ triangle[i][ix]
                elif ix==n-1:
                    triangle[i][ix] = triangle[i-1][ix-1] + triangle[i][ix]
                else:
                    triangle[i][ix] = min(triangle[i-1][ix-1], triangle[i-1][ix]) + triangle[i][ix]
        return min(triangle[num-1])
