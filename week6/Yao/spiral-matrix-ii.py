# Accepted
# From http://oj.leetcode.com/problems/spiral-matrix-ii/
# Date: April 20, 2014
# By Yao

class Solution:
# @return a list of lists of integer
    def generateMatrix(self, n):
        count = 0
        matrix = []
        while count < n :
            matrix.append([0]*n)
            count += 1
        count = 1
        i = 0
        j = 0
        while count <= n*n:
            while j < n and matrix[i][j]==0:
                matrix[i][j]=count
                j += 1
                count += 1
            i += 1
            j -=1
            while i < n and matrix[i][j]==0:
                matrix[i][j] = count
                i += 1
                count += 1
            j -= 1
            i -= 1
            while j>= 0 and matrix[i][j]==0:
                matrix[i][j] = count
                j -= 1
                count += 1
            i -= 1
            j += 1
            while i>=0 and matrix[i][j] ==0:
                matrix[i][j] = count
                i -= 1
                count += 1
            i += 1
            j += 1
        return matrix

mysolution = Solution()
print(mysolution.generateMatrix(5))
