import random

class Game:
    #"""
    #Game class
    #"""
    def __init__(self, size, word, guess, guesscount):
        self.size = size
        self.word = word
        self.guess = guess
        self.guesscount = guesscount

def launch_game():
    """
    Launches new instance of Game class
    """
    #split = [char for char in word]
    print('launching game!')
    f = open("3letterwords.txt", "r")
    chosen_word = random.choice(f.readlines()).strip()
    index = [char for char in chosen_word]
    new_game = Game(3, index, '', 0)
    return new_game


#def check_valid_input():
   # try:
   # except:

#def compare_input():
    # [i for i, j in zip(a, b) if i == j] from stack overflow https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
# checks if letter is in correct position


def main():
    #runs the game, generating random word from list as goal word by calling an instance of the class Word
    #checks that user input is valid - is a word on the word-pool list
    #indexes across user guess, splitting it into string
     = launch_game()


