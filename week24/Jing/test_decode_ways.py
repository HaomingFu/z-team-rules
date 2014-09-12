def numDecodings(s):
    """
    if len(s) <= 1:
        return 1
    for char in s:
        if char=="1" or char=="2" and int(char) <=6:
            return numDecodings(s[1:]) + numDecodings(s[2:])
    return 1
    """
    res = [1]*(len(s)+1)
    for i, char in enumerate(s):
        if i >=1:
            if s[i-1] == "1" or s[i-1] == "2" and int(char) <= 6:
                res[i+1] = res[i] + res[i-1]
            else:
                res[i+1] = res[i]
    return res[len(s)]

print(numDecodings("6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155"))
print(numDecodings("12"))
