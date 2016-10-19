# number_guess.py
# created by Neal Miller

import random
import os

answer = random.randint(1, 100)
count = 0
lowest = 0
highest = 101
os.system('clear')
print('Guess a number between {} and {}.'.format(lowest, highest))
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
            if guess < highest:
                highest = guess
            os.system('clear')
            print("Lower, between {} and {}.\nThat's {} guess(es) so far".format(lowest, highest, count))
        if answer > guess:
            if guess > lowest:
                lowest = guess
            os.system('clear')
            print("Higher, between {} and {}.\nThat's {} guess(es) so far.".format(lowest, highest, count))
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

