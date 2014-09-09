#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Using a list as stack with python
TIME:0.13 MEM：4.0M（HELP！）
STATUS:Accepted
DATE：March 29, 2014
From: http://www.spoj.com/submit/ONP/
"""
__author__ = 'frankfu'

def main():
	for i in range(int(raw_input('').strip())):
		stack = []
		for char in raw_input('').strip():
			if(char == ')'):
				stack[-4] = stack[-3]+stack[-1]+stack[-2]
				stack.pop()
				stack.pop()
				stack.pop()
			elif(char.isalpha() or char in ['+', '-', '*', '/', '^'] or char=='('):
				stack.append(char)
		print stack[0]
	return 0

if __name__ == '__main__':
	main()

