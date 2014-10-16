#!/usr/bin/env python
# encoding: utf-8

def subsetsWithDup(S):
    S.sort()
    res=[[]]
    pre, count = None,0
    for e in S:
        if e != pre:
            pre,count = e, len(res)
        res = res + [l+[e] for l in res[len(res) - count]
    return res


S = [4,2,1]
print(subsetsWithDup(S))
