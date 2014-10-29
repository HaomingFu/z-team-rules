#!/usr/bin/env python
# encoding: utf-8

def simplifyPath(path):
    li = path.split('/')
    stack = []
    for each in li:
        if each == '..':
            if len(stack) > 0:
                stack.pop()
            else:
                continue
        elif each == '.':
            continue
        elif each:
            stack.append(each)
    res = "/".join(stack)
    return '/' + res


path = '/'
print(simplifyPath(path))
