import random
word_list = ['ace', 'act', 'age', 'ago', 'air', 'ale', 'all', 'and', 'ape', 'app', 'are', 'ark', 'arm', 'ash', 'ask', 'ate', 'bad', 'bag', 'bat', 'bay', 'bed', 'bee', 'bet', 'big', 'bin', 'bit', 'bob', 'bog', 'bop', 'box', 'boy', 'bra', 'bum', 'bun', 'bus', 'but', 'buy', 'bye', 'cab', 'cap', 'can', 'car', 'cat', 'cop', 'cow', 'cry', 'cub', 'cut', 'dab', 'dad', 'dam', 'day', 'den', 'did', 'dip', 'doe', 'dog', 'dot', 'due', 'dug', 'ear', 'eat', 'egg', 'elf', 'elk', 'end', 'eye', 'fan', 'far', 'fat', 'fee', 'few', 'fig', 'fin', 'fit', 'fix', 'fly', 'foe', 'fog', 'for', 'fox', 'fry', 'fun', 'gap', 'gas', 'gay', 'gel', 'get', 'god', 'got', 'had', 'ham', 'has', 'hat', 'hen', 'her', 'hex', 'him', 'hip', 'his', 'hit', 'hoe', 'how', 'ice', 'ill', 'ink', 'jab', 'jam', 'jar', 'jet', 'job', 'jog', 'jug', 'key', 'kit', 'lay', 'leg', 'let', 'lie', 'lip', 'lit', 'lob', 'lot', 'mad', 'man', 'map', 'mat', 'may', 'met', 'mew', 'mix', 'mom', 'mud', 'mug', 'mum', 'nap', 'net', 'net', 'new', 'nod', 'not', 'now', 'nut', 'oaf', 'oar', 'odd', 'oil', 'old', 'one', 'our', 'out', 'owl', 'own', 'pat', 'paw', 'peg', 'pet', 'pin', 'pit', 'pop', 'pot', 'pup', 'put', 'rag', 'ram', 'rap', 'rat', 'row', 'rub', 'rug', 'run', 'sat', 'saw', 'see', 'set', 'sir', 'sit', 'sob', 'sow', 'tan', 'tap', 'tea', 'ten', 'the', 'tip', 'toe', 'top', 'tow', 'tub', 'tug', 'two', 'use', 'van', 'vat', 'vet', 'war', 'was', 'way', 'wet', 'who', 'why', 'wig', 'win', 'won', 'wow', 'yak', 'yes', 'yet', 'you', 'zap', 'zip']


class Game:
    """
    Game class
    """
    def __init__(self, size, word, guess, guesscount):
        self.size = size
        self.word = word
        self.guess = guess
        self.guesscount = guesscount
    
    def description(self):
        """
        Describes the game
        """
        return f'Word {self.size} letters long. {self.guesscount} guesses made.'

def launch_game():
    """
    Launches new instance of Game class
    """
    print('launching game!')
    chosen_word = random.choice(word_list)
    index = [char for char in chosen_word]
    new_game = Game(3, index, '', 0)
    print(new_game.description())

def get_user_input():
    while True:
        print('Guess a 3 letter word')
        user_guess = input('Make your guess here: ')
        user_guess_letters = user_guess.split()
        
        if check_valid_input(user_guess):
            print('Guess made')
            break

    return user_guess_letters

def check_valid_input(guessed_word):
    try:
        if guessed_word not in word_list:
            raise ValueError(
            f'Your guess {guessed_word} was not in the word list'
            )
    except ValueError as e:
       print(f"Invalid data: {e}, please try again.\n")
       return False

    return True

def compare_input(word_list, ):
    # [i for i, j in zip(a, b) if i == j] from stack overflow https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
# checks if letter is in correct position


#def main():
    #runs the game, generating random word from list as goal word by calling an instance of the class Word
    #checks that user input is valid - is a word on the word-pool list
    #indexes across user guess, splitting it into string
    


launch_game()
get_user_input()


