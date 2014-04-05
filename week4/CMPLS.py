#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import match
import sys

def getPn(f, z, S, C):
	output = ''
	for i in range(S+1,S+C+1):
		y = f[0]
		for j in range(1, z):
			tmp = 1
			for k in range(1,j+1):
				tmp *= (i-k)
			y += f[j][0]*tmp
		output += str(int(y))+" "
	return output
	
def main():
	#equal to about 5000
	for t in range(int(sys.stdin.readline().strip())):
		output = ''
		#  1<=S<100, 1<=C<100, (S+C)<=100
		S,C = sys.stdin.readline().strip().split()
		S = int(S)
		C = int(C)
		slist = sys.stdin.readline().strip().split()
		#共S-1阶差分
		f = ['']*S
		slist[0] = int(slist[0])
		for i in range(1,S):
			slist[i] = int(slist[i])
			f[i] = ['']*(S-i)
		f[0] = slist[0]
		#处理极端情况 S=1
		if S == 1:
			for i in range(S+1,S+C+1):
				output += str(f[0])+' '
		else:
			i = 1
			for j in range(0,len(f[i])):
				f[i][j] = slist[j+1]-slist[j]
			for i in range(2, S):
				zerocount = 0
				for j in range(0,len(f[i])):
					f[i][j] = float((f[i-1][j+1]-f[i-1][j])*1.0/i)
					if(f[i][j] == 0):
						zerocount += 1
				#break when f[i][j] are 0
				if(zerocount == j+1):
					break
			if i == S-1:
				i = S
			output = getPn(f, i, S, C)
		print output
	return 0

if __name__ == '__main__':
	main()

