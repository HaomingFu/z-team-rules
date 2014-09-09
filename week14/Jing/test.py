def longestPalindrome(s):
    if not s:
        return s
    maxL = 1
    left, right = 0, 0
    for i in range(len(s)):
        l = 1
        for j in range(1, i+1):
            if i+j < len(s) and s[i-j] == s[i+j]:
                l += 2
                if i-j == 0:
                    if l > maxL:
                        maxL = l
                        left, right = i-j, i+j+1
            else:
                if l > maxL:
                    maxL = l
                    left, right = i-j+1, i+j-1
                break
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            l = 2
            for j in range(1, i+1):
                if i+j+1 < len(s) and s[i-j] == s[i+j+1]:
                    l += 2
                    if i-j == 0:
                        if l > maxL:
                            maxL = l
                            left, right = i-j, i+j+2
                else:
                    if l > maxL:
                        maxL = l
                        left, right = i-j+1, i+j
                    break
    return s[left:right+1]

print(longestPalindrome("abbbba"))
print(longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccc"))
print(longestPalindrome("abcdcnnolajt;ajrwrwrnwrrjnejrwjebrrnwjk wj"))
