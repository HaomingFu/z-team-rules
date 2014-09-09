def canJump(A):
    maxJump, length = A[0], len(A)
    i = 0
    while(i < maxJump + 1):
        print(maxJump)
        if maxJump >= length - 1:
            break
        if i + A[i] > maxJump:
            maxJump = i + A[i]
        i += 1
    return maxJump >= length - 1

def test():
    print(canJump([1, 1, 1, 0]))
    print(canJump([0]))

test()
