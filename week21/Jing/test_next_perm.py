def nextPermutation(num):
    if not num:
        return num
    for j in range(len(num)-1, -1, -1):
        if j-1>=0 and num[j-1]<num[j]:
            break
    if j == 0:
        num.reverse()
        return num
    j -= 1
    for m in range(len(num)-1, j, -1):
        if num[m] > num[j]:
            num[m], num[j] = num[j], num[m]
            break
    num = num[:j+1] + list(reversed(num[j+1:]))
    return num

def test():
    print(nextPermutation([1,2,3]))
    print(nextPermutation([3,2,1]))
    print(nextPermutation([1,1,5]))
    print(nextPermutation([1,3,2]))

test()

