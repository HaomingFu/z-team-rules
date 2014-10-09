i = 0
test_cases = input()
while i < test_cases:
    i += 1
    number = raw_input()
    print number
    if len(number) == 1:
        print number
        continue
    odd = True if len(number)%2 == 1 else False
    mid = len(number)/2
    if not odd:
        if number[:mid][::-1] > number[mid:]:
            print number[:mid]+number[:mid][::-1]
        else:
            half = str(int(number[:mid])+1)
            print half+half[::-1]
    else:
        middle = number[mid]
        left = number[:mid]
        right = number[mid+1:]
        if left[::-1] > right:
            print left+middle+left[::-1]
        else:
            if middle != '9':
                print left + str(int(middle)+1) + left[::-1]
            else:
                middle = '0'
                left = str(int(left)+1)
                print left + middle + left[::-1]



