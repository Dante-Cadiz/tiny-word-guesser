import random
from rich.console import Console
from rich.table import Table
console = Console()


class Game:
    """
    Game class
    """
    def __init__(self, size, word, guess):
        self.size = size
        self.word = word
        self.guess = guess
        self.guesses = []

    def compare_input(self, word, guess):
        """
        Compares user input with the random word generated from the list. 
        Finds position-dependent letter matches and feeds back to user
        """
        if word == guess:
            console.print(f'Congratulations, {guess} is the correct answer')
            return
        correct_guesses = [i for i, j in zip(word, guess) if i == j]
        if correct_guesses:
            console.print(f'Letters {correct_guesses} in the correct position')
        incorrect_position_guesses = (set(word) & set(guess)) - set(correct_guesses)
        if incorrect_position_guesses:
            console.print(f'Letters {incorrect_position_guesses} somewhere in word')
            #push to list, display list after guesses
        incorrect_guesses = set(guess) - set(word)
        if incorrect_guesses:
            console.print(f'{incorrect_guesses} not in the word')
            #push to list, display list after guesses

    def store_guess(self, size, guess):
        """
        Stores user guesses in guesses class attribute, counting it to check guess count
        """
        table = Table()
        for i in range(size):
            table.add_column('test')
        console.print(table)
        self.guesses.append(guess)
        console.print(f'{len(self.guesses)} guesses made')
        #for guess in guesses print guess


def select_word():
    """
    Selects random word from global variable list
    """
    word_list = open('answerset.txt').read().split("\n")
    chosen_word = random.choice(word_list)
    console.print(chosen_word)
    return chosen_word


def get_user_input():
    """
    Prompts user to submit guess in terminal
    Triggered on initial game launch and after incorrect or invalid guesses
    """
    while True:
        console.print('Guess a 5 letter word')
        user_input = console.input('Make your guess here: ')

        if check_valid_input(user_input):
            console.print('Guess made')
            break
    
    return user_input


def check_valid_input(user_input):
    """
    Checks whether user input is a valid word in the word_list list
    """
    possible_guesses = open('possibleguesses.txt').read().split("\n")
    try:
        if user_input not in possible_guesses:
            raise ValueError(f'Your guess {user_input} was invalid')
    except ValueError as wrong_entry:
        console.print(f"{wrong_entry}, please try again.\n")
        return False

    return True


def main():
    """
    The main function that runs the word guessing game.
    """
    generated_word = select_word()
    new_game = Game(5, generated_word, '')
    while True:
        latest_guess = get_user_input()
        new_game.compare_input(generated_word, latest_guess)
        new_game.store_guess(5, latest_guess)

        if generated_word == latest_guess:
            return False


main()