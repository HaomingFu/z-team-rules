# From: https://oj.leetcode.com/problems/word-break/
# Date: May 23, 2014
# Status: Accepted

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        slen = len(s)
        tab = [False] * (slen+1)
        tab[-1] = True
        for i in range(len(s)-1, -1, -1):
            j = i + 1
            while j <= slen:
                if s[i:j] in dict and tab[j]:
                    tab[i] = True
                    break
                j += 1

        return tab[0]

if __name__ == "__main__":
    s = "a"
    d = ["a", "b"]
    solution = Solution()
    print(solution.wordBreak(s, d))
