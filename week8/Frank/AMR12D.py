#!/usr/bin/env python
# -*- coding: utf-8 -*-

def AMR12D():
	from sys import stdin
	lines = stdin.readlines()
	for t in range(map(int, lines[0].split())[0]):#1 <= T <= 100  1 <= |S| <= 10
		s = lines[t+1].strip('\n')
		l = len(s)
		tag = 0
		for i in range(l>>1):
			if s[i] != s[l-1-i]:
				tag = 1
				break
		if tag:
			print 'NO'
		else:
			print 'YES'			
AMR12D()
