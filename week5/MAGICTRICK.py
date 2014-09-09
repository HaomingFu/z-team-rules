#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'frankfu'

import sys
inputfile = open('magictrick.in','r')
outputfile = open('magictrick.out','w')
for t in range(int(inputfile.readline().strip())):
	Arr = ['']*2
	Arr[0] = ['']*4
	Arr[1] = ['']*4
	A1 = map(int, inputfile.readline().strip().split())
	Arr[0][0] = map(int, inputfile.readline().strip().split())
	Arr[0][1] = map(int, inputfile.readline().strip().split())
	Arr[0][2] = map(int, inputfile.readline().strip().split())
	Arr[0][3] = map(int, inputfile.readline().strip().split())
	A2 = map(int, inputfile.readline().strip().split())
	Arr[1][0] = map(int, inputfile.readline().strip().split())
	Arr[1][1] = map(int, inputfile.readline().strip().split())
	Arr[1][2] = map(int, inputfile.readline().strip().split())
	Arr[1][3] = map(int, inputfile.readline().strip().split())
	ret = ''
	count = 0
	val = 0
	for ll1 in Arr[0][A1[0]-1]:
		if ll1 in Arr[1][A2[0]-1]:
			count += 1
			val = ll1
	if count == 0:
		ret = 'Case #'+str(t+1)+': Volunteer cheated!'
	elif count == 1:
		ret =  'Case #'+str(t+1)+': '+str(val)
	else:
		ret = 'Case #'+str(t+1)+': Bad magician!'
	outputfile.write(ret+"\n")
