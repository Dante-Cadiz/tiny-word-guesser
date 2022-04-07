import random
from rich.console import Console
from rich.table import Table
console = Console()


class Game:
    """
    Game class
    """
    def __init__(self, word, guess, table):
        self.word = word
        self.guess = guess
        self.guesses = []
        self.table = table

    def build_table(self):
        table = Table()
        table.add_column()
        return table

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

    def store_guess(self, guess, table):
        """
        Stores user guesses in guesses class attribute, counting it to check guess count
        """
        table.add_row(guess)
        console.print(table)
        self.guesses.append(guess)
        console.print(f'{len(self.guesses)} guesses made')

def select_word():
    """
    Selects random word from global variable list
    """
    with open('answerset.txt', 'rt') as answer_dataset:
        word_list = [line.rstrip() for line in answer_dataset]
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
    try:
        with open('possibleguesses.txt', 'rt') as guess_dataset:
            possible_guesses = [line.rstrip() for line in guess_dataset]
            return possible_guesses
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
    new_game = Game(generated_word, '', '')
    new_table = new_game.build_table()
    while True:
        latest_guess = get_user_input()
        new_game.compare_input(generated_word, latest_guess)
        new_game.store_guess(latest_guess, new_table)

        if generated_word == latest_guess:
            return False


main()