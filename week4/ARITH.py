#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
think too much, add/sub/mult one digit by one digit, consume too much time~but it pass the test
Refer to: http://searchcode.com/codesearch/view/39883030
STATUS:TLE
DATE：April 4, 2014
From: http://www.spoj.com/submit/ARITH/
"""

from re import match
import sys

def printCalculation(m, opr, n):
	lm = len(m)
	ln = len(n)
	output = ''
	result = ''
	lo = 0
	if(opr == '+'):
		i = lm-1
		j = ln-1
		carry = 0
		while(i >= 0 and j >= 0):
			tmp = int(m[i])+int(n[j])+carry
			if(tmp <= 9):
				carry = 0
				result += str(tmp)
			else:
				carry = 1
				result += str(tmp)[1]
			i -= 1
			j -= 1
		if(i == -1 and j == -1):
			#lm = ln
			if(carry == 1):
				result += '1'
			result = result[-1::-1]
			lo = ln+1
		elif(i == -1 and j != -1):
			#lm < ln  923 9234
			if(carry == 1):
				k = ln-lm-1 #k=0
				cons = ln-lm
				while(k >= 0 and n[k] == '9'):
					k -= 1
				if(k == -1): #923+999344
					head = '1'+cons*'0'
				else:  #923+9992344
					head = n[:k]+str(int(n[k])+1)+(cons-1-k)*'0'
			else:
				head = n[:ln-lm]
			result = head + result[-1::-1]
			lo = ln+1
		elif(i != -1 and j == -1):
			#lm > ln  9234 923
			if(carry == 1):
				k = lm-ln-1 #k=0
				cons = lm-ln
				while(k >= 0 and m[k] == '9'):
					k -= 1
				if(k == -1): #999344+923
					head = '1'+cons*'0'
				else:  #9992344+923
					head = m[:k]+str(int(m[k])+1)+(cons-1-k)*'0'
			else:
				head = m[:lm-ln]
			result = head + result[-1::-1]
			lo = lm+1 if len(result) > lm else lm
		ll = lo
		output += m.rjust(lo, ' ')+'\n'
		output += (opr+n).rjust(lo, ' ')+'\n'
		output += (lo*'-').rjust(lo, ' ')+'\n'
		output += result.rjust(lo, ' ')+'\n'
	elif(opr == '-'):
		i = lm-1
		j = ln-1
		borrow = 0
		while(i >= 0 and j >= 0):
			tmp = int(m[i])-borrow-int(n[j])
			if(tmp >= 0):
				borrow = 0
				result += str(tmp)
			else:
				borrow = 1
				tmp += 10
				result += str(tmp)
			i -= 1
			j -= 1
		if(i == -1 and j == -1):
			#lm = ln
			result = result[-1::-1]
			if(result.strip('0') == ''):
				result = '0'
			else:
				result = result.lstrip('0')			
			lo = ln+1
			ll = lo
		elif(i != -1 and j == -1):
			#lm > ln  
			if(borrow == 1): #30001-12
				k = lm-ln-1 #k=2
				cons = lm-ln
				while(k >= 0 and m[k] == '0'):
					k -= 1
				head = m[:k]+str(int(m[k])-1)+(cons-1-k)*'9'
			else: #30013-12
				head = m[:lm-ln]
			result = head + result[-1::-1]
			if(result.lstrip('0') == ''):
				result = '0'
			else:
				result = result.lstrip('0')			
			lr = len(result)
			lo = lm
			ll = ln+1 if ln+1 >= lr else lr 
		output += m.rjust(lo, ' ')+'\n'
		output += (opr+n).rjust(lo, ' ')+'\n'
		output += (ll*'-').rjust(lo, ' ')+'\n'
		output += result.rjust(lo, ' ')+'\n'
	elif(opr == '*'):
		j = ln-1
		tmpop = ['']*ln
		while(j >= 0):
			carry = 0
			i = lm-1
			while(i > 0):
				tmp = int(n[j])*int(m[i])+carry
				if(tmp > 9):
					carry = tmp/10
				else:
					carry = 0
				tmpop[j] += str(tmp%10)
				i -= 1
			if(i == 0):
				tmp = int(n[j])*int(m[i])+carry
				tmpop[j] = str(tmp)+tmpop[j][-1::-1]
			#print tmpop[j]
			j -= 1
		#calculate the result
		lo = len(tmpop[0])+ln-1
		ltmpop = len(tmpop)
		#REVERSE
		tmpop = tmpop[-1::-1]
		carry = 0
		for k in range(lo):
			tmp = 0
			for q in range(0,k+1):
				if(q <= ltmpop-1):
					inx = len(tmpop[q])-k+q-1
					if(inx >= 0):
						tmp += int(tmpop[q][inx])
				q += 1	
			tmp += carry
			if(tmp > 9):
				carry = tmp/10
			else:
				carry = 0
			result += str(tmp%10)
			k += 1
		if(carry != 0):
			result += str(carry)
		result = result[-1::-1]
		ll2 = len(result)
		ltmp = len(tmpop[0].lstrip('0'))
		ll1 = ln+1 if ln+1 >= ltmp else ltmp
		lo = ll1 if ll1>ll2 else ll2 
		output += m.rjust(lo, ' ')+'\n'
		output += (opr+n).rjust(lo, ' ')+'\n'
		output += (ll1*'-').rjust(lo, ' ')+'\n'
		if(ln > 1):
			for z in range(len(tmpop)):
				if(tmpop[z].strip('0') == ''):
					output += '0'.rjust(lo-z, ' ')+'\n'
				else:
					output += tmpop[z].rjust(lo-z, ' ')+'\n'
				z += 1
			output += (ll2*'-').rjust(lo, ' ')+'\n'
		output += result.rjust(lo, ' ')+'\n'
	#~ return output
	print output

def main():
	for t in range(int(sys.stdin.readline().strip())):
		exp = match('(\d+)(.{1})(\d+)', sys.stdin.readline().strip())
		printCalculation(exp.group(1), exp.group(2), exp.group(3))
	#~ inputfile = open('arith.in','r')
	#~ outputfile = open('arith.out','w')
	#~ inputfile.readline()
	#~ for line in inputfile:
		#~ exp = match('(\d+)(.{1})(\d+)', line.strip())
		#~ output = printCalculation(exp.group(1), exp.group(2), exp.group(3))
		#~ print output
		#~ outputfile.write(output+"\n")
		#~ break
	return 0

if __name__ == '__main__':
	main()

