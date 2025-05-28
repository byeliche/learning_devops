import random

secret_number = random.randint(0, 100)
guess = 0
guesses = 0
while guess != secret_number:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess < secret_number:
        print("Too low! Try again.")
        guesses += 1
    elif guess > secret_number:
        print("Too high! Try again.")
        guesses += 1
    else:
        print("Congratulations! You guessed the number!")
        guesses += 1

print("The secret number was", secret_number)
print("You guessed", guesses, "times.")