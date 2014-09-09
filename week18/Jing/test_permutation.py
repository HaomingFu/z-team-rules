def permuteUnique(num):
    result, solution = [], []
    visited = [0]*len(num)
    generatePerm(num, 0, result, solution, visited)
    return result

def generatePerm(num, step, result, solution, visited):
    if step == len(num):
        result.append(solution[::])
        return
    for i in range(0, len(num)):
        if visited[i] == 0:
            print("mark ", i, "as visited")
            visited[i] = 1
            print("add ", i , "to solution")
            solution.append(num[i])
            print(solution)
            generatePerm(num, step+1, result, solution, visited)
            print("soltion after recursion")
            print(solution)
            print("pop last element")
            solution.pop()
            print("solution after popping last element")
            print(solution)
            visited[i] = 0

print(permuteUnique([1,2,3]))
