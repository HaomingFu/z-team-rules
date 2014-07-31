def jump(A):
    if len(A) <= 1:
        return 0
    jumps = [-1]*(len(A)-1)
    jumps.append(0)
    lastPosition = len(A)-1
    for i in range(len(A)-2, -1, -1):
        if A[i] + i >= lastPosition:
            jumps[i] = min([1+jumps[j] for j in range(i+1, A[i]+i+1) if jumps[j] >= 0])
            lastPosition = i
    return jumps[0]

print(jump([1,2]))
