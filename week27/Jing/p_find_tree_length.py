
def fillDepth(array, depth_list, n):
    if depth_list[n]:
        return
    elif array[n] == -1:
        depth_list[n] = 1
        return
    if depth_list[array[n]] == 0:
        fillDepth(array, depth_list, array[n])
    depth_list[n] = depth_list[array[n]] + 1

def findHight(array):
    depth = [0]*len(array)
    for i in range(len(array)):
        fillDepth(array, depth, i)
    return max(depth)

def test():
    print(findHight([1, 5, 5, 2, 2, -1, 3]))
    print(findHight([-1, 0, 0, 1, 1, 3, 5]))

test()
