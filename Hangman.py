import random
from words import words
from time import sleep
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O' ,'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def hide(word):
    unreveal = {}
    for i in word:
        unreveal[i] = '_'
    return unreveal

def guessing(guessed_letters):
    while True:
        guess = input("Guess the letter: ").upper()
        if guess in letters and guess not in guessed_letters:
            return guess
        elif guess in guessed_letters:
            print(f"You've already guessed the letter {guess}. Try again.")
            sleep(1)
        else:
            print(f"Invalid input. Please enter a valid letter.")
            sleep(1)

def hangman():
    possible_mistakes = 5
    guessed_letters = set()
    word = random.choice(words).upper()
    unreveal = hide(word)
    word_shown = ''.join(unreveal.values())
    #Zgadywanie słowa
    while set(unreveal.keys()) != set(unreveal.values()) and possible_mistakes > 0:
        #print(word) do usunięcia!
        print(word)
        print(word_shown)
        guess = guessing(guessed_letters)
        guessed_letters.add(guess)
    #Literka jest w słowie
        if guess in unreveal.keys():
            unreveal[guess] = guess
            word_shown = ''.join(unreveal.values())
        else:
            print(f"Unfortunately, there is no letter {guess} in the word")
            possible_mistakes -= 1
            sleep(1)
    if possible_mistakes > 0:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"You lost :( The word was: {word}")
hangman()



