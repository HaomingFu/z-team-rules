def isMatch(s, p):
    if not s and not p:
        return True
    if not s or not p:
        return False
    if len(p) < 2 or p[1] != "*":
        return (p[0] == s[0] or p[0] == "." and s) and isMatch(s[1:], p[1:])
    while s and (s[0] == p[0] or p[0] == "."):
        if isMatch(s, p[2:]):
            return True
        s = s[1:]
    return isMatch(s, p[2:])

print(isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
