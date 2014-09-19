def fourSum(num, target):
    num.sort()
    lookupDict = {}
    res = []
    setRes = set([])
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i]+num[j] not in lookupDict:
                lookupDict[num[i]+num[j]] = set([frozenset((i, j))])
            else:
                lookupDict[num[i]+num[j]].add(frozenset((i, j)))
    for k in lookupDict:
        if -k in lookupDict:
            for pair1 in lookupDict[k]:
                for pair2 in lookupDict[-k]:
                    if not pair1.intersection(pair2):
                        setRes.add(pair1.union(pair2))
    return map(list, setRes)
    for item in setRes:
        res.append([num[i] for i in item])
    return res


print(fourSum([1, 0, -1, 0, -2, 2], 0))
