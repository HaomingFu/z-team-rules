def numDistinct(S, T):
    if S == T or not T:
        return 1
    if len(T) > len(S):
        return 0
    if S[0] == T[0]:
        return numDistinct(S[1:], T[1:]) + numDistinct(S[1:], T)
    else:
        return numDistinct(S[1:], T)

print(numDistinct("rabbbit", "rabbit"))
