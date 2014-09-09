test_cases, case = int(input()), 1

for test in range(test_cases):
    print("Case #",end="")
    print(case, end="")
    print(":")
    row, col, num_mines = map(int, input().split())
    # all mines
    if row*col == num_mines+1:
        for i in range(row-1):
            print("*"*col)
        print("*"*(col-1)+"c")
        case += 1
        continue
    #no mines
    if num_mines == 0:
        for i in range(row-1):
            print("."*col)
        print("."*(col-1)+"c")
        case += 1
        continue
    if row == 1:
        if col > num_mines + 1:
            print("*"*num_mines+(col-num_mines-1)*"."+"c")
        else:
            print("Impossible")
    elif col == 1:
        if row > num_mines + 1:
            for j in range(num_mines):
                print("*")
            for k in range(row-num_mines-1):
                print(".")
            print("c")
        else:
            print("Impossible")
    elif col == 2:
        if num_mines%2 == 0 and row*col-num_mines >=4:
            for i in range(num_mines//2):
                print("**")
            for j in range(row-num_mines//2-1):
                print("..")
            print(".c")
        else:
            print("Impossible")
    elif row == 2:
        if num_mines%2 == 0 and row*col-num_mines >=4:
            print("*"*(num_mines//2)+"."*(col-num_mines//2))
            print("*"*(num_mines//2)+"."*(col-num_mines//2-1)+"c")
        else:
            print("Impossible")
    elif row >= 3 and col >=3:
        if num_mines <= col*(row-3):
            mine_row = num_mines//col
            mine_left = num_mines%col
            for i in range(mine_row):
                print("*"*col)
            if mine_left == col - 1:
                print("*"*(mine_left-1)+"."*(col-mine_left+1))
                print("*"+"."*(col-1))
                for i in range(row-mine_row-1-1-1):
                    print("."*col)
            else:
                print("*"*mine_left+"."*(col-mine_left))
                for i in range(row-mine_row-1-1):
                    print("."*col)
            print("."*(col-1)+"c")
        else:
            if col*row-num_mines >=9 and (num_mines-col*(row-3))%3 == 0:
                for i in range(row-3):
                    print("*"*col)
                c = (num_mines-col*(row-3))//3
                print("*"*c+"."*(col-c))
                print("*"*c+"."*(col-c))
                print("*"*c+"."*(col-c-1)+"c")
            elif col*row-num_mines >=4 and (num_mines-(row-3)*col) <= col-2:
                for i in range(row-3):
                    print("*"*col)
                print("*"*(num_mines-(row-3)*col)+"."*(col-num_mines+(row-3)*col))
                print("."*col)
                print("."*(col-1)+"c")
            elif col*row-num_mines >=4 and (col*row-num_mines)%2 == 0:
                for i in range(row-3):
                    print("*"*col)
                if num_mines-(row-3)*col <= col:
                    print("*"*(num_mines-(row-3)*col)+"."*(col-(num_mines-(row-3)*col)))
                    print("."*col)
                    print("."*(col-1)+"c")
                else:
                    print("*"*col)
                    r = (num_mines-(row-2)*col)//2
                    print("*"*r+"."*(col-r))
                    print("*"*r+"."*(col-1-r)+"c")
            else:
                print("Impossible")
    case += 1
