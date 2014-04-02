#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Using The Sieve of Eratosthenes alg.
Refer to: http://jamie-wong.com/2009/11/12/spoj-problem-2-prime-generator/
TIME: 1.65s MEM：4.6M 
STATUS:Accepted
DATE：April 1, 2014
From: http://www.spoj.com/submit/ONP/
"""
__author__ = 'frankfu'

from math import sqrt

def getBasicPrimes():
	primes = [2]
	for i in range(3,31630,2):
		#caption number 
		cap = sqrt(i) + 1
		isPrime = True
		for j in primes:
			#a number who could not be totally divided by primes smaller than cap is a prime too
			if(j >= cap):
				break
			if(i % j == 0):
				isPrime = False
		if(isPrime):
			primes.append(i)
	return primes

def main():
	#sqrt(1000,000,000) is 31622
	primes = getBasicPrimes()

	for t in range(int(raw_input())):
		m,n = raw_input().split()
		m = int(m)
		n = int(n)
		if(m < 2):
			m = 2
		#0=<n-m<=100000
		isPrime = [True] * 100001
		cap = sqrt(n) + 1		
		for j in primes:
			if(j >= cap):
				break
			if(j >= m):
				start = 2 * j
			else:
				# m =< start <= m+j and start%j == 0
				start = m + (j-m%j)%j
			falseblock = [False] * len(isPrime[start-m:n+1-m:j])
			isPrime[start-m:n+1-m:j] = falseblock
		for i in range(m, n+1):
			if(isPrime[i-m]):
				print i
		print 
	return 0

if __name__ == '__main__':
	main()

