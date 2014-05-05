#!/usr/bin/env python
# -*- coding: utf-8 -*-

def AG():
	from sys import stdin
	lines = stdin.readlines()
	for line in lines:
		a1,a2,a3 = map(int,line.split())
		if a1 == a2 and a2 == a3 and a3 == 0:
			break
		tmp1 = a3-a2
		if a1 == 0 or a2 == 0 or a3 == 0 or a2-a1 == tmp1:
			print 'AP', tmp1+a3
			continue	
		else:
			tmp2 = a3/a2
			print 'GP', tmp2*tmp2*a2
			continue
AG()
