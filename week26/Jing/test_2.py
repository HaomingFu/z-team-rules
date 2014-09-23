"""
res = []
def fullJustify(words, L):
    if not words:
        return
    length, len_words = 0, len(words)
    i = 0
    while i < len_words and length +i+len(words[i]) <= L:
        length += len(words[i])
        i += 1
    total_spaces = L - length
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
    return res
res = []
def fullJustify(words, L):
    if not words:
        return
    length, len_words = 0, len(words)
    i = 0
    while i < len_words and length +i+len(words[i]) <= L:
        length += len(words[i])
        i += 1
    total_spaces = L - length
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
    return res
"""

def fullJustify(words, L):
    res = []
    recursive(words, L, res)
    return res
def recursive(words, L, res):
    if not words:
        return
    length, len_words = 0, len(words)
    i = 0
    while i < len_words and length +i+len(words[i]) <= L:
        length += len(words[i])
        i += 1
    total_spaces = L - length
    line = ""
    if not words[i:]:
        for j in range(i-1):
            line += words[j]+ " "*1
        line = line+words[i-1] + " "*(L-length-i+1)
        res.append(line)
        return
    if i == 1:
        spaces = L - length
        extra_space = 0
    else:
        spaces = total_spaces/(i-1)
        extra_space = total_spaces%(i-1)
    for j in range(i-1):
        if j < extra_space:
            line += words[j]+" "*(1+spaces)
        else:
            line += words[j]+ " "*spaces
    line += words[i-1] if i != 1 else words[i-1] + " "*spaces
    res.append(line)
    recursive(words[i:], L, res)

#print(fullJustify(["a", "b", "c"], 1))
print(fullJustify(["What","must","be","shall","be."], 12))
#print(fullJustify([""], 0))

