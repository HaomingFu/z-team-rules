def combinationSum2(candidates, target):
    result = []
    solution = []
    candidates.sort()
    addCombinationSum(candidates, target, 0, result, solution)
    return result

def addCombinationSum(candidates, target, depth, result, solution):

    if target == 0:
        result.append(solution[::])
        return
    if target <0 or depth >= len(candidates):
        return
    for i in range(depth, len(candidates)):
        if i > depth and candidates[i] == candidates[i-1]:
            continue
        solution.append(candidates[i])
        addCombinationSum(candidates, target-candidates[i], i+1, result, solution)
        solution.pop()

print(combinationSum2([22,21,18,18,23,14,26,14,34,8,33,29,32,14,6,32,34,22,25,14,25,31,9,7,20,31,34,32,18,34,8,27,13,21,10,31,22,24,10,13,27,8,7,16,10,30,5,9,17,26,11,8,22,7], 25))
