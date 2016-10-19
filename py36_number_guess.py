# number_guess.py
# created by Neal Miller

import random
import os

answer = random.randint(1, 100)
count = 0
lowest = 0
highest = 101
os.system('clear')
print(f'Guess a number between {lowest} and {highest}.')
while True:
    try:
        guess = int(input())
        break
    except ValueError:
        print('Numbers only. Try again.')
        continue
if answer == guess:
    print('Wow! You got it on the first try!')
else:
    while count >= 0:
        count += 1
        if answer < guess:
            if guess < highest:
                highest = guess
            os.system('clear')
            print(f"Lower, between {lowest} and {highest}.\nThat's {count} guess(es) so far")
        if answer > guess:
            if guess > lowest:
                lowest = guess
            os.system('clear')
            print(f"Higher, between {lowest} and {highest}.\nThat's {count} guess(es) so far.")
        if answer == guess:
            os.system('clear')
            print(f"Correct! It took you {count} guesses.")
            break
        print('Guess again.')
        while True:
            try:
                guess = int(input())
                break
            except ValueError:
                print('Numbers only. Try again.')
                continue

