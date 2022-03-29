import random
# import rich use colours in CLI 
word_list = ['ace', 'act', 'age', 'ago', 'air', 'ale', 'all', 'amp', 'and', 'ant', 'any', 'ape', 'app', 'are', 'ark', 'arm', 'ash', 'ask', 'ate', 'awe', 'axe', 'bad', 'bag', 'bap', 'bat', 'bay', 'bed', 'bee', 'beg', 'bet', 'big', 'bin', 'bit', 'bob', 'bog', 'bop', 'bow', 'box', 'boy', 'bra', 'bud', 'bug', 'bum', 'bun', 'bus', 'but', 'buy', 'bye', 'cab', 'cap', 'can', 'car', 'cat', 'cob', 'cop', 'cow', 'cry', 'cub', 'cut', 'dab', 'dad', 'dam', 'day', 'den', 'did', 'dip', 'doe', 'dog', 'dot', 'dry', 'due', 'dug', 'ear', 'eat', 'egg', 'elf', 'elk', 'end', 'eye', 'fan', 'far', 'fat', 'fee', 'few', 'fig', 'fin', 'fit', 'fix', 'fly', 'foe', 'fog', 'for', 'fox', 'fry', 'fun', 'gap', 'gas', 'gay', 'gel', 'get', 'god', 'got', 'had', 'hag', 'ham', 'has', 'hat', 'hay', 'hen', 'her', 'hex', 'hid', 'him', 'hip', 'his', 'hit', 'hob', 'hoe', 'hop', 'how', 'hub', 'hug', 'hut', 'ice', 'ill', 'ink', 'jab', 'jam', 'jar', 'jaw', 'jet', 'job', 'jog', 'jug', 'jut', 'key', 'kid', 'kin', 'kit', 'lab', 'lag', 'lap', 'law', 'lay', 'leg', 'let', 'lid', 'lie', 'lip', 'lit', 'lob', 'lot', 'low', 'mad', 'man', 'map', 'mat', 'may', 'men', 'met', 'mew', 'mix', 'mob', 'mom', 'mop', 'mow', 'mud', 'mug', 'mum', 'nag', 'nap', 'net', 'new', 'nod', 'not', 'now', 'nut', 'oaf', 'oar', 'odd', 'oil', 'old', 'one', 'our', 'out', 'owe', 'owl', 'own', 'pad', 'pal', 'pan', 'par', 'pat', 'paw', 'pay', 'pea', 'peg', 'pen', 'pet', 'pie', 'pig', 'pin', 'pit', 'pop', 'pot', 'pox', 'pup', 'put', 'rag', 'ram', 'rap', 'rat', 'ray', 'rod', 'row', 'rub', 'rug', 'run', 'sap', 'sat', 'saw', 'say', 'see', 'set', 'sew', 'sir', 'sin', 'sit', 'sob', 'son', 'sow', 'tag', 'tan', 'tap', 'tea', 'ten', 'the', 'tie', 'tip', 'toe', 'ton', 'top', 'tow', 'tub', 'tug', 'two', 'use', 'van', 'vat', 'vet', 'vex', 'wad', 'war', 'was', 'wax', 'way', 'wet', 'who', 'why', 'wig', 'win', 'wit', 'won', 'wow', 'yak', 'yes', 'yet', 'you', 'zap', 'zip', 'zoo']


class Game:
    """
    Game class
    """
    def __init__(self, size, word, guess, guesscount):
        self.size = size
        self.word = word
        self.guess = guess
        self.guesscount = guesscount
    
    def compare_input(word, guess):
        """
        Compares user input with the random word generated from the list. 
        Finds position-dependent letter matches and feeds back to user
        """
        correct_position_guesses = [i for i, j in zip(word, guess) if i == j]
        print(f'Letters {correct_position_guesses} in the correct position')
        incorrect_position_guesses = (set(word) & set(guess)) - set(correct_position_guesses)
        print(f'Letters {incorrect_position_guesses} somewhere in word')
        incorrect_guesses = set(guess) - set(word)
        print(f'{incorrect_guesses} not in the word')
    
    def description(self):
        """
        Describes the game
        """
        return f'{self.guesscount} guesses made.'

def launch_game():
    """
    Launches new instance of Game class
    """
    print('launching game!')
    chosen_word = random.choice(word_list)
    new_game = Game(3, chosen_word, '', 0)
    print(new_game.description())
    print(chosen_word)
    return chosen_word

def get_user_input():
    """
    Prompts user to submit guess in terminal
    Triggered on initial game launch and after invalid guesses
    """
    while True:
        print('Guess a 3 letter word')
        guess = input('Make your guess here: ')
        
        if check_valid_input(guess):
            print('Guess made')

            break

    return guess

def check_valid_input(user_guess):
    """
    Checks whether user input is a valid word in the word_list list
    """
    try:
        if user_guess not in word_list:
            raise ValueError(
            f'Your guess {user_guess} was not in the word list'
            )
    except ValueError as e:
       print(f"{e}, please try again.\n")
       return False

    return True



def main():
    chosen_word = launch_game()
    user_guess = get_user_input()
    comparison = Game.compare_input(chosen_word, user_guess)
    

main()