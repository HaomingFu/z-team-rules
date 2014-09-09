""" Jing 20/3 2014
this is just an answer to a question on stackoverflow... Go vote me up...
http://stackoverflow.com/questions/22550302/find-neighbors-in-a-matrix-using-python/
"""
a = [[ 11,  21,  31,  41,  51,  61,  71],
   [ 12,  22,  32,  42,  52,  62,  72],
   [ 13,  23,  33,  43,  53,  63,  73],
   [ 14,  24,  34,  44,  54,  64,  74],
   [ 15,  25,  35,  45,  55,  65,  75],
   [ 16,  26,  36,  46,  56,  66,  76],
   [ 17,  27,  37,  47,  57,  67,  77]]
def neighbors(radius, rowNumber, columnNumber):
    return [[a[i][j] if  i>=0 and i<len(a) and j >=0 and j<len(a[0]) else 0 for j in range(columnNumber-1-radius, columnNumber+radius)] for i in range(rowNumber-1-radius, rowNumber+radius)]

"""
def neighbors(radius, rowNumber, columnNumber):
     return [[a[i][j] if  i>=0 and i< len(a) j >=0 and j <len(a[0]) else 0 for j in range(columnNumber-1-radius, columnNumber+radius)] for i in range(rowNumber-1-radius, rowNumber+radius)]
"""
print(neighbors(2, 3, 7))
