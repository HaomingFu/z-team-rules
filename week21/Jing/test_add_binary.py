def addBinary(a, b):
    reversedA = a[::-1]
    reversedB = b[::-1]
    c = ""
    carry = 0
    while reversedA or reversedB:
        if reversedA:
            carry += int(reversedA[0])
            reversedA = reversedA[1:]
        if reversedB:
            carry += int(reversedB[0])
            reversedB = reversedB[1:]
        c += str(carry%2)
        carry = carry//2
    if carry:
        c += "1"
    return c[::-1]

def test():
    print(addBinary("11", "1"))

test()
