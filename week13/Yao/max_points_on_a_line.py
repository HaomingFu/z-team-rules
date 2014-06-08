# From: https://oj.leetcode.com/problems/max-points-on-a-line/
# Date: June 8, 2014
# Status:

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of points
    # @return an integer
    def maxPoints(self, points):
        length = len(points)
        if length <= 2:
            return length
        maxPnts = 0
        for i in range(0, length):
            slopNumDict = {}
            duplicate = 0
            for j in range(0, length):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    continue
                if points[i].x == points[j].x:
                    slopNumDict['v'] = slopNumDict.get('v', 1) + 1
                    continue
                slop = (points[i].y - points[j].y) / (points[i].x - points[j].x)
                slopNumDict[slop] = slopNumDict.get(slop, 1) + 1
            if slopNumDict.values():
                mx = max(slopNumDict.values())
                maxPnts = maxPnts if maxPnts >= mx + duplicate  else  mx + duplicate
        return maxPnts

if __name__ == "__main__":
    s  = Solution()
    points = [Point(0, 0), Point(1, 1), Point(1, -1)]
    print(s.maxPoints(points))

