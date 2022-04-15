# Tiny Word Guesser

Tiny Word Guesser is a command line interface version of the popular word guessing game Wordle, following its exact rule set. 
The live and playable version is [here.](https://tinywordguesser.herokuapp.com/)
The GitHub page for the game is [here.](https://github.com/Dante-Cadiz/tiny-word-guesser)

## How to play:

The rules

## Features:

### Random word selection
Each time when played, Tiny Word Guesser selects a random word from a large data set of possible answers held in a .txt file. This word serves as the answer that the user will have to guess.
### User input
The game accepts types user input as guesses. Valid user inputs are then compared to the randomly selected word and indexed for letter matches in both the correct and incorrect positions within the word.
![user input prompt at start of game](https://i.imgur.com/dA0JNr7_d.webp?maxwidth=760&fidelity=grand)
### Guess validator - exception handling
Before accepting user guesses, the game checks them against another large data set of possible guesses (every 5 letter word in the English language). If the user's guess is not in this database, an error message is thrown, the guess is rejected and the user is prompted to resubmit a guess. 
![example of an invalid guess](https://i.imgur.com/ncod1oi.png)
The validator also rejects guesses that the user has already previously submitted.
![example of an already submitted invalid guess](https://i.imgur.com/AkYJHOZ.png)
### Constant user feedback
After comparing the submitted user guess with the answer, the user receives textual feedback detailing how their guess compared to the answer using colour-coded visual prompts. Along with this, each guess is appended to a table created using the external Rich library, and the table is printed in terminal after each attempt.
![gameplay with guesses being appended to table](https://i.imgur.com/n190UsQ.png)








Testing - PEP8online check




## Deployment: 
This application was deployed to Heroku using the following steps:
- Create a new application on Heroku Apps
- Set a config var of key PORT and value 8000
- Set the buildpacks to Python and NodeJS in that order
- Connect the application to the GitHub repository, enabling automatic deploys from the main branch


## Credits:

- The data for both the answer set and possible valid guesses was taken from cfreshman's Github Gists - [possible answer set](https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b) and [valid guess list excluding possible answers](https://gist.github.com/cfreshman/cdcdf777450c5b5301e439061d29694c), which in turn were created from Wordle's original official data set.
- The method for finding exact positional matches was taken from [this StackOverflow answer](https://stackoverflow.com/a/1388836)
- The Heroku-deployed version of this application is built in a mock terminal created by Code Institute.
- I would also like to credit my Code Institute mentor Sandeep Aggarwal for his input and advice during this project.


Potential future features:

Words of different lengths - can choose before playing game
