import random
import os
import time


def instructions():
    """
    Function to display the instructions on how to play
    And add player name
    """
    name = str(input("enter the player name: "))
    print("Welcome!", name)
    time.sleep(3)
    print("Instructions to play the game:")
    print("1. Enter row and column number to select a cell, Example \"2 3\"")
    print("2. In order to flag a mine:"
          "Enter F after row and column numbers, Example \"2 3 F\"")
    print("3. If you step on a mine, then GAME OVER")
    time.sleep(5)


def print_mines_grid():
    """
    Printing the Minesweeper Layout
    to show the framework of the game
    """
    global mine_values
    global num
    print()
    print("\t\t\tMINESWEEPER\n")

    cell = "   "
    for i in range(num):
        cell = cell + "     " + str(i + 1)
    print(cell)

    for r in range(num):
        cell = "     "
        if r == 0:
            for col in range(num):
                cell = cell + "______"
            print(cell)

        cell = "     "
        for col in range(num):
            cell = cell + "|     "
        print(cell + "|")

        cell = "  " + str(r + 1) + "  "
        for col in range(num):
            cell = cell + "|  " + str(mine_values[r][col]) + "  "
        print(cell + "|")

        cell = "     "
        for col in range(num):
            cell = cell + "|_____"
        print(cell + '|')

    print()


def set_mines():
    """
    Function for setting up Mines, tracking them,
    and placing them if not already there
    """
    global numbers
    global mines_no
    global num
    count = 0
    while count < mines_no:
        val = random.randint(0, num*num-1)
        r = val // num
        col = val % num
        if numbers[r][col] != -1:
            count = count + 1
            numbers[r][col] = -1


def set_values():
    """
    Function for setting up the other grid values.
    Loop for counting each cell value.
    Checking top, left, right, bottom and
    top-left, top-right, bottom-left and bottom-right
    """
    global numbers
    global num

    for r in range(num):
        for col in range(num):
            if numbers[r][col] == -1:
                continue
            if r > 0 and numbers[r-1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            if r < num-1 and numbers[r+1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            if col > 0 and numbers[r][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            if col < num-1 and numbers[r][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            if r > 0 and col > 0 and numbers[r-1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            if r > 0 and col < num-1 and numbers[r-1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            if r < num-1 and col > 0 and numbers[r+1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            if r < num-1 and col < num-1 and numbers[r+1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1


def end_game():
    """
    User can chose whether to restart the game
    or to quit the program.
    """
    while True:
        try:
            game_end_input = int(input("Please enter 1 "
                                       "to play again or 2 to quit: \n"))
            if game_end_input == 1:
                print("You chose to play again!!!")
                set_mines()
                set_values()
                instructions()
            if game_end_input == 2:
                print("You chose to exit the game!!!")
                exit()
        except ValueError:
            print("Wrong choice!. Please enter 1 to play again or 2 to quit")
            game_end_input


def adjacent_cells(r, col):
    """
    Recursive function to display all
    zero-valued adjacent cells around mines
    """
    global mine_values
    global numbers
    global visit
    if [r, col] not in visit:
        visit.append([r, col])
        if numbers[r][col] == 0:
            mine_values[r][col] = numbers[r][col]
            if r > 0:
                adjacent_cells(r-1, col)
            if r < num-1:
                adjacent_cells(r+1, col)
            if col > 0:
                adjacent_cells(r, col-1)
            if col < num-1:
                adjacent_cells(r, col+1)
            if r > 0 and col > 0:
                adjacent_cells(r-1, col-1)
            if r > 0 and col < num-1:
                adjacent_cells(r-1, col+1)
            if r < num-1 and col > 0:
                adjacent_cells(r+1, col-1)
            if r < num-1 and col < num-1:
                adjacent_cells(r+1, col+1)
        if numbers[r][col] != 0:
            mine_values[r][col] = numbers[r][col]


def clear():
    """
    Function for clearing the terminal
    """
    os.system("clear")


def show_mines():
    """
    This function shows the mines if player has landed
    on a cell with mines.
    """
    global mine_values
    global numbers
    global num

    for r in range(num):
        for col in range(num):
            if numbers[r][col] == -1:
                mine_values[r][col] = 'M'


def game_check_finish():
    """
    Function to check for completion of the game
    """
    global mine_values
    global num
    global mines_no
    count = 0
    for r in range(num):
        for col in range(num):
            if mine_values[r][col] != ' ' and mine_values[r][col] != 'F':
                count = count + 1
    if count == num * num - mines_no:
        return True
    else:
        return False


if __name__ == "__main__":
    """
    Main function running the game from
    instructions until end game
    """
    num = 8
    mines_no = 8

    numbers = [[0 for y in range(num)] for x in range(num)]
    mine_values = [[' ' for y in range(num)] for x in range(num)]
    flags = []

    instructions()
    set_mines()
    set_values()

    over = False  # Variable for maintaining Game Loop
    while not over:  # The Game Loop
        """
        This loop oversees the below:
        The cell has already been flagged or not.
        Whether the cell to be flagged is already displayed to the player.
        The number of flags does not exceed the number of mines.
        """
        print_mines_grid()

        inp = input("Enter row number followed by space"
                    " and column number and space again with "
                    "F/f if flagging a mine:").split()
        if len(inp) == 2:
            try:
                val = list(map(int, inp))
            except ValueError:
                print("Wrong input! Please try again.")
                time.sleep(2)
                continue
        elif len(inp) == 3:
            if inp[2] != 'F' and inp[2] != 'f':
                print("Wrong input! Please try again.")
                time.sleep(2)
                continue
            try:
                val = list(map(int, inp[:2]))
            except ValueError:
                print("Wrong input! Please try again.")
                time.sleep(2)
                continue
            if val[0] > num or val[0] < 1 or val[1] > num or val[1] < 1:
                print("Wrong input! Please try again.")
                time.sleep(2)
                continue
            r = val[0]-1
            col = val[1]-1
            if [r, col] in flags:
                print("Flag already set")
                time.sleep(2)
                continue
            if mine_values[r][col] != ' ':
                print("Value already displayed!")
                time.sleep(2)
                continue
            if len(flags) < mines_no:
                print("Flag set")
                flags.append([r, col])
                mine_values[r][col] = 'F'
                time.sleep(2)
                continue
            else:
                print("Flags finished")
                time.sleep(2)
                continue
        else:
            print("Wrong input! Please try again.")
            time.sleep(2)
            continue
        if val[0] > num or val[0] < 1 or val[1] > num or val[1] < 1:
            print("Wrong Input! Please try again.")
            time.sleep(2)
            continue
        r = val[0]-1
        col = val[1]-1
        if [r, col] in flags:
            flags.remove([r, col])
        if numbers[r][col] == -1:
            mine_values[r][col] = 'M'
            show_mines()
            print_mines_grid()
            print("You landed on a mine! GAME OVER!!!!!")
            over = True
            end_game()
            continue
        elif numbers[r][col] == 0:
            visit = []
            mine_values[r][col] = '0'
            adjacent_cells(r, col)
        else:
            mine_values[r][col] = numbers[r][col]
        if(game_check_finish()):
            show_mines()
            print_mines_grid()
            print("Congratulations!!! YOU WIN")
            over = True
            end_game()
            continue
        clear()
