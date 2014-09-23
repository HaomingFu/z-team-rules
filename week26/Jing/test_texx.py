res = []
def fullJustify(words, L):
    print(words)
    if not words:
        return
    length, len_words = 0, len(words)
    i = 0
    while i < len_words and length +i+len(words[i])< L:
        print(words[i])
        length += len(words[i])
        i += 1
    total_spaces = L - length
    print(total_spaces)
    print(i)
    if i == 1:
        spaces = L - length
        extra_space = 0
    else:
        spaces = total_spaces/(i-1)
        extra_space = total_spaces%(i-1)
    line = ""
    for j in range(i-1):
        if j < extra_space:
            line += words[j]+" "*(1+spaces)
        else:
            line += words[j]+ " "*spaces
    line += words[i-1] if i != 1 else words[i-1] + " "*spaces

    res.append(line)
    fullJustify(words[i:], L)
    print(len(res[0]))
    return res

print(fullJustify([""], 16))
