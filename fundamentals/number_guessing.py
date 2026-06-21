from curses.ascii import isdigit
import random

lowestNum = 1
highestNum = 100
answer = random.randint(lowestNum, highestNum)
guesses = 0
isRunning = True

print("Python Number Guessing Game")
print(f"Select a number between {lowestNum} and {highestNum}")

while isRunning:
    guess = input("Enter you guess: ").strip()
    if guess.isdigit():
        guess =  int(guess)
        guesses += 1

        if guess < lowestNum or guess > highestNum:
            print("That number is out of range.")
            print(f"Please select a number between {lowestNum} and {highestNum}")
        elif guess < answer:
            print("Too low! Try Again!")
        elif guess > answer:
            print("Too high! Try Again!")
        else:
            print(f"CORRECT! The answer was {guess}!")
            print(f"Number of guesses: {guesses}")
            isRunning = False
        print()
    else:
        print("Invalid guess!")
        print(f"Please select a number between {lowestNum} and {highestNum}")