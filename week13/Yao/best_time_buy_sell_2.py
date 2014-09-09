# From: https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Date: June 7, 2014
# Status: Accepted

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <2:
            return 0
        profit = 0
        minPrice = prices[0]
        maxPrice = prices[1]
        if minPrice > maxPrice:
            minPrice = maxPrice
        i = 2
        while i < len(prices):
            if prices[i] <  maxPrice:
                profit += maxPrice - minPrice
                minPrice = maxPrice = prices[i]
            else:
                maxPrice = prices[i]
            i += 1
        profit += maxPrice - minPrice
        return profit

if __name__ == "__main__":
    s = Solution()
    prices = [10, 2, 5, 4, 6, 9, 2, 3]
    print(s.maxProfit(prices))

