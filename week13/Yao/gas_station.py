# From: https://oj.leetcode.com/problems/gas-station/
# Date: June 8, 2014
# Status: Accepted

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)
        diff = [gas[i] - cost[i] for i in range(0, length)]
        if sum(diff)< 0:
            return -1
        i = 0
        while i < length:
            s = 0
            j = 0
            while j < length:
                s += diff[(i+j)%length]
                if s < 0:
                    i = i + j + 1
                    break
                j += 1
            if s >= 0:
                return i
        return -1

s = Solution()
gas = [1, 2, 3, 3]
cost = [2, 1, 5, 1]
print(s.canCompleteCircuit(gas, cost))
