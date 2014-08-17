def permuatation(s):
    res = []
    if len(s) <= 1:
        return [s]
    for i, val in enumerate(s):
        for perm in permuatation(s[:i]+s[i+1:]):
            print(val , perm)
            res += [val+perm]
    return res

print(permuatation("abcd"))
