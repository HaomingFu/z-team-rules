def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    if not s1:
        return s2 == s3
    if not s2:
        return s1 == s3
    if s3[0] != s1[0] and s3[0] != s2[0]:
        return False
    if s3[0] != s1[0] and s3[0] == s2[0]:
        return isInterleave(s1, s2[1:], s3[1:])
    if s3[0] == s1[0] and s3[0] != s2[0]:
        return isInterleave(s1[1:], s2, s3[1:])
    if s3[0] == s1[0] and s3[0] == s2[0]:
        print(s1)
        print(s2)
        print(s3)
        return isInterleave(s1, s2[1:], s3[1:]) or isInterleave(s1[1:], s2, s3[1:])

print(isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))
