#!/usr/bin/env python
# encoding: utf-8

def isNumber(s):
    s = s.strip()

    if not s:
        return False
    if (s[0]=='+' or s[0]=='-') and len(s) > 1:
        s = s[1:]
    try:
        ix=s.index('e')
        if ix < len(s) -1:
            return judgeNumber(s[0:ix]) and judgeNumber(s[ix+1:])
        else:
            return False
    except:
        return judgeNumber(s)


def judgeNumber(s):
    if not s:
        return False
    ndot = 0
    for each in s:
        if each.isdigit():
            continue
        elif each == '.':
            ndot += 1
            if ndot>1:
                return False
        else:
            return False
    if ndot:
        ix = s.index('.')
        if ix==0:
            return s[1:].isdigit()
        elif not (ix<len(s)-1 and s[ix+1:].isdigit() and s[0:ix].isdigit()):
            return False
    return True




if __name__ == "__main__":
    s = ".e9"
    print(isNumber(s))

