from collections import Counter
def isScramble(s1, s2):
    if s1 == s2:
        return True
    if len(s1) != len(s2):
        return False
    if Counter(s1) != Counter(s2):
        return False
    for i in range(1, len(s1)):
        print(s1[:i], s2[:i], s1[i:], s2[i:])
        if isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]):
            return True
        if isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[-i:]):
            return True
    return False

print(isScramble("xstjzkfpkggnhjzkpfjoguxvkbuopi", "xbouipkvxugojfpkzjhnggkpfkzjts"))
