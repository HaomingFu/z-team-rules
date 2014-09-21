def wordBreak(s, dict):
    res = []
    def buildPath(path, index):
        if index == 0:
            return
        if index == -1:
            path_copy = path[:]
            path_copy.reverse()
            res.append(" ".join(path_copy))
            return
        else:
            for neighbor in marks[index]:
                path.append(neighbor[1])
                print("path", path)
                buildPath(path, neighbor[0])
                path.pop()

    wordDict = set(dict)
    indicator = [False]*len(s)
    marks = {}
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] in wordDict:
                if i == 0 or indicator[i-1]:
                    indicator[j-1] = True
                    if j-1 not in marks:
                        marks[j-1] = set([(i-1,s[i:j])])
                    else:
                        marks[j-1].add((i-1, s[i:j]))
    if not indicator[-1]:
        return []
    print(indicator)
    print(marks)
    buildPath([], len(s)-1)
    return res

print(wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
