def convert(s, nrows):
    if nrows == 1:
        return s
    res = ""
    s_l = len(s)
    for i in range(min(nrows, s_l)):
        res = res + s[i]
        index = i
        if (i == 0 or i == nrows - 1):
            while index + (nrows-1)*2 < s_l:
                res = res + s[index+(nrows-1)*2]
                index += (nrows-1)*2
        else:
            while index + 2*(nrows-i-1) < s_l:
                res = res + s[index + 2*(nrows-i-1)]
                print(s[i + 2*(nrows-i-1)])
                if index + (nrows-1)*2 < s_l:
                    res = res + s[index+(nrows-1)*2]
                    print(s[i+(nrows-1)*2])
                index = index + (nrows-1)*2
    return res

print(convert("A", 2))
