# convert an integer to Roman numerals -- version 3
# other people's answer
# From:http://oj.leetcode.com/discuss/1208/how-to-improve-code

class Solution:
    roman_dict = [
            (1000,'M'), (900,'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    def intToRoman(self, num):
        for kv in self.roman_dict:
            if kv[0] <= num:
                return kv[1] + self.intToRoman(num - kv[0])
        return ''

if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3888))
