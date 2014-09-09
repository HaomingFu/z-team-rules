#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
MOD = 1000000007
"""
Using matrix exponentiation, implement it with while loop rather than recursive function call
Refer to: http://fulmicoton.com/posts/fibonacci/   http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#exact 
http://nayuki.eigenstate.org/page/fast-fibonacci-algorithms
TIME: 4.4s MEM：4.0M 
STATUS:Accepted
DATE：April 8, 2014
From: http://www.spoj.com/submit/FIBOSUM/
"""
__author__ = 'frankfu'

#nonrecursive use while
def nonre_fibo_matrix(n):
	M = [[1,1], [1,0]] #or [[0,1], [1,1]] 
	ret = [[1,0], [0,1]]
	temp = [[0,0], [0,0]]
	while n:
		if n&1:
			temp = [[0,0], [0,0]]
			for i in range(2):
				for j in range(2):
					for k in range(2):
						temp[i][j] = (temp[i][j]+ret[i][k]*M[k][j])%MOD
			for i in range(2):
				for j in range(2):
					ret[i][j] = temp[i][j]
		n = n>>1
		if not n:
			break
		temp = [[0,0], [0,0]]
		for i in range(2):
			for j in range(2):
				for k in range(2):
					temp[i][j] = (temp[i][j]+M[i][k]*M[k][j])%MOD
		for i in range(2):
			for j in range(2):
				M[i][j] = temp[i][j]
	return (ret[0][1])%MOD
#t <= 1000
for t in range(int(sys.stdin.readline().strip())):
	#0<=N<=M<=10^9
	N,M = sys.stdin.readline().strip().split()
	N = int(N)
	M = int(M)
	#matrix exponentiation
	print (nonre_fibo_matrix(M+2)-nonre_fibo_matrix(N+1)+MOD)%MOD
	
