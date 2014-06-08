# From: https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Date: June 7, 2014
# Status:  Accepted

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        minPrice = prices[0]
        maxPrice = prices[1]
        if minPrice > maxPrice:
            minPrice = maxPrice
        i = 2
        less = minPrice
        while i < len(prices):
            if prices[i] > maxPrice:
                maxPrice = prices[i]
                minPrice = less
            elif prices[i] < less:
                less = prices[i]
            elif maxPrice - minPrice < prices[i] - less:
                maxPrice = prices[i]
                minPrice = less
            i += 1
        return maxPrice - minPrice


if __name__ == "__main__":
    s = Solution()
    prices = [7, 4, 1, 2]
    print(s.maxProfit(prices))
