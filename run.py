import random
word_list = ['and', 'fix', 'own', 'are', 'fly', 'odd', 'ape', 'fry', 'our', 'ace', 'for', 'pet', 'act', 'got', 'pat', 'ask', 'get', 'peg', 'arm', 'god', 'paw', 'age', 'gel', 'pup', 'ago', 'gas', 'pit', 'air', 'hat', 'put', 'ate', 'hit', 'pot', 'all', 'has', 'pop', 'but', 'had', 'pin', 'bye', 'how', 'ham', 'rat', 'bad', 'her', 'rag', 'big', 'his', 'rub', 'bed', 'hen', 'row', 'bat', 'ink', 'rug', 'boy', 'ice', 'run', 'bus', 'ill', 'rap', 'bag', 'jab', 'ram', 'box', 'jug', 'sow', 'bit', 'jet', 'see', 'bee', 'jam', 'saw', 'buy', 'jar', 'set', 'bun', 'job', 'sit', 'cub', 'jog', 'sir', 'cat', 'kit', 'sat', 'car', 'key', 'sob', 'cut', 'lot', 'tap', 'cow', 'lit', 'tip', 'cry', 'let', 'top', 'cab', 'lay', 'tug', 'can', 'mat', 'tow', 'dad', 'man', 'toe', 'dab', 'mad', 'tan', 'dam', 'mug', 'ten', 'did', 'mix', 'two', 'dug', 'map', 'use', 'den', 'mum', 'van', 'dot', 'mud', 'vet', 'dip', 'mom', 'was', 'day', 'may', 'wet', 'ear', 'met', 'win', 'eye', 'net', 'won', 'eat', 'new', 'wig', 'end', 'nap', 'war', 'elf', 'now', 'why', 'egg', 'nod', 'who', 'far', 'net', 'way', 'fat', 'not', 'wow', 'few', 'nut', 'you', 'fan', 'oar', 'yes', 'fun', 'one', 'yak', 'fit', 'out', 'yet', 'fin', 'owl', 'zip', 'fox', 'old', 'zap']


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
        user_guess = input('Make your guess here')
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


launch_game()
get_user_input()

#def compare_input():
    # [i for i, j in zip(a, b) if i == j] from stack overflow https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
# checks if letter is in correct position


#def main():
    #runs the game, generating random word from list as goal word by calling an instance of the class Word
    #checks that user input is valid - is a word on the word-pool list
    #indexes across user guess, splitting it into string
    


