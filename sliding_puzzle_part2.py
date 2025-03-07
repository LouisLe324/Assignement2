#Louis Le 2338697

import random
import sys


def tileLabels(n):
    tiles = []
    for i in range(0, n**2 -1):
        tiles.append(i + 1)
    tiles.append(' ')
    return tiles

def getNewPuzzle(n):
    board = []
    j = 0
    tiles = tileLabels(n)
    random.shuffle(tiles)
    for i in range(n):
        row = []
        for i in range(n):
            row.append(tiles[j])
            j += 1
        board.append(row)
    return board

def findEmptyTile(board):
    i = 0
    j = 0
    for row in board:
        for number in row:
            if number == ' ':
                i = row.index(number)
                j = board.index(row)     

    return (j, i)

def nextMove(board):
    emptytile = findEmptyTile(board)
    row, column = emptytile
    while True:
        W = 'W'
        A = 'A'
        S = 'S'
        D = 'D'
        if row == 0:
            S = ''
        if row == len(board) - 1:
            W = ''
        if column == 0:
            D = ''
        if column == len(board) - 1:
            A = ''
        command = input(f'Enter WASD (or QUIT): ({W}) ({A}) ({S}) ({D}) ').upper()

        if command == 'QUIT':
            sys.exit()

        if command == 'W' and W:
            return 'W'
            
        elif command == 'A' and A:
           return 'A'

        elif command == 'S' and S:
            return 'S'

        elif command == 'D' and D:
           return 'D'
        
        else:
            print('Please enter a valid move')
 

def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))


#part 2

def makeMove(board, move):
    emptytile = findEmptyTile(board)
    row, column = emptytile

    if move == 'W':
        
        board[row][column], board[row + 1][column] = board[row + 1][column], board[row][column]
 
            
    elif move == 'A':
        board[row][column], board[row][column + 1] = board[row][column + 1], board[row][column]
  

    elif move == 'S':
        board[row][column], board[row - 1][column] = board[row - 1][column], board[row][column]
  

    elif move == 'D':
        board[row][column], board[row][column - 1] = board[row][column - 1], board[row][column]

def checkWin(n, board):
    sortedTiles = tileLabels(n)
    sortedBoard = []
    j = 0
    for i in range(n):
        row = []
        for k in range(n):
            row.append(sortedTiles[j])
            j += 1
        sortedBoard.append(row)
    return sortedBoard == board



#Main Program

def mainProgram(n):
    print('Welcome User! This program will ask for a number and will print out a board with the dimensions of the number given. However, there will be an empty space in that board. You can slide adjacent numbers into that empty space using the letters WASD, W for the number above, S for the number under, A for the number to the left and D for the number to the right. You have a limited amount of moves to sort the numbers from smallest to largest from left to right.')
    n = int(input('Please enter a number:'))
    board = getNewPuzzle(n)
    displayBoard(board)
    count = 0
    if n == 3:
        maxMoves = 31
    else:
        maxMoves = 5 * (n**2)
    while count < maxMoves:
        move = nextMove(board)
        makeMove(board, move)
        displayBoard(board)
        count += 1

        if checkWin(n, board):
            print('Congratulations! You Won!')
            return
    print('You lost! You reached the max amount of allowed moves. Best of luck next time!')



mainProgram(0)

    
        







    
