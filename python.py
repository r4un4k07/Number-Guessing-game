import random
import os

os.system("cls")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a Number between 1 and 100")

num = random.randint(2, 99)

diff = input("Choose difficulty level, 'easy' or 'hard': ")

if diff == "easy":
    attempt = 10
elif diff == "hard":
    attempt = 5

winning = False

while attempt != 0:
    print(f"\nYou have {attempt} attempts remaining.")
    guess = int(input("Make a guess: "))
    if guess > num:
        print("Too High!")
    elif guess < num:
        print("Too Low!")
    elif guess == num:
        winning = True
        break
    attempt -= 1

if winning:
    print("You WIN!")
else:
    print("You LOST!")

print(f"The number I was thinking of was {num}.")