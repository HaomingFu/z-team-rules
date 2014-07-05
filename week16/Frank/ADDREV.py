#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
	for t in range(map(int, sys.stdin.readline().strip('\n').split())[0]):
		A, B = map(int, sys.stdin.readline().strip('\n').split())
		tmp = 0
		while A:
			tmp = tmp*10 + A%10
			A /= 10
		A = tmp
		tmp = 0
		while B:
			tmp = tmp*10 + B%10
			B /= 10
		B = tmp
		C = A + B
		tmp = 0
		while C:
			tmp = tmp*10 + C%10
			C /= 10
		print tmp

if __name__ == '__main__':
    main()
