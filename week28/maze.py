#!/usr/bin/env python
# encoding: utf-8

"""
Given a maze, you can only move up, down, right and left. Start from
the start point and to see if you can arrive at the end point.
"""

fh = open("maze.txt", 'r')

N = int(fh.readline().strip())
M = int(fh.readline().strip())

maze = fh.readlines()
fh.close()

maze = [each.strip() for each in maze]
table = [[False]*N]*M
res = []

def solve(maze, N, M):
    n = len(maze)
    s_pos = 0
    g_pos = 0
    for ix in range(0, n):
        if 'S' in maze[ix]:
            s_pos = (ix, maze[ix].index('S'))
            if s_pos and g_pos:
                break
        if 'G' in maze[ix]:
            g_pos = (ix, maze[ix].index('G'))
            if s_pos and g_pos:
                break
    return s_pos, g_pos


def recursive(maze, N, M, S, G, step):
    if S ==G:
        res.append(step)
        maze[S[0]][S[1]] = True
        return
    if S[0] < M-1 and table[S[0]][S[1]] == False:
        recursive(maze, N, M, (S[0]+1, S[1]),G, step+1)
    if S[0] > 0 and  table[S[0]-1][S[1]] == False:
        recursive(maze, N, M, (S[0]-1, S[1]), G, step +1)
    if S[1] < N -1 and table[S[0]][S[1]+1]  == False:
        recursive(maze, N, M, (S[0], S[1]+1), G, step+1)
    if S[1] > 0 and table[S[0]][S[1]-1] == False:
        recursive(maze, N, M, (S[0], S[1]-1, G, step +1))
    return

S, G = solve(maze, N, M)
recursive(maze, N,M,S,G,0)




