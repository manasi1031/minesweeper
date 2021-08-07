import random
import os


def instructions():
    """
    Function to display the instructions on how to play
    """
    print("Welcome!")
    print("Instructions to play the game:")
    print("1. Enter row and column number to select a cell, Example \"2 3\"")
    print("2. In order to flag a mine:"
          "Enter F after row and column numbers, Example \"2 3 F\"")
    print("3. If you step on a mine, then GAME OVER")


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


def clear():
    """
    Function for clearing the terminal
    """
    os.system("clear")


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

    set_mines()
    set_values()
    instructions()
    over = False  # Variable for maintaining Game Loop
    while not over:  # The Game Loop
        print_mines_grid()

        inp = input("Enter row number followed by space"
                    " and column number:").split()
        if len(inp) == 2:
            try:
                val = list(map(int, inp))
            except ValueError:
                clear()
                print("Wrong input! Please try again.")
                instructions()
                continue
