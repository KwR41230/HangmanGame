import random
import requests

response = requests.get('https://random-word-api.herokuapp.com/word')
word = response.json()[0]

# Limit the word length to 5 characters
if len(word) <= 5:
    print(word)
else:
    # If the word is too long, get a new one
    while len(word) > 5:
        response = requests.get("https://random-word-api.herokuapp.com/word")
        word = response.json()[0]
    #print(word)
# List of words to choose from
#words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Choose a random word from the list
#random_word = random.choice(words)

# Initialize the hangman figure
hangman_figure = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========""",
]

# Initialize the word with underscores
word_with_underscores = ['_'] * len(word)

# Initialize the number of incorrect guesses
incorrect_guesses = 0


print(r'''
__        __   _                            _____     
\ \      / /__| | ___ ___  _ __ ___   ___  |_   _|__  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) |
 _ \_/\_/ \___|_|\___\___/|_| |_| |_|\___|   |_|\___/ 
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __ | |     
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \| |     
|  _  | (_| | | | | (_| | | | | | | (_| | | | |_|     
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_(_)     
                   |___/                              
''')
print()
print(" " * 30 + hangman_figure[0])
print()

used_letters = []
def add_used_letter(guess):
    used_letters.append(guess.upper())

while '_' in word_with_underscores and incorrect_guesses < len(hangman_figure) - 1:
    # Ask the user for a guess
    print()
    guess = input("Guess a letter: ").lower()
    print()

    # Check if the guess is in the used letters
    if guess.upper() in used_letters:
        print("You already guessed that letter. Try again.")
        print()
        print("Used Letters: ", used_letters)
        print()
    else:
        # Add the guess to the list of used letters
        add_used_letter(guess)
        print()
        print("Used Letters: ", used_letters)
        print()

        # Check if the guess is in the word
        if guess in word:
            # Replace the underscores with the correct letter
            for i in range(len(word)):
                if word[i] == guess:
                    word_with_underscores[i] = guess
        else:
            # Increment the number of incorrect guesses
            incorrect_guesses += 1

    # Print the current state of the word and the hangman figure
    print(' '.join(word_with_underscores))
    print(hangman_figure[incorrect_guesses])


# Check if the user won or lost
if '_' not in word_with_underscores:
    print("Congratulations, you won! The word was " + word.upper()+'!')
else:
    print("Sorry, you lost. The word was " + word.upper()+'!')