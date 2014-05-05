#!/usr/bin/env python
# -*- coding: utf-8 -*-

def AMZSEQ():
	from sys import stdin
	ans = []
	ans.append(1)
	ans.append(3)
	i = 2
	n = map(int, stdin.readline().split())[0]
	while i <= n:
		ans.append(ans[i-1] + ans[i-2] + ans[i-1])
		i += 1
	print ans[n]
AMZSEQ()

