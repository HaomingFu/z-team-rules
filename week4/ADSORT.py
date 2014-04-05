#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TIME: 0s MEM：4M 
STATUS:Accepted
DATE：April 5, 2014
From: http://www.spoj.com/submit/ADSORT/
"""
import sys

for t in range(int(sys.stdin.readline().strip())):
	print '+'.join(map(str, sorted(map(int, sys.stdin.readline().strip().split('+')))))
