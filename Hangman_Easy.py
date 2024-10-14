import random
import time
import os
from colorama import init, Fore, Back, Style

init()


def win_animation():
    print("\n" + Fore.GREEN + "Congratulations, you won!" + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.YELLOW + "Well done!" + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.CYAN + "You guessed the word correctly!" + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.MAGENTA + "Here's a virtual confetti for you:" + Style.RESET_ALL)
    time.sleep(1)


def rainbow_confetti():
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Style.BRIGHT + Fore.RED,
              Style.BRIGHT + Fore.YELLOW, Style.BRIGHT + Fore.GREEN, Style.BRIGHT + Fore.CYAN, Style.BRIGHT + Fore.BLUE,
              Style.BRIGHT + Fore.MAGENTA]

    # Add blank lines to push the animation down
    for _ in range(15):
        print()

    # Firework launch
    for i in range(5):
        print("\033[A" * (5 - i) + " " * 30 + Fore.WHITE + "." + Style.RESET_ALL)
        time.sleep(0.1)

    # Pause before explosion
    time.sleep(0.5)

    # Move cursor up to position explosion above the trail
    print("\033[10A", end="\r")

    # Explosion
    for frame in range(5):
        for y in range(10):
            line = " " * 20
            for x in range(20):
                if random.random() < 0.3 * (5 - frame) / 5:
                    line += random.choice(colors) + random.choice(['*', '+', '.', 'o']) + Style.RESET_ALL
                else:
                    line += " "
            print(line)
        time.sleep(0.4)
        if frame < 4:
            print("\033[10A", end="\r")  # Move cursor up 10 lines

    print(Style.RESET_ALL)


def get_random_word(top_100_nouns):
    with open(top_100_nouns, 'r') as f:
        words = f.readlines()
        return random.choice(words).strip()


random_word = get_random_word('top_100_nouns.txt')
print(random_word)

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
word = random_word
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
max_width = 80  # adjust this value to match your terminal width
hangman_width = max(len(line) for line in hangman_figure[0].split('\n'))
spaces = (max_width - hangman_width) // 2

print("\n" + hangman_figure[0].center(max_width))
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
    win_animation()
    rainbow_confetti()
    # print("\nCongratulations, you won! The word was " + word.upper()+'!\n')
else:
    print("\nSorry, you lost. The word was " + word.upper() + '!\n')