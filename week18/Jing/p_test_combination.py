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

print(combinationSum2([1, 2, 2, 2], 7))
