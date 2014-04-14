#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'frankfu'

import sys
inputfile = open('cookieclicker.in','r')
outputfile = open('cookieclicker.out','w')
# 1=<t<=100
for t in range(int(inputfile.readline().strip())):
	# 1=<C<=500  1<=F<=4  1<=X<=2000 
	C,F,X = map(float, inputfile.readline().strip().split())
	V = 2
	T = 0
	while X/(V+F) < (X-C)/V:
		T += C/V
		V = V+F
	T += X/V
	outputfile.write("Case #")
	outputfile.write("%d" % (t+1))
	outputfile.write(": ")
	outputfile.write("%.7f" % T)
	outputfile.write("\n")

