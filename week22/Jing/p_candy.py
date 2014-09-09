"""
From: https://oj.leetcode.com/problems/candy/
Author: Jing Zhou
Date: Aug 27, 2014
Thought: There are several solutions. This one is simple but not intuitive.
Tags: array, number, list
"""



class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        num_of_children = len(ratings)
        candies_left = [1]*num_of_children
        candies_right = [1]*num_of_children
        for i in range(1, num_of_children):
            if ratings[i] > ratings[i-1]:
                candies_left[i] = candies_left[i-1] + 1
        for i in range(num_of_children-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies_right[i] = candies_right[i+1] + 1
        return sum([max(candies_left[i], candies_right[i]) for i in range(num_of_children)])
