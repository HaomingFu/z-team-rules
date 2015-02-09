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
        
        for aSum in pairSum.keys():
            if target - aSum not in pairSum:
                continue
            pairs = pairSum[sum]
            if target - aSum == aSum and len(pairs)==1:
                continue
            nPairs = pairSum[target - aSum]
            for aPair in pairs:
                for bPair in nPairs:
                    if aPair == bPair:
                        continue
                    temp = [aPair[0], aPair[1], bPair[0], bPair[1]]
                    res.append(sorted(temp))
        return res
