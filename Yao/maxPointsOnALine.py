#!/usr/bin/env python
# encoding: utf-8

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <=2:
            return n

        maxPnts = 0
        for ix in range(0, n):
            slopDict = {}
            duplicate = -1
            for jx in range(0, n):
                if points[ix].x == points[jx].x and points[ix].y==points[jx].y:
                    duplicate += 1
                    continue
                if points[ix].x == points[jx].x:
                    slopDict['v'] = slopDict.get('v', 1) + 1
                    continue
                slop = (points[ix].y - points[jx].y) / (points[ix].x - points[jx].x)
                slopDict[slop] = slopDict.get(slop, 1) + 1
            if slopDict.values():
                mx = max(slopDict.values())
                maxPnts = max(maxPnts, mx + duplicate)
            else:
                maxPnts = max(maxPnts, duplicate + 1)
        return maxPnts

s = Solution()
testValue = [(84,250),(0,0),(1,0),(0,-70),(0,-70),(1,-1),(21,10),(42,90),(-42,-230)]
points = [Point(x, y) for x, y in testValue]
print(s.maxPoints(points))


