#!/usr/bin/env python
# encoding: utf-8

class Solution:

    def fractionToDecimal(self, numerator, denominator):
        res = ''
        sign = numerator*denominator
        numerator = abs(numerator)
        denominator = abs(denominator)
        remainder = numerator % denominator
        res += str(numerator // denominator)
        if remainder == 0:
            return res if sign > 0 else '-'+ res
        res += '.' + self.getFraction(remainder, denominator)
        return res if sign > 0 else '-' + res

    def getFraction(self, remainder, denominator):
        remains = {remainder:0}
        res = ''
        index = 0
        temp = 1
        while remainder:
            temp = 0.1
            index += 1
            newRemainder = int(remainder / float(temp)) % denominator
            res += str(int(remainder / float(temp) // denominator))
            if newRemainder in remains.keys():
                startIx = remains[newRemainder]
                return res[0:startIx] + '(' + res[startIx:] + ')'
            else:
                remains[newRemainder] = index
            remainder = newRemainder
        return res


s = Solution()

print(s.fractionToDecimal(-50,8))
