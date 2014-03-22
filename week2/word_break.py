"""Jing 3/20 2014
http://oj.leetcode.com/problems/word-break/
"""
"""
works but TLE...
def wordBreak(s, dict):
    if not dict:
        return False
    dict = [word for word in dict if word in s]
    for word in dict:
        if s == word:
            return True
        if s.startswith(word):
            wordBreak(s[len(word):], dict)
    return False
"""
def wordBreak(self, s, dict):
    """better solution with DP"""
    if not dict:
        return False
    if s in dict:
        return True
    length = len(s)
    dp = [False]*(length+1)
    dp[0] = True
    for i in range(length):
        for j in range(i, length+1):
            if s[i:j] in dict and dp[i]:
                dp[j] = True
    return dp[length]

s = "leetcode"
dict = ["leet", "code"]
print(len(dict))
print(len(set(dict)))
print(wordBreak(s, dict))

#s = "bccdbacdbdacddabbaaaadababadad"
#dict = ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]
