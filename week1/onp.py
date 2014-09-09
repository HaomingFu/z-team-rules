"""
Written by Jing Zhou
Used a simple stack
From: http://www.spoj.com/submit/ONP/
"""

import sys
from collections import deque
d = deque()
for line in sys.stdin.readlines():
    for char in line.strip():
        if char.isalpha():
            print(char, end="")
        elif char in ['+', '-', '*', '/', '^']:
            d.append(char)
        elif char == ')':
            print(d.pop(), end='')
    print()
