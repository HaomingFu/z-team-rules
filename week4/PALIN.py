#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
mainly consider cost time of type cast from str to int, only deal with one digit，deal K with str slices, consider boundary  input cases  
TIME: 1.39  MEM：4.0M  
STATUS:Accepted
DATE：April 2, 2014
From: http://www.spoj.com/submit/ONP/
"""
__author__ = 'frankfu'

#get the smallest palindrome larger than K by adding 1, deal with 9, even or odd
def getPalin(K, tmp, halfl, isEven):
	while(tmp >= 0 and K[tmp] == '9'):
		tmp -= 1
	#the index of dismatch >= 0
	if(tmp != -1):
		#unchanged part + adding 1 part + 0 part
		lhalf = K[0:tmp] + str(int(K[tmp])+1) + '0'*(halfl-1-tmp)
	else:
		#1 part + 0 part
		lhalf = '1'+halfl*'0'
	if(isEven):
		rhalf = lhalf[halfl-1::-1]
	else:
		rhalf = lhalf[halfl-2::-1]
	print lhalf+rhalf


def main():
	for t in range(int(raw_input())):
		K = raw_input()
		lk = len(K)
		isEven = False
		if(lk == 1):
			if(K[0] != '9'):
				print str(int(K[0])+1)
			else:
				print '11'
			continue	
		if(lk % 2 == 0):
			isEven = True
			#end index of lhalf and start index of rhalf of K, will change value
			kh = lk/2
			kl = lk/2-1
			#index of dismatched number(not 9) from middle to both ends, will change value
			tmp = lk/2-1
			#to get palin, will not change value
			halfl = lk/2
		else:
			kh = lk/2+1
			kl = lk/2-1
			tmp = lk/2
			#including midlle digit
			halfl = lk/2+1
		#find the index of dismatch
		while(kl >= 0 and K[kh] == K[kl]):
			kh += 1
			kl -= 1
		#lhalf is totally equal to rhalf
		if(kl < 0):
			#get palin based on K by adding 1, deal with 9,odd or even,middle digit
			getPalin(K, tmp, halfl, isEven)
		else:
			#the digit of the index of dismatch at lhalf > rhalf. 12311, 2>1. 123311, 2>1.  
			if(int(K[kl]) > int(K[kh])):
				lhalf = K[:halfl]
				if(isEven):
					rhalf = lhalf[halfl-1::-1]
				else:
					rhalf = lhalf[halfl-2::-1]
				print lhalf+rhalf
			else:
				getPalin(K, tmp, halfl, isEven)											
	return 0

if __name__ == '__main__':
	main()

