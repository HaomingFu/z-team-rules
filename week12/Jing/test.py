def countAndSay(n):
        s = '1'
        for i in range(n):
            newS = ''
            num = 1
            for j in range(len(s)):
                if j == len(s)-1:
                    newS += str(num)+s[-1]
                elif s[j] == s[j+1]:
                    num += 1
                else:
                    newS += str(num) + s[j]
                    num = 1
            s = newS
        return s
for i in range(5):
    print(countAndSay(i))
