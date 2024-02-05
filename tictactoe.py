BOARD = []
def line(first, last):
    line = []
    for a in range(first, last):
        line.append(a)
    return line


def board(n):
    first = 0
    last = n
    for a in range(0, n):
        numbers = line(first, last)
        BOARD.append(numbers)
        first += n
        last += n 
    return BOARD

def printBoard(n):
    for a in board(n):
        for b in a[:-1]:
            if b < 10:
                print('', b, end= ' ')
            else:
                print(b, end= ' ')
        if a[-1] < 10:
            print('', a[-1])
        else:
            print(a[-1])

def printBoard2():
    for a in BOARD:
        for b in a[:-1]:
            if b == 'X' or b == 'O':
                print('', b, end=' ')
            elif b < 10:
                print('', b, end=' ')
            else:
                print(b, end=' ')
        if a[-1] == 'X' or a[-1] == 'O':
            print('', a[-1])
        elif a[-1] < 10:
            print('', a[-1])
        else:
            print(a[-1])

def turn(size, XorO):
    XO = int(input(f'{XorO}--> '))
    for list in BOARD:
        for b in range(size):
            if XO == list[b]:
                list[b] = XorO

def status(n, XorO):
    for a in range(n): 
        count = 0
        for b in range(n):
            if BOARD[a][b] == XorO: #horizontal check
                count += 1
                if count == n:
                    return True
    for a in range(n):
        count = 0
        for b in range(n):
            if BOARD[b][a] == XorO: #vertical check
                count += 1
                if count == n:
                    return True
    count = 0
    for a in range(n):
        for b in range(n):
            if a == b:
                if BOARD[a][b] == XorO:
                    count += 1
                    if count == n:
                        return True
    count = 0
    for a in range(n):
        for b in range(n):
            if ((a+b) == n-1):
                if BOARD[a][b] == XorO:
                    count += 1
                    if count == n:
                        return True

def full(n):
    for a in range(n):
        for b in range(n):
            if str(BOARD[a][b]).isdecimal():
                return False #not full
    return True

size = int(input('Size--> '))
printBoard(size)
XorO = 'X'
while(True):
    turn(size, XorO)
    printBoard2()
    if (status(size, XorO)):
        print(f'Winner: {XorO}')
        break
    if (full(size)):
        print('Winner: None')
        break
    if XorO == 'X':
        XorO = 'O'
    else:
        XorO = 'X'