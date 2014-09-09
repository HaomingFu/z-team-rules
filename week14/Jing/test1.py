def nextPermutation(num):
    if not num:
        return num
    minDict = {}
    maxN, minN = -1, 11
    found = False
    for j in range(len(num)-1, -1, -1):
        if num[j] not in minDict:
            minDict[num[j]] = j
            if num[j] > maxN:
                maxN = num[j]
            elif num[j] < minN:
                minN = num[j]
        if num[j] < maxN:
            found = True
            break
    if found:
        print("hahahah")
        for i in range(num[j]+1, maxN+1):
            if i in minDict:
                print("eheheheh")
                print(j , minDict[i], i, num[j])
                num[j], num[minDict[i]] = i, num[j]
                return num
    num.reverse()
    return num

print(nextPermutation([1,5,1]))
