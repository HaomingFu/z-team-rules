#!/usr/bin/env python
# -*- coding: utf-8 -*-

#answer is less than 1000000000
p=5**.5;
g=lambda n:((1+p)**n-(1-p)**n)/(p*2**n);

def AMZRCK():
	from sys import stdin
	lines = stdin.readlines()
	for t in range(map(int, lines[0].split())[0]):
		print "%.f"%g(map(int, lines[t+1].split())[0]+2)
AMZRCK()
