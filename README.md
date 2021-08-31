# PORTFOLIO PROJECT 3
------

# MINESWEEPER

![Multi Device Mockup Image](https://github.com/manasi1031/minesweeper/blob/main/assets/images/multi-device-mockup.jpg)

![Single Mockup Image](https://github.com/manasi1031/minesweeper/blob/main/assets/images/mockup.jpg)

## PURPOSE:
---
Minesweeper is a Python terminal game, which runs in the Code Institute mock terminal of Heroku. This is the third milestone project in my academic schedule with the Code Institute.

## INFORMATION ABOUT PROJECT:
---
Minesweeper is classic windows game. 

It is a single-player logic game where mines are hidden in a grid of squares and the player has to prevent himself from landing on a mine with the help of numbers in the neighbouring tiles. If you land on a mine, then “GAME OVER”.

Minesweeper is similar to a Sudoku puzzle; in that your success is largely contingent on being able to eliminate possible answers until only one answer remains.

I remember playing this game when in the 90’s and the craze that was associated with it. Hence I though it was a pretty good idea to bring this classic and nostalgic game alive in my project.

If you have never played before, please see the link to read some information about this. https://en.wikipedia.org/wiki/Minesweeper_(video_game) 

## [View live website here](https://minesweeper2021.herokuapp.com/)

---------

## TABLE OF CONTENTS
---

- [Information to Play](#information-to-play)
    - [How to play](#how-to-play)
    - [Detailed Instructions](#detailed-instructions)
- [Goals](#goals)
    - [Goal](#goal)
    - [Aim](#aim)
    - [User Stories and testing](#user-stories-and-testing)
    - [Target Audience](#target-audience)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future features](#future-features)
- [Technologies Used](#technologies-used)
- [Data Model](#data-model)
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

![Instructions on deployed site](https://github.com/manasi1031/minesweeper/blob/main/assets/images/instructions.jpg)

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
- You will have the option of starting a new game or redoing the one you just played at the end of the game.
- The restart game will start from the exact beginning from requesting the player name to add to sheet. 

[Back to Table of Contents](#table-of-contents)
---


## GOALS
---

### Goal:
My goal is to re-create the minesweeper game in a Python terminal to test my ability of Python coding.

### Aim:
My aim is to provide data relevant to the user story and enhance the overall experience of this game.

### User Stories and testing:

#### First time user:
- I want clear instructions about how to play

    _I have given clear instructions to play the game in 4 steps and this repeats with any key input errors_

- I want clear feedback to my input

    _Clear feedback is given to inputs. Example: when name is given, it states "welcome <player name>"; when row and column number is added, the system states what the player has chosen, etc_

- I want to have an option to play game again or exit if I win or fail.

    _There is a function that gives an option at the end to either press 1 to play again or press 2 to exit the game_


#### Repeat User:
- I want to see scores
- I want to time my game
- I want to have levels of difficulty
Note: This is a part of the future features section and not used for current version.

#### Target Audience:
Anyone can play this game and there is no specific target audience for the game.

[Back to Table of Contents](#table-of-contents)
---


## FEATURES
---

### Existing Features:

- I have used the random grid for the game outlining the below:
    - The location of mines change with every game.
    - The player cannot see this location until end of game either when they win or land on a mine.

![Grid on deployed site](https://github.com/manasi1031/minesweeper/blob/main/assets/images/grid.jpg)

- The game starts immediately after the instructions are displayed, as that means the player wants to play the game. The view can be scrolled if the player wants to read the instructions again or add wrong input in the game and see the instructions.

- The game accepts users input for player name and selecting cell (Row & Column) and or mine choice.

![Player name Image](https://github.com/manasi1031/minesweeper/blob/main/assets/images/player-name.jpg)

![Game input Image](https://github.com/manasi1031/minesweeper/blob/main/assets/images/game-input.jpg)

![End of game with replay option Image](https://github.com/manasi1031/minesweeper/blob/main/assets/images/end-game-replay-option.jpg)


- The game also allows for input validation and error-checking as below:
    - You must enter numbers for the rows and columns with a space in between.
    - You must enter F or f for marking the flag.
    - You cannot enter the row and column greater than 8.
    - You cannot flag more than 8 flags.
    - If you put the above it will show an error and also display the instructions again to player to read.
    - The current feature does not prompt if a cell is already displaying a number (chosen cell) and it just skips to a new grid with new input. This will be an update to add to the future feature version.
    - If you have chosen a flag but you just add the row and column co-ordinates, then the flag will change to an actual number (or mine!!!) if you changed your mind.

![Input flag no space error](https://github.com/manasi1031/minesweeper/blob/main/assets/images/input-flag-no-space-error.jpg)

![Input no number error](https://github.com/manasi1031/minesweeper/blob/main/assets/images/input-no-number-error.jpg)

![Input no space error](https://github.com/manasi1031/minesweeper/blob/main/assets/images/input-no-space-error.jpg)

![Flags exceeded error](https://github.com/manasi1031/minesweeper/blob/main/assets/images/flags-exceeded-error.jpg)


- Maintains a record of the names of all the players who have played the game and shows the number of the player on the list recorded. To view the google spreadsheet for any issues see [link](https://docs.google.com/spreadsheets/d/1b8eg39v8RJIqNgyyxrlcV7u56zLA8AMa-3h0r1FZ8Sw/edit?usp=sharing)

![Player list Image](https://github.com/manasi1031/minesweeper/blob/main/assets/images/player-list.jpg)


### Future features:

- Time limits or recording time in general taken to play.
- Level of difficulty – Easy, Medium and Hard.
- If a value is already provided on grid, then state that its there and try again by highlighting the section view.
- After instructions are displayed, to add an option whether to begin playing game or still read instructions again.


![Grid on deployed site](https://github.com/manasi1031/minesweeper/blob/main/assets/images/grid.jpg)

FEEDBACK NOTE UPDATE: I received feedback that grid size of the minesweeper is too big for the Heroku deployed window. Please note that at the time of me creating this grid, it showed perfectly fine on the gitpod terminal. When I deployed it, the view does not fit in the screen and my fellow students on Slack suggested that I reduce the size to fit the screen. However, I have chosen not to proceed with this to give a better game experience and people can really scroll down the screen to view the full view.
This is not a bug really, but I wanted to ensure that I have recorded feedback received and taken a note of it.
In the future version, this will be the easy grid and the smallest one available. The medium and hard versions will be bigger than this for sure but I may re-visit the cell size or have more columns, etc.

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

### PNG to JPG:
- I have used this [link](https://png2jpg.com/) to convert png images to jpg.

### Lucidchart:
- Lucidchart was used to map the workflow for the game.
I was not comfortable with this feature and have tried my best to show an overview of my game.

![Lucid Chart for Workflow](https://github.com/manasi1031/minesweeper/blob/main/assets/images/lucid-chart.jpg)


[Back to Table of Contents](#table-of-contents)
---

## DATA MODEL
---

- Each function is defined separately and finally called in the play_game function to ensure that sections are working individually.
    - _players_name_ function lets the player add their name.
    - _update_sheet_ function adds the name recorded to the google spreadsheet.
    - _get_number_ function gets the last row number of the player and gives the comment - "You are player number "20". Lets play!".
    - _instructions_ function gives the instructions for players to read about how to play the game.
    - _print_mines_grid_ function 
- I have used Google spreadsheets to record player names and pulled the record to show the number on the list of the player from who have played this game prior.
- I have not used any Python library for this project as it did not seem relevant.
- My code is quite simple and hence on this occassion, I have not used any Class. This may change in the future versions.
- I have used python packages / modules as below for the project:
    - "Random" to plot the mines and adjacent cells so that mines are never in the same place.
    - "Time" has been used to show the delay after displaying some content and then moving on to the next section of the game This allows time for users / players to read instructions or feedback.
    - "OS" to clear terminal.
    - "Termcolor" has been used to just add a splash of color to the otherwise black and white screen.
- I have used global variables mainly, as they relate in different functions.

[Back to Table of Contents](#table-of-contents)
---

## TESTING
---

### Functionality Testing

- Each piece of code was tested in Gitpod as well as in Python Tutor (where possible).
- Family members and friends were asked to test the app once the final product was deployed. 

### Solved Bugs

1. There was no pause after the error messages were showing up and the grid came on next with the input request. I thought that there is a bug. "No error messages were popping up when a wrong input is given for the game." In reality, there was nothing to slow down the function in my code to show the error before showing the next grid.
For this, I used the time.sleep function after the message and that actually showed the messages before the next grid came up. This gave a more realistic approach to the game, as the player could see what has happened before the next grid came up.

2. Terminal syntax error for global values of all variables in the play_game function. I had also defined 2 global values with some data. This was what resulted in the error as below. 

![Terminal syntax error](https://github.com/manasi1031/minesweeper/blob/main/assets/images/terminal-syntaxerror.jpg)

To avoid this error, I removed the values defined, as I had already defined them later again and just added the list of my global variables required. This stopped the error and played the game.

3. Heroku Deployment Error

![Heroku Deployment error](https://github.com/manasi1031/minesweeper/blob/main/assets/images/deployment-error.jpg)

To resolve the issue, I added "six" module to the requirements.txt as recommended by Slackers and by CI Tutor. Once I pushed this and re-deployed on heroku, the app worked well.

- The player name does not append to googlespreadsheet and this was not recording data to my spreadsheet or giving me the player number on my list. I spent a lot of time trying to read material online but was unsuccessful. To resolve this I finally had assistance from my mentor and we did the following steps:
    - Removed "str" from this line "name = input("Enter the player name:\n")"
    - In player name function, also added a "return name" to give the name result for using it in next functions.
    - In the play game function, we changed the calling of the previous functions to below:
        player_name = players_name()
        update_sheet(player_name)

4. When I added the end_game function, the option to exit worked well, but the option to restart was not working at all. 
Originally I had used if __name__ == "__main__" for the final game function, as I was reading through some material online and thought this was a good fit. But with the end_game function this did not work well as I could not call this function from my end_game function.
For this, I changed the main game function to state as "play_game" function and this worked perfectly.


### Remaining Bugs

- No bugs left to resolve.


### Code Validation

The code was checked using [PEP8 Python Validator](http://pep8online.com/) and it did not show any errors.

![Pep8 validator result](https://github.com/manasi1031/minesweeper/blob/main/assets/images/pep8-validator-result.jpg)

[Back to Table of Contents](#table-of-contents)
---

## DEPLOYMENT
---

This project was deployed using Code Institute's mock terminal for Heroku.

- Ensure all the dependencies are included by adding them to the requirements.txt file by running the following command in the terminal: pip3 freeze > requirements.txt.
- Ensure the project has been fully committed and pushed to git.
- Go to your heroku account, if you don't have one create one.
- On the home screen click on the create new app button.
- Enter a name for the project and select your region to the correct region.
- On the next screen select settings.
- Go to config vars and click reveal config vars.
- Switch to the program file and where you are keeping your credentials copy these and then on heroku enter a name for the key (CREDS) and paste the code into the config vars value box and click add.
- Now scroll down to buildPacks and click add build packs.
- First select python and click save changes.
- Click back into build packs and choose node.js and click save again.
- Ensure that the Python build pack is at the top of the list you are abe to drag and drop if you need to rearrange.
- Now select deploy.
- From the deployment method select GitHub.
- Then click on the connect to github button that appears.
- Click into the search box and search for the project name.
- Once located select connect.
- Then click deploy branch, this will then be shown in the box below.
- You can the click view to show the app in a browser.
- The program can be deployed automatically, but I have chosen to keep it as a manual deploy so i can ensure that while I am testing and maybe adding more to the code currently it is better to deploy it manually meaning returning to the screen and clicking deploy branch each time you want to make any changes. (My mentor also suggested to keep on a manual deploy for the project)

How to clone a github repository?

- On GitHub go to the main page of the Repository.
- Above the list of files click the code button with the drop-down arrow.
- To clone the repository using HTTPS, under "Clone with HTTPS", click on the clipboard.
- Open the Git Bash terminal.
- Change the current working directory to the location where you want the cloned directory.
- Type git clone, and then paste the URL you copied earlier from step 3.
- Press Enter to create your local clone.

[Back to Table of Contents](#table-of-contents)
---

## CREDITS
---

1. I have used the time.sleep() function to show messages and hold it before showing grid again. This was to give some pause for the player to read instructions or feedback. The link I used was - [time.sleep function](https://realpython.com/python-sleep/#adding-a-python-sleep-call-with-timesleep)

2. Python recursive function usage or understanding notes taken from the below link: [Recursive function in Python](https://www.programiz.com/python-programming/recursion#:~:text=Recursive%20Function%20in%20Python%20Following%20is%20an%20example,%28denoted%20as%206%21%29%20is%201%2A2%2A3%2A4%2A5%2A6%20%3D%20720.%20)

3. I have used termcolor cprint usage options by reading this page for examples of how to use to give some color to the page - [How to use termcolor in Python](https://www.programcreek.com/python/example/60805/termcolor.cprint)

4. I have used the link from Wikipedia show show people what minesweeper is in general - [Minesweeper Wikipedia link](https://en.wikipedia.org/wiki/Minesweeper_(video_game))

5. I have used the used this as a study or guide to help me with creating and understanding the way to proceed with my minesweeper game - [How to program minesweeper in Python](https://replit.com/talk/learn/How-to-program-MineSweeper-in-Python-fully-explained-in-depth-tutorial/9397)

6. I had to used the Code Institute Love Sandwiches project as an instruction manual when adding library / modules and finally deploying to Heroku.

7. Reference material when using the If __name__ == ‘__main__’- [If __name__ == ‘__main__’: What Does It Mean in Python?](https://codefather.tech/blog/if-name-main-python/)


[Back to Table of Contents](#table-of-contents)
---


## ACKNOWLEDGEMENTS
---
I could not have done this project without the guidance and confidence of my mentor - Adegbenga Adeye.

Last but not the least, I would like to thank [Code Institute](https://codeinstitute.net/) for their support.

[Back to Table of Contents](#table-of-contents)
---

