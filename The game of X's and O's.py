#The game of X's and O's

import random

def drawBoard(board):   #выводит игровое поле
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter(): #разрешение игроку ввести букву, возврат списка, где буква игрока первый элемент, ИИ - второй
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Выбери на какой ты стороне, малой...Ну типа крестик или нолик, ну ты понял, да? X или O крч английские')
        letter = input().upper()
        
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst(): #случайный выбор игрока, к-ый сделает первых ход
    if random.randint(0, 1) == 0:
        return'Кибер Монстр'
    else:
        return'Челомедведосвин'

def makeMove(board, letter, move): #разммещение клеток на игровом поле
    board[move] = letter

def isWinner(bo, le): #учитывая заполение игрового поля и буквы игрока, функция возвращает True, если игрок выиграл
    #bo = board, le = letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le)  or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board): #cоздает копию игрового поля и возвращает его
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move): # возвращает True, если сделан ход в свободную клетку
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('Че, малой, твой ход, далеко не уходи...ахахахахаххаахахха...все еще не смешно? потом поймешь. кст там от 1 до 9 поставь ')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList): #возвращает допустимый ход
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) !=0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #aлгоритм для ИИ для игры
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9]) #пробуем занять углы
    if move != None:
        return move
    
    if spaceFree(board, 5): #пробуем занять центр
        return 5

    
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board): #возвращает True если клетка на игровом поле занята
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("The Game Of X's & O's")

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('' + turn + ' ходит первым!')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            #Ход игрока
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Ахуй, малой, кожанные мешки выживут в этом году...')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья, позор')
                    break
                else:
                    turn = 'Компуктер'

        else:
            #ход моего смертоносного ИИ
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("УУУУ, малой. ИИ победил, че теперь то делать будешь ммм?")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья, позор!')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем еще раз, малой? Или сыкуешь...(да или нет))))')
    if not input().lower().startswith('д'):
        break
    

















































    
    
    
