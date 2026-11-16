import random

words = ["python", "computer", "mango", "college", "grapes"]

secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("===============================")
print("      WELCOME TO HANGMAN       ")
print("===============================")

while incorrect_guesses < max_attempts:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Incorrect guess!")

else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing!")