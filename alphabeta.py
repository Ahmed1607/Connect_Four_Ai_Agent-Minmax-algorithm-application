import math
from tkinter import *
import random


Alpha_Beta_window = Tk()

Alpha_Beta_window.title("alpha beta  Esay")
Alpha_Beta_window.geometry("800x600")

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]


def get_next_row(col):
    N = 6
    for N in reversed(range(N+1)):
        if grid[N][col] == 0:
            return N


def p():
    grid_str = []
    for i in range(6):
        row_str = ""
        for j in range(7):
            row_str += str(grid[i][j]) + " "
        grid_str.append(row_str.strip())
    grid_str = "\n".join(grid_str)
    return grid_str


Label_0 = Label(Alpha_Beta_window, text=str(p()), font='0')
Label_0.place(x=320, y=50)


def row_check():
    for row in range(6):
        for col in range(7 - 3):
            if grid[row][col] != "." and grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == grid[row][col + 3] == 1:
                return 1
            if grid[row][col] != "." and grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == grid[row][col + 3] == 2:
                return 2


def colo_check():
    for row in range(6 - 3):
        for col in range(7):
            if grid[row][col] != "." and grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col] == 1:
                return 1
            elif grid[row][col] != "." and grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col] == 2:
                return 2


def minmax_algo():
    colo = random.randint(0, 5)
    print(colo)
    for i in range(5, -1, -1):
        if grid[int(i)][int(colo)] == 1 or grid[int(i)][int(colo)] == 2:
            continue
        else:
            grid[int(i)][int(colo)] = 2
            break


def diagonal_check_1():
    for row in range(6 - 3):
        for col in range(7 - 3):
            if grid[row][col] != "." and grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3] == 1:
                return 1
            elif grid[row][col] != "." and grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3] == 2:
                return 2


def diagonal_check_2():
    for row in range(6 - 3):
        for col in range(3, 7):
            if grid[row][col] != "." and grid[row][col] == grid[row + 1][col - 1] == grid[row + 2][col - 2] == grid[row + 3][col - 3] == 1:
                return 1
            elif grid[row][col] != "." and grid[row][col] == grid[row + 1][col - 1] == grid[row + 2][col - 2] == grid[row + 3][col - 3] == 2:
                return 2


def vertical_count(row, col):
    value = 0
    if grid[row][col] != "." and grid[row+1][col] == grid[row+2][col] == grid[row+3][col] == 2:  # 3 pieces in column
        value += 30
    elif row >= 1 and grid[row+1][col] == grid[row+2]:  # 2 pieces in column
        value += 20
    elif row >= 2 and grid[row + 1][col]:  # 1 piece
        value+10
    else:
        return 0  # zero pieces

    return value


def horizontal_count(row, column):
    count = 0  # Number of pieces of the same color in the same horizontal line
    current_column = column - 1  # Start from the previous column

    # Check pieces to the left of the specified position
    while current_column >= 0 and grid[row][current_column] == 2:
        count += 10
        current_column -= 1

    current_column = column + 1  # Start from the next column

    # Check pieces to the right of the specified position
    while current_column < len(grid[0]) and grid[row][current_column] == 2:
        count += 10
        current_column += 1

    return count


def Diagonal_count1(row, column):
    count = 0  # Number of pieces of the same color in the same horizontal line
    current_column = column - 1  # Start from the previous column

    # Check pieces to the left of the specified position
    while current_column >= 0 and grid[row][current_column] == 2:
        count += 10
        current_column -= 1
        row += 1

    current_column = column + 1  # Start from the next column

    # Check pieces to the right of the specified position
    while current_column < len(grid[0]) and grid[row][current_column] == 2:
        count += 10
        current_column += 1
        row -= 1

    return count


def Diagonal_count2(row, column):
    count = 0  # Number of pieces of the same color in the same horizontal line
    current_column = column - 1  # Start from the previous column

    # Check pieces to the left of the specified position
    while current_column >= 0 and grid[row][current_column] == 2:
        count += 10
        current_column -= 1
        row -= 1

    current_column = column + 1  # Start from the next column

    # Check pieces to the right of the specified position
    while current_column < len(grid[0]) and grid[row][current_column] == 2:
        count += 10
        current_column += 1
        row += 1

    return count


def check_win():
    if diagonal_check_1() == 1:
        Label2 = Label(Alpha_Beta_window, text="1 win", font='20')
        Label2.place(x=350, y=350)
    elif diagonal_check_1() == 2:
        Label3 = Label(Alpha_Beta_window, text="2 win", font='20')
        Label3.place(x=350, y=350)

    elif diagonal_check_2() == 1:
        Label4 = Label(Alpha_Beta_window, text="1 win", font='20')
        Label4.place(x=350, y=350)
    elif diagonal_check_2() == 2:
        Label5 = Label(Alpha_Beta_window, text="2 win", font='20')
        Label5.place(x=350, y=350)

    elif row_check() == 1:
        Label6 = Label(Alpha_Beta_window, text="1 win", font='20')
        Label6.place(x=350, y=350)

    elif row_check() == 2:
        Label7 = Label(Alpha_Beta_window, text="2 win", font='20')
        Label7.place(x=350, y=350)

    elif colo_check() == 1:
        Label8 = Label(Alpha_Beta_window, text="1 win", font='20')
        Label8.place(x=350, y=350)
    elif colo_check() == 2:
        Label9 = Label(Alpha_Beta_window, text="2 win", font='20')
        Label9.place(x=350, y=350)


def position_pick():
    MaxPoints = -1000
    position
    for c in range(7):
        if valid_place(c):
            H = horizontal_count(get_next_row(c), c)
            V = vertical_count(get_next_row(c), c)
            D1 = diagonal_check_1(get_next_row(c), c)
            D2 = diagonal_check_2(get_next_row(c), c)

            if MaxPoints < max(H, V, D1, D2):
                MaxPoints = max(H, V, D1, D2)
                position = c
    return MaxPoints


valid_places = []


def get_valid_places():

    for c in range(7):  # looping on colums ||
        if valid_place():
            valid_places.append(c)
    return valid_places


def valid_place(column):

    if grid[0][column] == 0:
        return True
    else:
        return False


def Alpha_Beta_algo():
    colo = random.randint(0, 5)
    print(colo)
    for i in range(5, -1, -1):
        if grid[int(i)][int(colo)] == 1 or grid[int(i)][int(colo)] == 2:
            continue
        else:
            grid[int(i)][int(colo)] = 2
            break
    #  if depth==0 or check_win()>0:
    #     if check_win()==2:
    #         return (None,math.inf) # 1 wins
    #     elif check_win()==1:
    #         return (None,-math.inf) # 2 wins
    #     else:
    #         return (None,0) # no body wins
    # else : # depth =0
    #     return (None , position_pick())
    # valid=get_valid_places
    # val=-math.inf
    # if isMaximizingPlayer:
    #     value =-math.inf
    #     column = random.choice(valid)
    #     for c in valid:
    #         row=get_next_row(column)
    #         new_grid=grid
    #         new_grid[row][column]=2
    #         points=Alpha_Beta_algo(new_grid ,depth-1 ,FALSE,alpha , beta)
    #         if points>val:
    #             val=points
    #             column=c
    #         alpha = max(alpha, value)
    #         if alpha >= beta:
    #             break
    #         return column, value
    # else:
    #     value =math.inf
    #     column = random.choice(valid)
    #     for c in valid:
    #         row=get_next_row(column)
    #         new_grid=grid
    #         new_grid[row][column]=1
    #         points=Alpha_Beta_algo(new_grid ,depth-1 ,FALSE,alpha , beta)
    #         if points>val:
    #             val=points
    #             column=c
    #         beta = min(beta, value)
    #         if alpha >= beta:
    #             break
    #         return column, value


def ev1():
    Label_0.destroy()
    colo = random.randint(0, 5)
    print(colo)
    for i in range(5, -1, -1):
        if grid[int(i)][int(colo)] == 1 or grid[int(i)][int(colo)] == 2:
            continue
        else:
            grid[int(i)][int(colo)] = 1
            break
    Label1 = Label(Alpha_Beta_window, text=p(), font='0')
    Label1.place(x=320, y=50)
    check_win()
    Alpha_Beta_algo()
    Label1.destroy()
    Label1 = Label(Alpha_Beta_window, text=p(), font='0')
    Label1.place(x=320, y=50)
    check_win()


label0 = Label(Alpha_Beta_window, text="Grid", font='5')
label0.place(x=350, y=0)


bt = Button(Alpha_Beta_window, command=ev1,
            text="Start Game", fg="Black", font="30")
bt.place(x=310, y=250)

Alpha_Beta_window.mainloop()
