import itertools
def permuteUnique(num):
    sortedPer = sorted([list(i) for i in itertools.permutations(num)])
    i = 0
    while i < len(sortedPer):
        j = i+1
        while j < len(sortedPer) and sortedPer[j] == sortedPer[i]:
            sortedPer[j] = -100
            j += 1
        i = j
    return [i for i in sortedPer if i != -100]

print(permuteUnique([3,3,0,0,2,3,2]))
