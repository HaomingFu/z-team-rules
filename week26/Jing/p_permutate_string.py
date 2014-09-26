import itertools
def permutate(a):
    res = []
    def perm(a, start, end):
        if start == end:
            res.append("".join(a[:]))
        else:
            for j in range(start, end+1):
                a[start], a[j] = a[j], a[start]
                perm(a, start+1, end)
                a[start], a[j] = a[j], a[start]
    a = list(a)
    perm(a, 0, len(a)-1)
    print(res)
    return res


print(permutate("ABC"))

print("itertools.permutations:", list(itertools.permutations("ABC")))
