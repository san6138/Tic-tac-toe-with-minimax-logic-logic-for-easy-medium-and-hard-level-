
import random
list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
indexlist = [None, (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
modes =('easy', 'user', 'medium', 'hard')
realplayer = ""
anotherplayer = ""

class Board:
    pass

def printlist(list):
    print(' ---------')
    for i in list:
        strjoin = " ".join(i)
        for i in strjoin:
            if i.isdigit(): strjoin = strjoin.replace(i, " ")
        print('| ' + strjoin + ' |')

    print('---------')

def getemptyindex(list):
    return [i for x in list for i in x if i.isdigit()]

def mapn(x, a=indexlist):
    return a[int(x)]

def minmax(list, player):
    emptyindices = getemptyindex(list)
    if winloselogichardlevel(list, realplayer):
        return 10
    elif winloselogichardlevel(list, anotherplayer):
        return -10
    elif len(emptyindices) == 0:
        return 0
    moves = []
    nemptyindices = map(mapn, emptyindices)
    for i in nemptyindices:
        move = Board()
        move.index = list[i[0]][i[1]]
        if player == realplayer:
            list[i[0]][i[1]] = realplayer
            score= minmax(list, anotherplayer)
            if type(score) == Board:
                move.score = score.score
            else:
                move.score = score
        else:
            list[i[0]][i[1]] = anotherplayer
            score = minmax(list, realplayer)
            if type(score) == Board:
                move.score = score.score
            else:
                move.score = score

        list[i[0]][i[1]] = move.index
        moves.append(move)

    moves.sort(key=lambda x:x.score)

    if player == realplayer:
        return moves[-1]
    else:
        return moves[0]

def mediumlogic(letter, *args):
    print('a')
    for i in range(3):
        if list[i][0] == list[i][1] == letter and list[i][2] not in ('X', 'O'):
            list[i][2] =  letter if args == () else args[0]
            printlist(list)
            return
        elif list[i][1] == list[i][2] == letter and list[i][0] not in ("X", 'O'):
            list[i][0] =  letter if args == () else args[0]
            printlist(list)
            return
    for i in range(3):
        if list[0][i] == list[1][i] == letter and list[2][i] not  in ("X", 'O'):
            list[2][i] = letter if args == () else args[0]
            printlist(list)
            return
        elif list[1][i] == list[2][i] == letter and list[0][i] not in ("X", 'O'):
            list[0][i] = letter if args == () else args[0]
            printlist(list)
            return
    if list[0][0] == list[1][1] == letter and list[2][2] not in ("X", 'O'):
        list[2][2] = (letter if args == () else args[0])
        printlist(list)
        return
    elif list[1][1] == list[2][2] == letter and list[0][0] not in ("X", 'O'):
        list[0][0] = letter if args == () else args[0]
        printlist(list)
        return
    elif list[0][2] == list[1][1] == letter and list[2][0] not in ("X", 'O'):
        list[2][0] = letter if args == () else args[0]
        printlist(list)
        return
    elif list[1][1] == list[2][0] == letter and list[0][2] not in ("X", 'O'):
        list[0][2] = letter if args == () else args[0]
        printlist(list)
        return
    elif args == ():
        while True:
            num1 = random.randint(0, 2)
            num2 = random.randint(0, 2)
            if list[num1][num2] in ('X', 'O'): continue
            list[num1][num2] = letter if args == () else args[0]
            printlist(list)
            break
    else:
        return 'None Appended'

def winloselogichardlevel(list, player):
    for i in range(3):
        if list[i][0] == list[i][1] == list[i][2] == player and list[i][2] in ("X", 'O'):
            #print(f'{list[i][0]} wins')
            return True
        elif list[0][i] == list[1][i] == list[2][i] == player and list[2][i] in ("X", 'O'):
            #print(f'{list[0][i]} wins')
            return True

    if list[0][0] == list[1][1] == list[2][2] == player or list[0][2] == list[1][1] == list[2][0] == player and list[1][1]  in ("X", 'O'):
            #print(f'{list[1][1]} wins')
        return True
    else:
        return False

def winloselogic():
    for i in range(3):
        if list[i][0] == list[i][1] == list[i][2] and list[i][2] in ("X", 'O'):
            print(f'{list[i][0]} wins')
            return
        elif list[0][i] == list[1][i] == list[2][i] and list[2][i]  in ("X", 'O'):
            print(f'{list[0][i]} wins')
            return

        elif list[0][0] == list[1][1] == list[2][2] or list[0][2] == list[1][1] == list[2][0] and list[1][1]  in ("X", 'O'):
            print(f'{list[1][1]} wins')
            return
    if all([False if i.isdigit() else True for x in list for i in x ]) == False:
            # print('Game not finished')
        return 'Game not finished'
    else:   # return 'draw'
        print('Draw')

def hardlevel():
    global list, realplayer, anotherplayer
    countx = sum(i.count('X') for i in list)
    counto = sum(i.count('O') for i in list)
    print(countx, counto)
    if countx == counto:
       realplayer = 'X'
       anotherplayer = 'O'
    else:
        realplayer = 'O'
        anotherplayer = 'X'

    index = minmax(list, realplayer).index
    tupleindex = indexlist[int(index)]
    list[tupleindex[0]][tupleindex[1]] = realplayer
    printlist(list)

def mediumlevel():
    countx = sum(i.count('X') for i in list)
    counto = sum(i.count('O') for i in list)
    if countx == counto:
        if mediumlogic('O', 'X') == 'None Appended':
            mediumlogic('X')
    else :
        if mediumlogic('X', 'O') == 'None Appended':
            mediumlogic('O')

def easylevel():
    while True:
        num1 = random.randint(0,2)
        num2 = random.randint(0,2)
        if list[num1][num2] in ("X", 'O'):
            continue
        print('Making move level "easy"')
        countx = sum(i.count('X') for i in list)
        counto = sum(i.count('O') for i in list)
        if countx == counto:
            list[num1][num2] = 'X'
        else:
            list[num1][num2] = 'O'
            # list[num1][num2] = 'O'
        printlist(list)
        break

def useroper():
    global list
    while True:
        ordinate = input('Enter the coordinates:')
        lord = ordinate.split()
        if any([i.isalpha() for i in lord]) == True:
            print("You should enter numbers!")
            continue
        # lord = [int(i) for i in lord]
        elif all([0 < int(i) < 4 for i in lord]) == False:
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            lord = [int(i) - 1 for i in lord]
            countx = sum(i.count('X') for i in list)
            counto = sum(i.count('O') for i in list)

            if list[lord[0]][lord[1]] in ("X", 'O'):
                print("This cell is occupied! Choose another one!")
                # printlist(list)
                continue
            elif countx == counto:
                list[lord[0]][lord[1]] = 'X'
            else:
                list[lord[0]][lord[1]] = 'O'
            printlist(list)
            # print('a')
            break

while True:
    method = input('Input command:')
    if method == 'exit': break
    elif len(method.split()) != 3 or method.split()[0] != 'start' or method.split()[1] not in modes or method.split()[2] not in modes:
        print('Bad parameters!')
        continue
    else:
        printlist(list)
        operdic ={'user': 'useroper()', 'easy': 'easylevel()', 'medium': 'mediumlevel()', 'hard': 'hardlevel()' }
        operations = method.split()
        while True:
            eval(operdic[operations[1]])
            if winloselogic() != 'Game not finished': break
            eval(operdic[operations[2]])
            if winloselogic() != 'Game not finished': break
    break
