import random
# import rich use colours in CLI 
word_list = ['ace', 'act', 'add', 'age', 'ago', 'air', 'ale', 'all', 'amp', 'and', 'ant', 'any', 'ape', 'app', 'are', 'ark', 'arm', 'ash', 'ask', 'ate', 'awe', 'axe', 'bad', 'bag', 'ban', 'bap', 'bar', 'bat', 'bay', 'bed', 'bee', 'beg', 'bet', 'big', 'bin', 'bit', 'bob', 'bog', 'bop', 'bow', 'box', 'boy', 'bra', 'bud', 'bug', 'bum', 'bun', 'bus', 'but', 'buy', 'bye', 'cab', 'cap', 'can', 'car', 'cat', 'cob', 'cop', 'cow', 'cry', 'cub', 'cut', 'dab', 'dad', 'dam', 'day', 'den', 'dew', 'did', 'die', 'dig', 'dim', 'dip', 'doe', 'dog', 'dot', 'dry', 'due', 'dug', 'dye', 'ear', 'eat', 'eel', 'egg', 'elf', 'elk', 'end', 'eye', 'fan', 'far', 'fat', 'fee', 'few', 'fig', 'fin', 'fit', 'fix', 'fly', 'foe', 'fog', 'for', 'fox', 'fry', 'fun', 'gap', 'gas', 'gay', 'gel', 'get', 'god', 'got', 'had', 'hag', 'ham', 'has', 'hat', 'hay', 'hen', 'her', 'hex', 'hid', 'him', 'hip', 'his', 'hit', 'hob', 'hoe', 'hop', 'how', 'hub', 'hug', 'hut', 'ice', 'ill', 'ink', 'jab', 'jam', 'jar', 'jaw', 'jet', 'job', 'jog', 'jug', 'jut', 'key', 'kid', 'kin', 'kit', 'lab', 'lag', 'lap', 'law', 'lay', 'leg', 'let', 'lid', 'lie', 'lip', 'lit', 'lob', 'lot', 'low', 'lye', 'mad', 'man', 'map', 'mat', 'may', 'men', 'met', 'mew', 'mix', 'mob', 'mom', 'mop', 'mow', 'mud', 'mug', 'mum', 'nag', 'nap', 'net', 'new', 'nip', 'nod', 'not', 'now', 'nut', 'oaf', 'oar', 'odd', 'oil', 'old', 'one', 'our', 'out', 'owe', 'owl', 'own', 'pad', 'pal', 'pan', 'par', 'pat', 'paw', 'pay', 'pea', 'peg', 'pen', 'pet', 'pie', 'pig', 'pin', 'pit', 'pop', 'pot', 'pox', 'pry', 'pup', 'put', 'rag', 'ram', 'rap', 'rat', 'raw', 'ray', 'red', 'rob', 'rod', 'rot', 'row', 'rub', 'rug', 'rum', 'run', 'rut', 'sad', 'sag', 'sap', 'sat', 'saw', 'say', 'see', 'set', 'sew', 'sir', 'sin', 'sip', 'sit', 'six', 'sob', 'son', 'sow', 'tag', 'tan', 'tap', 'tax', 'tea', 'ten', 'the', 'tie', 'tin', 'tip', 'toe', 'ton', 'top', 'tow', 'toy', 'tub', 'tug', 'two', 'use', 'van', 'vat', 'vet', 'vex', 'wad', 'war', 'was', 'wax', 'way', 'wet', 'who', 'why', 'wig', 'win', 'wit', 'won', 'wow', 'yak', 'yes', 'yet', 'you', 'zap', 'zip', 'zoo']


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
            print(f'Congratulations, {guess} is the correct answer')
            return 
        correct_guesses = [i for i, j in zip(word, guess) if i == j]
        if correct_guesses:
            print(f'Letters {correct_guesses} in the correct position')
        incorrect_position_guesses = (set(word) & set(guess)) - set(correct_guesses)
        if incorrect_position_guesses:
            print(f'Letters {incorrect_position_guesses} somewhere in word')
        incorrect_guesses = set(guess) - set(word)
        if incorrect_guesses:
            print(f'{incorrect_guesses} not in the word')

    def store_guess(self, guess):
        """
        Stores user guesses in guesses class attribute, counting it to check guess count
        """
        self.guesses.append(guess)
        print(f'{len(self.guesses)} guesses made')


def select_word():
    """
    Selects random word from global variable list
    """
    chosen_word = random.choice(word_list)
    print(chosen_word)
    return chosen_word


def get_user_input():
    """
    Prompts user to submit guess in terminal
    Triggered on initial game launch and after incorrect or invalid guesses
    """
    while True:
        print('Guess a 3 letter word')
        user_input = input('Make your guess here: ')

        if check_valid_input(user_input):
            print('Guess made')
            return user_input


def check_valid_input(user_input):
    """
    Checks whether user input is a valid word in the word_list list
    """
    try:
        if user_input not in word_list:
            raise ValueError(f'Your guess {user_input} was not in word list')
    except ValueError as e:
        print(f"{e}, please try again.\n")
        return False

    return True


def main():
    """
    The main function that runs the word guessing game.
    """
    generated_word = select_word()
    new_game = Game(3, generated_word, '')
    while True:
        latest_guess = get_user_input()
        new_game.compare_input(generated_word, latest_guess)
        new_game.store_guess(latest_guess)


main()