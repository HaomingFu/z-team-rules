"""
Jing 3/20, 2014
http://oj.leetcode.com/problems/evaluate-reverse-polish-notation/
Note in the OJ collections is imported so just use q = collections.deque() is fine :)
"""
from collections import deque
q = deque()
tokens = ["4", "13", "5", "/", "+"]
for val in tokens:
    if val not in ['+', '-', '*', '/']:
        q.append(val)
    else:
        op1 = int(q.pop())
        op2 = int(q.pop())
        if val == '-':
            result = op2 - op1
        elif val == '+':
            result = op2 + op1
        elif val == '*':
            result = op1*op2
        elif val == '/':
            result = int(op2/float(op1))
        q.append(result)
print(q.pop())
