# Portfolio Project 3
------

# MINESWEEPER
The link is old and needs to change to new
![Mockup Image](https://github.com/manasi1031/Mighty-quest/blob/master/assets/images/mockup.jpg)

## Purpose:
---
Minesweeper is a Python terminal game, which runs in the Code Institute mock terminal of Heroku. This is the third milestone project in my academic schedule with the Code Institute.

## Information about Project:
---
Minesweeper is classic windows game. 

It is a single-player logic game where mines are hidden in a grid of squares and the player has to prevent himself from landing on a mine with the help of numbers in the neighbouring tiles. If you land on a mine, then “GAME OVER”.

Minesweeper is similar to a Sudoku puzzle; in that your success is largely contingent on being able to eliminate possible answers until only one answer remains.

I remember playing this game when in the 90’s and the craze that was associated with it. Hence I though it was a pretty good idea to bring this classic and nostalgic game alive in my project.

If you have never played before please see the link to read some information about this. https://en.wikipedia.org/wiki/Minesweeper_(video_game) 

## [View live website here] ADD

---------

## Table of Contents
---

- [Information to Play](#information-to-play)
    - [How to play](#how-to-play)
    - [Detailed Instructions](#detailed-instructions)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future features](#future-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)



## Information to Play
---
### How to play:
Instructions to play the game on the actual game:
1. Each board has 8 rows and 8 columns and 8 mines
2. Enter row and column number to select a cell, Example \"2 3\"
3. In order to flag a mine: Enter F after row and column numbers, Example \"2 3 F\"
4. If you step on a mine, then GAME OVER

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

## Features
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

### Future features:
- Time limit
- Level of difficulty – Easy, Medium and Hard.
- Maintain names of users who have won the game

[Back to Table of Contents](#table-of-contents)
---

## Technologies used:
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



[Back to Table of Contents](#table-of-contents)
---

## DEPLOYMENT
---


[Back to Table of Contents](#table-of-contents)
---

## CREDITS
---



[Back to Table of Contents](#table-of-contents)
---