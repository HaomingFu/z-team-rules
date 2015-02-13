#!/usr/bin/env python
# encoding: utf-8
class Solution:
        # @param num, a list of integers
        # @return a string
        def largestNumber(self, num):
            num = sorted(num, self.isGreater, reverse=True)
            print(num)
            return "".join([str(i) for i in num])

        def isGreater(self, x, y):
            print(x, y)
            xList, yList = [],[]
            if x == 0:
                xList = [0]
            if y== 0:
                yList =[0]
            while x :
                xList.append(x % 10)
                x = x // 10
            while y:
                yList.append(y % 10)
                y = y // 10
            xList.reverse()
            yList.reverse()

            n = max(len(xList), len(yList))
            for ix in range(n):
                xIndex = ix if ix < len(xList) else ix %  len(xList)
                yIndex = ix if ix < len(yList) else ix % len(yList)
                print(xIndex, yIndex)
                if xList[xIndex] > yList[yIndex]:
                    return 1
                if xList[xIndex] < yList[yIndex]:
                    return -1
            return 0

s = Solution()
num = [1440,7548,4240,6616,733,4712,883,8,9576]
print(s.largestNumber(num))
