# convert an integer to roman numerals -- version 2
# from: http://oj.leetcode.com/problems/integer-to-roman/
# Accepted
class Solution:
    def intToRoman(self, num):
        romanDict = {1:'I',5:'V',10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        #divisor = [1000,500, 100, 50, 10, 5, 1]
        divider = 1000
        res = ''
        while divider > 0 and num >0:
            q = num // divider
            num = num % divider
            if q ==9:
                res = res + romanDict[divider] + romanDict[10*divider]
            elif q>= 5:
                res = res + romanDict[divider*5] + romanDict[divider]*(q-5)
            elif q==4:
                res = res + romanDict[divider] + romanDict[divider*5]
            else :
                res = res + romanDict[divider]*q
            divider //= 10

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(9))
    print(solution.intToRoman(3999))
    print(solution.intToRoman(3888))
