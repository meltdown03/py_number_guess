#!/usr/bin/env python
# -*- coding: utf-8 -*-

# py36_number_guess.py
# created by Neal Miller

import random
import os

count = 0
os.system('clear')
# User selects starting range
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
    except:
        os.system('clear')
        print('Whole Numbers only, try again.')
        continue
os.system('clear')
answer = random.randint(lowest, highest)    # random int is set
print(f'Guess a number from {lowest} to {highest}.')
while True:
    try:
        guess = int(input())
        break
    except:
        print('Numbers only. Try again.')
        continue
if answer == guess:
    print('Wow! You got it on the first try!')
else:
    while count >= 0:
        count += 1
        if answer < guess:
            if guess <= highest:
                highest = (guess - 1)
            os.system('clear')
            print(f"Lower, guess from {lowest} to {highest}.\nThat's {count} guess(es) so far")
        if answer > guess:
            if guess >= lowest:
                lowest = (guess + 1)
            os.system('clear')
            print(f"Higher, guess from {lowest} to {highest}.\nThat's {count} guess(es) so far.")
        if answer == guess:
            os.system('clear')
            print(f"Correct! It took you {count} guesses.")
            break
        print('Guess again.')
        while True:
            try:
                guess = int(input())
                break
            except:
                print('Numbers only. Try again.')
                continue
