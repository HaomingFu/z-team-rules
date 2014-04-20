"""
Question from: http://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/
Author: Jing Zhou
Date: 3/22, 2014
Version: 3(first 2 TLE, the last one passed ok)
Time complexity: O(n), iterate list 4 times
Lesson learned: the best way to reversed a sequence(list or string) is by [::-1].
list(reversed()) is much slower so it should be avoided.
nl = list(pre_list) nl.reverse() is the second best approach
See: http://stackoverflow.com/a/3705705/1062364
"""
def maxProfit(prices):
    if not prices:
        return 0
    mins = [prices[0]]
    for i in range(1, len(prices)):
        mins.append(min(mins[-1], prices[i]))
    maxs = [prices[-1]]
    prices.reverse()
    for i in range(1, len(prices)):
        maxs.append(max(maxs[-1], prices[i]))

    return max([list(reversed(maxs))[i]-mins[i] for i in range(len(mins))])
print(maxProfit(prices))

"""
This is the version that passed the test.
The only differences being
1. this version didn't reversed any list
2. this version pre-calculated the length
"""
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        length = len(prices)
        mins, maxs = [prices[0]], [prices[-1]]
        for i in range(1, length):
            mins.append(min(mins[-1], prices[i]))
        for i in range(length-1, 0, -1):
            maxs.append(max(maxs[-1], prices[i]))

        return max([maxs[length-1-i]-mins[i] for i in range(length)])
