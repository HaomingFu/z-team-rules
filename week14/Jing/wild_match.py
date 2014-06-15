def isMatch(s, p):
    print(s, p)
    if s == '' and p == '':
            return True
    if p == '' and s != '':
        return False
    if p[0] == '*' and p != '*' and s == '':
        return False
    if p[0] == '?' or p[0] == s[0]:
        return isMatch(s[1:], p[1:])
    if p[0] == '*':
        return isMatch(s[1:], p) or isMatch(s, p[1:])

print(isMatch("aa", "*"))
