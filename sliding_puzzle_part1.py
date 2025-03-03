import random
import sys
tiles = []

def tileLabels(n):
    for i in range(0, n**2 -1):
        tiles.append(i + 1)
    tiles.append(' ')
    return tiles


def getNewPuzzle(n):
    board = []
    j = 0
    tileLabels(n)
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
        print(j)
        for number in row:
            if number == ' ':
                i = row.index(number)
                j = board.index(row)     

    return (j, i)

#def nextMove(board):
#    emptytile = findEmptyTile(board)
#    while True:
#        a = ''
#        b = ''
#        c = ''
#        d = ''
#        if emptytile[0] == 0:
#        input(f'Enter WASD (or QUIT) : {a}{b}{c}{d}')




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



        
        
        
        
