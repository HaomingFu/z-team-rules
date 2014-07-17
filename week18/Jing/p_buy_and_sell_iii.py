"""
From: https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Author: Jing Zhou
Date: Jul 15, 2014
Thought: no need to use DP. Can be solved in O(n)
"""



class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        minArray = [prices[0]]
        len_prices = len(prices)-1
        for i, val in enumerate(prices):
            if i > 0:
                minArray.append(val if val < minArray[-1] else minArray[-1])
        firstPart = [i - j for i,j in zip(prices, minArray)]
        for i in range(1, len(firstPart)):
            if firstPart[i] < firstPart[i-1]:
                firstPart[i] = firstPart[i-1]
        maxElement = prices[-1]
        maxRes = 0
        for i, val in enumerate(reversed(prices)):
            if val > maxElement:
                maxElement = val
            res = maxElement - prices[len_prices-i] + firstPart[len_prices-i]
            if res > maxRes:
                maxRes = res
        return maxRes
