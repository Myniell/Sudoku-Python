sudoku = [
    [0, 0, 0, 7, 9, 0, 0, 5, 0],
    [3, 5, 2, 0, 0, 8, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 4],
    [6, 0, 0, 3, 0, 1, 0, 0, 8],
    [9, 0, 0, 0, 8, 0, 0, 1, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 5, 0, 0, 8, 9, 1],
    [0, 8, 0, 0, 3, 7, 0, 0, 0]
]


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        x, y = find

    for i in range(1, 10):
        if valid(board, i, (x, y)):
            board[x][y] = i

            if solve(board):
                return True

            board[x][y] = 0

    return False


def valid(board, value, position):
    # check the row
    for i in range(len(board[0])):
        if board[position[0]][i] == value and position[1] != i:
            return False

    # check the column
    for i in range(len(board)):
        if board[i][position[1]] == value and position[0] != i:
            return False

    # check one of the 9 mini-boards

    mini_board_x = position[1] // 3
    mini_board_y = position[0] // 3

    for i in range(mini_board_y*3, mini_board_y*3 + 3):
        for j in range(mini_board_x*3, mini_board_x*3 + 3):
            if board[i][j] == value and position != (i,j):
                return False

    return True


def show_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - -')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('|', end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range (len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


show_board(sudoku)
solve(sudoku)
print('---------------------------------------')
print('----------------SOLVED-----------------')
print('---------------------------------------')
show_board(sudoku)
