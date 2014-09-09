def partition(s):
    if not s:
        return []
    result = []
    tmp = []
    partitionPan(s, 0, tmp, result)
    return result

def partitionPan(s, start, tmp, result):
    if start == len(s):
        print(tmp)
        result.append(tmp[::])
        return
    i = start+1
    while i <= len(s):
        if isPalin(s, start, i-1):
            print(s[start:i])
            tmp.append(s[start:i])
            partitionPan(s, i, tmp, result)
            tmp.pop()
        i += 1

def isPalin(s, start, end):
    while start < end:
        print(start, end)
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

print(partition("a"))
