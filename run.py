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
        self.guesslist = []
        self.table = table
        self.incorrect_set = set()

    def build_table(self):
        """
        Builds the table displayed to the user in terminal
        """
        table = Table(show_lines=True, show_header=False)
        table.add_column()
        return table

    def select_word(self):
        """
        Selects random word from global variable list
        """
        with open('answerset.txt', 'rt') as answer_dataset:
            word_list = [line.rstrip() for line in answer_dataset]
        chosen_word = random.choice(word_list)
        return chosen_word

    def get_user_input(self, guesslist):
        """
        Prompts user to submit guess in terminal.
        Triggered on initial game launch and after incorrect/invalid guesses.
        """
        while True:
            console.print('Guess a 5 letter word.')
            user_input = console.input('Make your guess here:\n')

            if self.check_valid_input(user_input, guesslist):
                console.print('Guess made')
                break

        return user_input

    def check_valid_input(self, guess, guesslist):
        """
        Checks whether user input is a valid word in the word_list list
        """
        try:
            with open('possibleguesses.txt') as guess_dataset:
                possible_guesses = [line.rstrip() for line in guess_dataset]
            if guess not in possible_guesses:
                raise ValueError(f'Your guess {guess} was invalid')
            if guess in guesslist:
                raise ValueError(f'You already guessed {guess}')
        except ValueError as wrong_entry:
            console.print(f"{wrong_entry}, please try again.\n")
            return False

        return True

    def compare_input(self, word, guess):
        """
        Compares user input with the random word generated from the list.
        Finds position-dependent letter matches and feeds back to user
        """
        if word == guess:
            console.print(f'Congratulations, {guess} is the correct answer')
            return
        correct = [i for i, j in zip(word, guess) if i == j]
        if correct:
            console.print(
                f'Letters [green]{correct}[/green] in the correct position')
        incorrect_position = (set(word) & set(guess)) - set(correct)
        if incorrect_position:
            console.print(
                f'Letters [red]{incorrect_position}[/red] somewhere in word')
        incorrect_guesses = set(guess) - set(word)
        if incorrect_guesses:
            for i in incorrect_guesses:
                self.incorrect_set.add(i)
            console.print(
                f'[yellow]{self.incorrect_set}[/yellow] not in the word')

    def store_guess(self, guess, guesslist, table):
        """
        Stores user guesses in guesslist class attribute.
        Prints table of guesses to terminal.
        """
        table.add_row(guess)
        console.print(table)
        guesslist.append(guess)
        console.print(f'{len(guesslist)} guesses made')


def print_instructions():
    """
    Prints instructions for playing the game to the user.
    """
    INSTRUCTIONS = """
    [purple]Welcome to Tiny Word Guesser![/purple]
    Use your deduction to guess a 5 letter word.
    After each guess, you will see how the letters
    in your guess compare to the answer.
    Guesses need to be in lower case.
    You have 6 attempts to get the correct answer.
    4 is good, 3 is impressive!
    """
    console.print(INSTRUCTIONS)


def main():
    """
    The main function that runs the word guessing game.
    """
    print_instructions()
    new_game = Game('', '', '')
    generated_word = new_game.select_word()
    new_table = new_game.build_table()
    new_guesslist = new_game.guesslist
    while True:
        latest_guess = new_game.get_user_input(new_guesslist)
        new_game.compare_input(generated_word, latest_guess)
        new_game.store_guess(latest_guess, new_guesslist, new_table)

        if generated_word == latest_guess:
            return False

        if len(new_guesslist) == 6:
            console.print(f'All attempts used. {generated_word} was the word.')
            return False


if __name__ == "__main__":
    main()
