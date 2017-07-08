#!/usr/bin/env python
# -*- coding: utf-8 -*-

# py_number_guess.py
# created by Neal Miller

import random
import os

os.system('clear')
#  User selects starting range
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
    except NameError:
        os.system('clear')
        print('Numbers only, try again.')
        continue
os.system('clear')
answer = random.randint(lowest, highest)     # random int is set
count = 0
os.system('clear')
print('Guess a number from {} to {}.'.format(lowest, highest))
while True:
    try:
        guess = int(input())
        break
    except NameError:
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
            print("Lower, guess from {} to {}.\nThat's {} guess(es) so far".format(lowest, highest, count))
        if answer > guess:
            if guess >= lowest:
                lowest = (guess + 1)
            os.system('clear')
            print("Higher, guess from {} to {}.\nThat's {} guess(es) so far.".format(lowest, highest, count))
        if answer == guess:
            os.system('clear')
            print("Correct! It took you {} guesses.".format(count))
            break
        print('Guess again.')
        while True:
            try:
                guess = int(input())
                break
            except NameError:
                print('Numbers only. Try again.')
                continue
