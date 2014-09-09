"""
Problem: http://oj.leetcode.com/problems/rotate-image/
Author: Jing
Date: 11/04/2014
Lessons: This is a easy question but I used a new way(and wrong) to create the
matrix and spent some time trying to figure out what's wrong.
I used [[0]*length]*length... which just create a list of *same* list.
See:http://stackoverflow.com/questions/23018470/incorrect-output-when-trying-to-rotate-a-matrix-in-python
"""

def rotate(matrix):
     length = len(matrix)
     new_matrix = [[0]*length for _ in range(length)]
     for i in range(length):
         for j in range(length):
             new_matrix[j][length-1-i] = matrix[i][j]
             print("new_matrix[",j,"][", length-1-i,"]", "is", new_matrix[j][length-1-i])
     for i in range(length):
         for j in range(length):
             print(new_matrix[i][j])
     return new_matrix
print(rotate([[1 ,2, 3], [4, 5, 6], [7, 8, 9]]))
