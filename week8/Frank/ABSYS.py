#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

for t in range(map(int, sys.stdin.readline().strip('\n').split())[0]):
	sys.stdin.readline()
	num1,opr1,num2,opr2,num3 = sys.stdin.readline().split()
	if "machula" in num3:
		print num1, opr1, num2, opr2, int(num1)+int(num2)
	if "machula" in num1:
		print int(num3)-int(num2), opr1, num2, opr2, num3
	if "machula" in num2:
		print num1, opr1, int(num3)-int(num1), opr2, num3