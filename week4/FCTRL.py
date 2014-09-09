#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 20=2^2*5^1   100=2^2*5^2. calculate the number of 5 in the Integer factorization result of N!.  
 only prime digit 2*5=10. prime factorizations of  10! has two 5, 20! has four 5, 
 but 30! has seven 5 not six 5 because of 25=5*5. ...
TIME: 2.97s MEM：4.3M 
STATUS:Accepted
DATE：April 3, 2014
From: http://www.spoj.com/submit/FCTRL/
"""
__author__ = 'frankfu'

from time import time
import sys

def Z(n):
	f = 5
	z = 0
	while(f <= n):
		z += n/f
		f *= 5
	print z
	
def Z1(n):
	z = 0
	while(5 <= n):
		z += n/5
		n = n/5
	print z
	
def main():
	for t in range(int(sys.stdin.readline().strip())):
		N = int(sys.stdin.readline().strip())
		Z(N)
	return 0
	
if __name__ == '__main__':
	main()
