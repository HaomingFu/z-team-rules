#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import factorial
	
def main():
	for t in range(int(raw_input())):
		N = int(raw_input())
		print factorial(N)
	return 0
	
if __name__ == '__main__':
	main()
