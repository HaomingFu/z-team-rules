#convert an integer to roman
#From: http://oj.leetcode.com/problems/integer-to-roman/
#Accepted

class Solution:
    def intToRoman(self, num):
        #roman_dict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D', 1000:'M'}
        def thousand(thsd):
            return 'M'*(thsd//1000) if thsd else ''
        def hundred(hdrd):
            res = ''
            if hdrd <= 300:
                res = 'C'*(hdrd//100)
            elif hdrd== 400:
                res = 'CD'
            elif hdrd <=800:
                res = 'D' + 'C'*((hdrd-500)//100)
            else:
                res = 'CM'
            return res
        def tens(tn):
            res = ''
            if tn <= 30:
                res = 'X'*(tn//10)
            elif tn == 40:
                res = 'XL'
            elif tn <= 80:
                res = 'L' + 'X'*((tn -50 ) //10)
            else:
                res = 'XC'
            return res
        def digit(dgt):
            if dgt <=3:
                res = 'I'*dgt
            elif dgt == 4:
                res = 'IV'
            elif dgt <=8:
                res = 'V' + 'I'*(dgt-5)
            else:
                res = 'IX'
            return res
        thsd = num // 1000
        hdrd = (num%1000)//100
        tn = (num%100)//10
        dgt = num%10
        return thousand(thsd*1000) + hundred(hdrd*100) + tens(tn*10) + digit(dgt)
if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(1))

