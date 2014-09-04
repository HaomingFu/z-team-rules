def candy(ratings):
    print(ratings)
    num_of_children = len(ratings)
    candies_left = [1]*num_of_children
    candies_right = [1]*num_of_children
    for i in range(1, num_of_children):
        if ratings[i] > ratings[i-1]:
            candies_left[i] = candies_left[i-1] + 1
    for i in range(num_of_children-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies_right[i] = candies_right[i+1] + 1
    print(candies_left)
    print(candies_right)
    return sum([max(candies_left[i], candies_right[i]) for i in range(num_of_children)])

print(candy([2,2,1]))
