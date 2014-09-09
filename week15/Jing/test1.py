def findSubstring(S, L):
    if not S or not L:
        return []
    res = []
    SL = len(S)
    itemN, itemL = len(L), len(L[0])
    dic = {k:0 for k in L}
    for k in L:
        dic[k] += 1
    i = 0
    while i+itemN*itemL <= SL:
        newDic = {}
        j = 0
        item = S[i+j*itemL:i+(j+1)*itemL]
        while j < itemN:
            if item not in dic:
                break
            if item not in newDic:
                newDic[item] = 1
            else:
                newDic[item] += 1
            if newDic[item] > dic[item]:
                break
            j += 1
            item = S[i+j*itemL:i+(j+1)*itemL]
        if j == itemN:
            res.append(i)
        i += 1
    return res

print(findSubstring("a", ["a"]))
