def maxSubArray(A):
    if not A:
        return 0
    return maxSub(A, 0, len(A)-1)
def maxSub(array, low, high):
    if low == high:
        return array[low]
    mid = (low + high)/2
    return max(maxSub(array, low, mid), maxSub(array, mid+1, high), maxCross(array, low, mid, high))
def maxCross(array, low, mid, high):
    sum_left = sum_right = 0
    max_left = max_right = -1000000
    # mid will be on the low side if two numbers are equal
    for i in range(mid, low-1, -1):
        sum_left = sum_left + array[i]
        if sum_left > max_left:
            max_left = sum_left
    for j in range(mid+1, high+1):
        sum_right = sum_left + array[j]
        if sum_right > max_right:
            max_right = sum_right
    return max_left + max_right

print(maxSubArray([1]))
