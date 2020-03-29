# import random as rd
from numpy import array as narray
from numpy import matrix as nmatrix
from math import sqrt

'''
size = 9
# initialize a grid
   grid = np.array([np.zeros(size)])
   for row in range(size - 1):
       board = np.append(grid, [np.zeros(size)], axis = 0)
       '''
# for now, define your own puzzle:
'''
grid = narray.[[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''
size = 9  # 9 by 9 game by default but changeable
game = narray([[0, 0, 0, 0, 0, 0, 0, 3, 1],
               [7, 0, 0, 9, 0, 0, 0, 4, 0],
               [0, 0, 0, 0, 0, 0, 5, 0, 0],
               [0, 0, 0, 0, 3, 1, 0, 0, 0],
               [9, 0, 0, 0, 0, 0, 0, 0, 8],
               [0, 0, 0, 4, 0, 5, 0, 0, 0],
               [0, 0, 0, 6, 0, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 6],
               [0, 5, 3, 0, 0, 0, 0, 0, 0]])


# (y, x) = (r, c)
# matrix index c = coordinate x = column
# matrix index r = coordinate y = row
def possible(r, c, num):
    # given a number num, check if it's possible to put it in (r, c)
    global game
    global size
    zone = int(sqrt(size))
    for i in range(0, size):  # check within row
        if game[r][i] == num:
            return False
    for j in range(0, size):  # check within col
        if game[j][c] == num:
            return False
    # within each zone:
    rz = (r // 3) * 3
    cz = (c // 3) * 3
    # [0:2], [3:5], [6:8]
    # (1, 4): check ([0:2], [3:5])
    '''
    for m in range(rz, rz + 2):
        for n in range(cz, cz + 2):
            if game[m][n] == num:
                return False
    '''
    for m in range(0,3):
        for n in range(0,3):
            if game[rz+m][cz+n] == num:
                return False
    return True

'''
if __name__ == "__main__":
    # game = np.matrix(game)
    # global game
    for test in range(1, 10):
        for row in range(9):
            for col in range(9):
                while game[row][col] != 0:
                    if possible(row, col, test):
                        game[row][col] = test

    print(game)
    print("Program ends.")
'''

def solve_it():
    global game
    # global size
    for row in range(9):
        for col in range(9):
            if game[row][col] == 0:
                #for guess in range(1, size + 1):
                for guess in range(1, 10):
                    if possible(row, col, guess):
                        game[row][col] = guess
                        solve_it()
                        game[row][col] = 0
                return
    print(nmatrix(game))
#if __name__ == "__main__":
solve_it()
    #print(game)