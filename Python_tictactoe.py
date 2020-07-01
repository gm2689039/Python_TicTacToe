# write your code here
# write your code here
#input_str = input()
c_match = 0
c_space = 0
result  = None
playturn = True
player = 1
move = 0
#list_str = list(input_str)
list_str = []
for i in range(9):
    list_str.append(' ')
print('---------')
print('|',list_str[0],list_str[1],list_str[2],'|')
print('|',list_str[3],list_str[4],list_str[5],'|')
print('|',list_str[6],list_str[7],list_str[8],'|')
print('---------')
XCoord, YCoord = input().split()

while playturn:
    while True:

        if not XCoord.isnumeric() or not YCoord.isnumeric():
            print('You should enter numbers!')
            XCoord, YCoord = input().split()
            continue

        #print(XCoord,YCoord)
        if int(XCoord) < 0 or  int(XCoord) > 3 or int(YCoord) < 0 or  int(YCoord) > 3:
            print('Coordinates should be from 1 to 3!')
            XCoord, YCoord = input().split()
            continue

        coord = (int(XCoord) - 1)  + (9 - (3 * int(YCoord)))
        if list_str[coord] == 'X' or list_str[coord] == 'O':
            print('This cell is occupied! Choose another one!')
            XCoord, YCoord = input().split()
        else:
            break

    if player == 1:
        list_str[coord] = 'X'
        player = 2
    else:
        list_str[coord] = 'O'
        player = 1

    print('---------')
    print('|',list_str[0],list_str[1],list_str[2],'|')
    print('|',list_str[3],list_str[4],list_str[5],'|')
    print('|',list_str[6],list_str[7],list_str[8],'|')
    print('---------')

    if list_str[0] == list_str [1] and list_str[1] == list_str[2] and list_str[0] != ' ' and list_str[1] != ' ' and list_str[2] != ' ':
        result = list_str[0]
        c_match += 1
    if list_str[3] == list_str [4] and list_str[4] == list_str[5] and list_str[3] != ' ' and list_str[4] != ' ' and list_str[5] != ' ':
        result = list_str[3]
        c_match += 1
    if list_str[6] == list_str [7] and list_str[7] == list_str[8] and list_str[6] != ' ' and list_str[7] != ' ' and list_str[8] != ' ':
        result = list_str[6]
        c_match += 1
    if list_str[0] == list_str [3] and list_str[3] == list_str[6] and list_str[0] != ' ' and list_str[3] != ' ' and list_str[6] != ' ':
        result = list_str[0]
        c_match += 1
    if list_str[1] == list_str [4] and list_str[4] == list_str[7] and list_str[1] != ' ' and list_str[4] != ' ' and list_str[7] != ' ':
        result = list_str[1]
        c_match += 1
    if list_str[2] == list_str [5] and list_str[5] == list_str[8] and list_str[2] != ' ' and list_str[5] != ' ' and list_str[8] != ' ':
        result = list_str[2]
        c_match += 1
    if list_str[0] == list_str [4] and list_str[4] == list_str[8] and list_str[0] != ' ' and list_str[4] != ' ' and list_str[8] != ' ':
        result = list_str[0]
        c_match += 1
    if list_str[6] == list_str [4] and list_str[4] == list_str[2] and list_str[6] != ' ' and list_str[4] != ' ' and list_str[2] != ' ':
        result = list_str[6]
        c_match += 1

    move += 1
    if c_match == 1:
        result += ' wins'
        playturn = False
    elif c_match > 1:
        result = 'Impossible'
        playturn = False
    elif c_match == 0 and move == 9:
        numX = 0
        numY = 0

        for i in list_str:
            if i == 'X':
                numX += 1
            if i == 'O':
                numY += 1
            if i == '_' or i == ' ':
               c_space += 1

        diffXY = abs(numX - numY)
        print(diffXY)
        print(c_space)
        if diffXY == 1 and c_space == 0:
            result = 'Draw'
        if diffXY <= 0:
            result = 'Game not finished'
        if diffXY > 1 :
        #    print('play')
            result = 'Impossible'
        playturn = False


print(result)
#print('X O X')
#print('O X O')
#print('X X O')
