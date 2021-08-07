# write code

def instructions():
    """
    Function to display the instructions on how to play
    """
    print("Welcome!")
    print("Instructions to play the game:")
    print("1. Enter row and column number to select a cell, Example \"2 3\"")
    print("2. In order to flag a mine: Enter F after row and column numbers, Example \"2 3 F\"")
    print("3. If you step on a mine, then GAME OVER")

instructions()


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
        if row == 0:
            for col in range(num):
                cell = cell + "______"
            print(cell)

        cell = "     "
        for col in range(num):
            cell = cell + "|     "
        print(cell + "|")

        cell = "  " + str(row + 1) + "  "
        for col in range(num):
            cell = cell + "|  " + str(mine_values[r][col]) + "  "
        print(cell + "|")

        cell = "     "
        for col in range(num):
            cell = cell + "|_____"
        print(cell + '|')

    print()

print_mines_grid()