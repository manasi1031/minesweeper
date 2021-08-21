# PORTFOLIO PROJECT 3
------

# MINESWEEPER
CHANGE
![Mockup Image](https://github.com/manasi1031/Mighty-quest/blob/master/assets/images/mockup.jpg)

## PURPOSE:
---
Minesweeper is a Python terminal game, which runs in the Code Institute mock terminal of Heroku. This is the third milestone project in my academic schedule with the Code Institute.

## INFORMATION ABOUT PROJECT:
---
Minesweeper is classic windows game. 

It is a single-player logic game where mines are hidden in a grid of squares and the player has to prevent himself from landing on a mine with the help of numbers in the neighbouring tiles. If you land on a mine, then “GAME OVER”.

Minesweeper is similar to a Sudoku puzzle; in that your success is largely contingent on being able to eliminate possible answers until only one answer remains.

I remember playing this game when in the 90’s and the craze that was associated with it. Hence I though it was a pretty good idea to bring this classic and nostalgic game alive in my project.

If you have never played before please see the link to read some information about this. https://en.wikipedia.org/wiki/Minesweeper_(video_game) 

## [View live website here] ADD

---------

## TABLE OF CONTENTS
---

- [Information to Play](#information-to-play)
    - [How to play](#how-to-play)
    - [Detailed Instructions](#detailed-instructions)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future features](#future-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
    - [Functionality Testing](#functionality-testing)
    - [Solved Bugs](#solved-bugs)
    - [Remaining Bugs](#remaining-bugs)
    - [Code Validation](#code-validation)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)



## INFORMATION TO PLAY
---

### How to play:

Instructions to play the game on the actual game:
1. Each board has 8 rows and 8 columns and 8 mines.
2. Enter row and column number to select a cell, Example \"2 3\".
3. In order to flag a mine: Enter F after row and column numbers, Example \"2 3 F\".
4. If you step on a mine, then GAME OVER.

### Detailed Instructions:

- You are presented with a board of unmarked cells. 
- Some cells contain mines (bombs), others don't.
- Each board has 8 rows and 8 columns and 8 mines.
- If you select a cell containing a bomb, you lose. 
- If you manage to select all the cells (without selecting on any bombs) you win.
- Selecting a cell which doesn't have a mine reveals the number of adjacent cells containing mines. Use this information plus some guess work to avoid the mines.
- To select a cell, type the row number with a space and followed by column number.
- To flag a cell you think is a bomb, type the row number with a space followed by column number and space again followed by the words “F” or “f”.
- Adjacent cells above, below, left, right, and all 4 diagonals surround a cell. Cells on the sides of the board or in a corner have fewer neighbours.
- If you open a cell with 0 neighboring bombs, all its neighbors will automatically open. This can cause a large area to automatically open.
- A number on a cell refers to the number of mines that are currently touching that cell. For example, if there are two cells touching each other and one of the cells has "1" on it, you know that the cells next to it has a mine beneath it. 
- You don't have to flag all the mines to win; you just need to open all non-mine cells.
- The 'M' symbol denotes the presence of a ‘mine’ in that cell. Any number on the grid denotes the number of mines present in the neighbouring ‘eight’ cells. 
- You cannot stop the game mid-way unless you click “Run terminal”.
- You will have the option of starting a new game or redoing the one you just played.

[Back to Table of Contents](#table-of-contents)
---

## FEATURES
---

### Existing Features:

- Random grid:
    - The location of mines change with every game.
    - The player cannot see this location until end of game.

- Accepts users input for name and selecting cell and or mine choice

- Input validation and error-checking:
    - You must enter numbers for the rows and columns
    - You must enter F or f for the flag
    - You cannot enter the row and column greater than 8
    - You cannot enter the same input again

- Maintains a record of the names of all the players who have played the game.

### Future features:

- Time limits or recording time in gerenal taken to play.
- Level of difficulty – Easy, Medium and Hard.


[Back to Table of Contents](#table-of-contents)
---

## TECHNOLOGIES USED:
---

### Programming Languages:
- Python

### Git:
- Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

### Github:
- GitHub is used to store the projects code after being pushed from Git.

### Code Institutes mock terminal (Heroku):
- Code Institute provided a mock terminal for use for the project.

### Lucidchart:
- Lucidchart was used to map the workflow for the game.
ADD CHART HERE


## TESTING
---

### Functionality Testing

- Each piece of code was tested in Gitpod as well as in Python Tutor (where possible).
- Family members and friends were asked to test the app once the final product was deployed. 

### Solved Bugs

- 

### Remaining Bugs

- The data does not append to workheet so the 2 functions still dont work correctly 


### Code Validation

The code was checked using [PEP8 Python Validator](http://pep8online.com/) and it did not show any errors.

Add image at end

[Back to Table of Contents](#table-of-contents)
---

## DEPLOYMENT
---

This project was deployed using Code Institute's mock terminal for Heroku.

- Fork or clone this repository

- Create a new Heroku app

- Set the buildbacks to Puthon and NodeJS in that order

- Link the Heroku app to repository

- Click on Deploy


[Back to Table of Contents](#table-of-contents)
---

## CREDITS
---

1. I have used the time.sleep() function to show messages and hold it before showing grid again. This was to give some pause for the player to read instructions or feedback. The link I used was - https://realpython.com/python-sleep/#adding-a-python-sleep-call-with-timesleep  

2. Python recursive function usage or understanding notes taken from the below link: https://www.programiz.com/python-programming/recursion#:~:text=Recursive%20Function%20in%20Python%20Following%20is%20an%20example,%28denoted%20as%206%21%29%20is%201%2A2%2A3%2A4%2A5%2A6%20%3D%20720.%20 

3. I have used termcolor cprint usage options by reading this page for examples of how to use to give some color to the page - https://www.programcreek.com/python/example/60805/termcolor.cprint 

4. I have used the link from Wikipedia show show people what minesweeper is in general - https://en.wikipedia.org/wiki/Minesweeper_(video_game)

[Back to Table of Contents](#table-of-contents)
---

## ACKNOWLEDGEMENTS
---
I could not have done this project without the guidance and confidence of my mentor - Adegbenga Adeye.

Last but not the least, I would like to thank [Code Institute](https://codeinstitute.net/) for their support.

[Back to Table of Contents](#table-of-contents)
---