def combinationSum(candidates, target):
        result = []
        solution = []
        total = 0
        candidates.sort()
        addCombinationSum(candidates, target, 0, total, result, solution)
        return result

def addCombinationSum(candidates, target, depth, total, result, solution):
    if total > target:
        return
    if total == target:
        result.append(solution[:])
        return
    for i in range(depth, len(candidates)):
        total += candidates[i]
        solution.append(candidates[i])
        addCombinationSum(candidates, target, i, total, result, solution)
        solution.pop()
        total -= candidates[i]

print(combinationSum([1,1,1,1,1,1],2))
