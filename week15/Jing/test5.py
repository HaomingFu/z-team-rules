def trap(A):
    res = []
    if len(A) <= 2:
        return 0
    for i in range(len(A)):
        print(res)
        if i == 0 and A[i] > A[i+1]:
            res.append(i)
        elif i == len(A)-1:
            if A[i] > A[i-1]:
                while len(res) >= 2 and A[i] > A[res[-1]] and A[res[-1]] <= A[res[-2]]:
                    res.pop()
                res.append(i)
        elif A[i] >= A[i-1] and A[i] >= A[i+1]:
            while len(res) >=2 and A[i] >= A[res[-1]] and A[res[-1]] <= A[res[-2]]:
                res.pop()
            res.append(i)
    print(res)
    if len(res) < 2:
        return 0
    num = 0
    for i in range(len(res)-1):
        for j in A[res[i]+1:res[i+1]]:
            num += max(0, min(A[res[i]],A[res[i+1]])-j)
    return num

print(trap([8,8,1,5,6,2,5,3,3,9]))
