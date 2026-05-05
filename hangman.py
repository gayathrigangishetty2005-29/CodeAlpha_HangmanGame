import random

words = ["python", "java", "html", "coding", "program"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)

    if "_" not in display_word:
        print("You won! 🎉")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter")
    elif guess in word:
        print("Correct!")
        guessed_letters.append(guess)
    else:
        print("Wrong!")
        attempts -= 1
        print("Attempts left:", attempts)

if attempts == 0:
    print("You lost! The word was:", word)