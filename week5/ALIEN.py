#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Using sliding window alg 
STATUS:TLE
DATE：April 10, 2014
From: http://www.spoj.com/submit/ALIEN/
"""
__author__ = 'frankfu'

import sys
for t in range(int(sys.stdin.readline().strip())):
	At,Bt = map(int, sys.stdin.readline().strip().split())
	A = map(int, sys.stdin.readline().strip().split())
	nstations = 0
	npeople = 0
	front = 0
	back = -1
	nptmp = A[0]
	finished = False
	while True:
		if nptmp <= Bt and (front-back > nstations or (front-back == nstations and nptmp <= npeople)):
			nstations = front-back
			npeople = nptmp
		print front,back,nptmp
		if finished:
			break
		if nptmp <= Bt:
			front += 1
			if front <= At-1:
				nptmp += A[front]
			else:
				front -= 1
				finished = True
		else:
			back += 1
			nptmp -= A[back]
		print front,back,nptmp

		print npeople,nstations
	print str(npeople)+" "+str(nstations)
