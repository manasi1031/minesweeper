# Import packages
import random
import os
import time
from termcolor import cprint
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('minesweeper')


name = [""]


def players_name():
    """
    And add player name
    """
    cprint("\t\t\tMINESWEEPER\n", "green")
    name = input("Enter the player name:\n")
    print("Welcome!", name, ". Let's play Minesweeper!")
    print("\n")
    time.sleep(2)
    return name


def update_sheet(data):
    """
    Update worksheet with new players name
    """
    players_name = SHEET.worksheet("players")
    players_name.append_row([data])


def get_number():
    """
    Get the last row in the sheet
    """
    numb = SHEET.worksheet("players").get_all_values()
    player_numb = len(numb) - 1
    print(f"You are player number: {player_numb}. Let's play!")
    print("\n")
    time.sleep(1)


def instructions():
    """
    Function to display the instructions on how to play
    """
    cprint("Instructions to play the game:\n", "green")
    print("1.Each board has 8 rows and 8 columns and 8 mines")
    cprint("2. Enter row and column number to select a cell, Example \"2 3\"")
    print("3. In order to flag a mine:"
          "Enter F after row and column numbers, Example \"2 3 F\"")
    print("4. If you step on a mine, then GAME OVER\n")
    time.sleep(5)


def print_mines_grid():
    """
    Printing the Minesweeper Layout
    to show the framework of the game
    """
    global mine_values
    global num
    print()
    cprint("\t\t\tMINESWEEPER\n", "green")

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
    # Track mines already set up
    count = 0
    while count < mines_no:
        # Random number from all grid positions
        val = random.randint(0, num*num-1)
        # Generate row and column from number
        r = val // num
        col = val % num
        # Place mine if not placed
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

    # Loop for counting cell values
    for r in range(num):
        for col in range(num):
            # If it has a mine, then skip
            if numbers[r][col] == -1:
                continue
            # check up
            if r > 0 and numbers[r-1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # check down
            if r < num-1 and numbers[r+1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # check left
            if col > 0 and numbers[r][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # check right
            if col < num-1 and numbers[r][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # check top-left
            if r > 0 and col > 0 and numbers[r-1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # check top-right
            if r > 0 and col < num-1 and numbers[r-1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # check bottom-left
            if r < num-1 and col > 0 and numbers[r+1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # check bottom-right
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
                cprint("You chose to play again!!!", "green")
                time.sleep(2)
                play_game()
            if game_end_input == 2:
                cprint("You chose to exit the game!!!", "green")
                time.sleep(2)
                print("Click 'RUN PROGRAM' to play again")
                exit()
        except ValueError:
            cprint("Wrong choice!. Please enter 1 to play or 2 to quit", "red")
            game_end_input


def adjacent_cells(r, col):
    """
    Recursive function to display all
    zero-valued adjacent cells around mines
    """
    global mine_values
    global numbers
    global visit
    # If the cell has not been visited
    if [r, col] not in visit:
        # Mark visited cell
        visit.append([r, col])
        # Zero valued cell
        if numbers[r][col] == 0:
            # Display to user
            mine_values[r][col] = numbers[r][col]
            # Recursive calls for adjacent cells
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
        # If not a zero valued cell
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
    # Count all numbered values
    count = 0
    # Check each cell in grid as a loop
    for r in range(num):
        for col in range(num):
            if mine_values[r][col] != ' ' and mine_values[r][col] != 'F':
                count = count + 1
    # Count comparison
    if count == num * num - mines_no:
        return True
    else:
        return False


def play_game():
    """
    Main module running the game from
    instructions until end game.
    """
    global num
    global mines_no
    global numbers
    global visit
    global mine_values

    # Actual values of grid
    num = 8
    mines_no = 8
    numbers = [[0 for y in range(num)] for x in range(num)]
    mine_values = [[' ' for y in range(num)] for x in range(num)]
    flags = []  # Positions of flag

    player_name = players_name()
    update_sheet(player_name)
    get_number()
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

        # Input from user row & column & // flag
        inp = input("Enter row number followed by space"
                    " and column number \n and space again with "
                    "F/f if flagging a mine: \n").split()
        # Standard input check
        if len(inp) == 2:
            try:
                val = list(map(int, inp))
                print("your input was: ", inp)
                time.sleep(2)
            except ValueError:
                cprint("Wrong input! Please try again.", "red")
                instructions()
                time.sleep(2)
                continue
        # Flag input check
        elif len(inp) == 3:
            if inp[2] != 'F' and inp[2] != 'f':
                cprint("Wrong input! Please try again.", "red")
                instructions()
                time.sleep(2)
                continue
            try:
                val = list(map(int, inp[:2]))
            except ValueError:
                cprint("Wrong input! Please try again.", "red")
                instructions()
                time.sleep(2)
                continue
            if val[0] > num or val[0] < 1 or val[1] > num or val[1] < 1:
                cprint("Wrong input! Please try again.", "red")
                instructions()
                time.sleep(2)
                continue
            # Get row and column numbers
            r = val[0]-1
            col = val[1]-1
            # If a cell has been flagged already
            if [r, col] in flags:
                cprint("Flag already set", "red")
                time.sleep(2)
                continue
            # If a cell has been displayed already
            if mine_values[r][col] != ' ':
                cprint("Value already displayed!", "red")
                instructions()
                time.sleep(2)
                continue
            # Check the number for flags
            if len(flags) < mines_no:
                cprint("Flag set", "red")
                # Add flag to list
                flags.append([r, col])
                # Set flag to display
                mine_values[r][col] = 'F'
                time.sleep(2)
                continue
            else:
                cprint("Flags finished", "red")
                instructions()
                time.sleep(2)
                continue
        else:
            cprint("Wrong input! Please try again.", "red")
            instructions()
            time.sleep(2)
            continue
        if val[0] > num or val[0] < 1 or val[1] > num or val[1] < 1:
            cprint("Wrong Input! Please try again.", "red")
            instructions()
            time.sleep(2)
            continue
        r = val[0]-1
        col = val[1]-1
        # Unflag cell if already flagged
        if [r, col] in flags:
            flags.remove([r, col])
        # Game over is landed on mine
        if numbers[r][col] == -1:
            mine_values[r][col] = 'M'
            show_mines()
            print_mines_grid()
            cprint("You landed on a mine! GAME OVER!!!!!", "red")
            over = True
            end_game()
            continue
        # If landed on a mine with zero in adjacent cells
        elif numbers[r][col] == 0:
            visit = []
            mine_values[r][col] = '0'
            adjacent_cells(r, col)
        # if even 1 mine in adjacent cell
        else:
            mine_values[r][col] = numbers[r][col]
        # check for game completion or finish
        if(game_check_finish()):
            show_mines()
            print_mines_grid()
            cprint("Congratulations!!! YOU WIN", "green")
            over = True
            end_game()
            continue
        clear()


play_game()
