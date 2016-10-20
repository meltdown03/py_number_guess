# number_guess.py
# created by Neal Miller

import random
import os

count = 0
os.system('clear')
while True:    
    try:
        print('Select the low number:')
        lowest = int(input())
        print('Select the high number:')
        highest = int(input())
        if highest <= lowest:
            os.system('clear')
            print('High number must be greater than the low number.')
            continue
        break
    except ValueError:
        os.system('clear')
        print('Numbers only, try again.')
        continue
os.system('clear')
answer = random.randint(lowest, highest)
print(f'Guess a number from {lowest} to {highest}.')
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

