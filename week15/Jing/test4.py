def grayCode(n):
    res = [0]
    for i in range(1, n+1):
        newRes = [2**(i-1)+j for j in reversed(res)]
        res.extend(newRes)
    return res

for m in range(4):
    print(grayCode(m))
