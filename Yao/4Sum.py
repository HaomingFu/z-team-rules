class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        res = []
        n = len(num)
        if n < 4:
            return []
        pairSum = {}
        for i in range(n-1):
            for j in range(i + 1, n):
                sum = num[i] + num[j]
                if sum not in pairSum:
                    s = set()
                    s.add((i,j))
                    pairSum[sum] = s
                else:
                    pairSum[sum].add((i,j))
        reSet = set()

        for aSum in pairSum.keys():
            if target - aSum not in pairSum:
                continue
            pairs = pairSum[aSum]
            if target - aSum == aSum and len(pairs)==1:
                continue
            nPairs = pairSum[target - aSum]
            for aPair in pairs:
                for bPair in nPairs:
                    if aPair == bPair:
                        continue
                    if bPair[0] in aPair or bPair[1] in aPair:
                        continue
                    temp = sorted([num[aPair[0]], num[aPair[1]], num[bPair[0]], num[bPair[1]]])
                    if temp not in res:
                        res.append(temp)
        return res

s = Solution()
num = [1,0,-1,0,-2,2]
target = 0
print(s.fourSum(num, target))
