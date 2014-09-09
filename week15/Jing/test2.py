def longestValidParentheses(s):
    if not s:
        return 0
    maxl = i = t = 0
    st = []
    while i < len(s):
        print(i)
        if s[i] == '(':
            st.append(('(', i))
            print(st)
        else:
            print(st)
            if not st:
                t = i+1
            if st:
                print(st)
                tmp = st[-1]
                print(tmp)
                st.pop()
                if tmp[0] == '(':
                    if st:
                        maxl = max(maxl, i-st[-1][1])
                    else:
                        maxl = max(maxl, i-t+1)
        i += 1
    return maxl

print(longestValidParentheses("(()"))
