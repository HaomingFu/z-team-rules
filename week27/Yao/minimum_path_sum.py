#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/minimum-path-sum/
# Date: Oct. 1, 2014
# Status: AC

def minPathSum(self, grid):
    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    if m == 1:
        return sum(grid[0])
    if n == 1:
        return sum(sum(grid))
    for ix in range(1, m):
        grid[ix][0] = grid[ix-1][0] + grid[ix][0]
    for jx in range(1, n):
        grid[0][jx] += grid[0][jx-1]
    for ix in range(1, m):
        for jx in range(1, n):
            grid[ix][jx] = min(grid[ix-1][jx]) + grid[ix][ix]
    return grid[m-1][n-1]
