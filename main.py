import random


def load_words(filename="words.txt"):
    difficulties = {'easy':[], 'medium':[], 'hard':[]}
    current_level = None
    try:
        with open(filename,'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('#'):
                    current_level = line[1:].lower()
                elif line and current_level in difficulties:
                    difficulties[current_level].append(line.lower())
    except FileNotFoundError:
        print("File not found")
        exit()
    return difficulties
def choose_difficulty():
    while True:
        choice = input("Choose difficulty (easy / medium / hard): ").lower()
        if choice in ['easy', 'medium', 'hard']:
            return choice
        else:
            print("Choose a valid difficulty")
def choose_word(words_dict,difficulty):
    return random.choice(words_dict[difficulty])
def display_word(word,guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])
def get_guess(guessed_letters, word_length):
    while True:
        guess = input("Guess a letter or the full word: ").lower()
        if guess.isalpha():
            if len(guess) == 1:
                if guess in guessed_letters:
                    print("Already guessed that letter.")
                else:
                    return guess
            elif len(guess) == word_length:
                return guess
            else:
                print(f"Enter a single letter or a {word_length}-letter word.")
        else:
            print("Only letters allowed.")


def play_game():
    words_dict = load_words()
    difficulties = choose_difficulty()
    word=choose_word(words_dict,difficulties)
    guessed_letters=[]
    incorrect_guesses=0
    if difficulties == "easy":
        max_attempts=8
    if difficulties == "medium":
        max_attempts=6
    if difficulties == "hard":
        max_attempts=4
    stages = [
        '''
         +---+
         |   |
             |
             |
             |
             |
        =========''',  # 0 incorrect
        '''
         +---+
         |   |
         O   |
             |
             |
             |
        =========''',  # 1 incorrect
        '''
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========''',  # 2 incorrect
        '''
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========''',  # 3 incorrect
        '''
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========''',  # 4 incorrect
        '''
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========''',  # 5 incorrect
        '''
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========''', # 6 incorrect
        '''
                 +---+
                 |   |
                 O   |
                /|\\  |
               // \\  |
                     |
                =========''', # 7 incorrect
        '''
                +---+
                |   |
                O   |
              //|\\  |
              // \\  |
                     |
                =========''', # 8 incorrect
    ]
    print("\nWelcome to Hangman!")
    while True:
        print(stages[incorrect_guesses])
        print("\n" + display_word(word, guessed_letters))
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        print(f"Remaining attempts: {max_attempts-incorrect_guesses}")

        guess = get_guess(guessed_letters, len(word))
        if len(guess) == 1:
            guessed_letters.append(guess)
            if guess in word:
                print("Good Guess")
            else:
                incorrect_guesses += 1
                print(f"Wrong guess :( , remaining guesses: {max_attempts - incorrect_guesses}")
        else:
            if guess == word:
                print(f"You Win! You guessed the word: {word}")
                break
            else:
                incorrect_guesses += 1
                print(f"Wrong full word guess :( , remaining guesses: {max_attempts - incorrect_guesses}")
        if all(letter in guessed_letters for letter in word):
            print(f"You Win! The word was: {word}")
            break
        if incorrect_guesses >= max_attempts:
            print(f"You Lose! The word was: {word}")
            break


play_game()
