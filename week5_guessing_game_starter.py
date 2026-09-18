"""
CIS 3680 - Week 5: Loops and Iteration
Number Guessing Game - In-Class Practice

This is practice only. Nothing in this file is submitted or graded.
Fill in each ADD THIS line where marked. Everything else already works.
Covers both Monday and Wednesday's class sessions, in order.
"""

# ============================================================
# MONDAY: WHILE LOOPS
# ============================================================

# ----- PROCESS: Count-controlled while loop (the wrong way, on purpose) -----
# Type this exactly as shown. We are about to find out why it's risky.
'''
total = 0
count = 1
while count < 100:
    total += count
    count += 1
print(total)
'''
# ADD THIS: as a comment, write down whether that total looks right
# for "the sum from 1 to 100." Talk to your neighbor before moving on.


# ----- PROCESS: Count-controlled while loop (the correct, deliberate way) -----
# ADD THIS: write the same loop again, but change ONE character so
# count = 100 gets included in the sum. Store the result in a
# variable called total, print it.


# ----- PROCESS: Number Guessing Game, while-loop version -----
# ADD THIS: import the random module


# ADD THIS: set my_number using random.randint(1, 20). Set count to 0.


# ADD THIS: write a while True loop. Each time through: add 1 to
# count, ask the player to guess with input() (convert to int), then
# print "Too small!" if the guess is less than my_number, "Too large!"
# if it's more, or a message using count and break if it's correct.
'''
import random
my_number = random.randint(1, 20)
count = 0
while True:
    count += 1
    guess = int(input('Enter your guess: '))
    if guess < my_number:
        print('Too small!')
    elif guess > my_number:
        print('Too big!')
    elif guess == my_number:
        print(f'Correct! {count} tries.')
        break
'''
# ============================================================
# GUIDED PRACTICE
# ============================================================

# ADD THIS: add one feature to the guessing game using augmented
# assignment (+=) or a while loop of your own. Some ideas:
#   - Count how many guesses were too high vs. too low, using two
#     separate counters.
#   - Add a maximum of 3 wrong guesses before the game gives up and
#     reveals the number.
#   - Let the player choose the number range instead of hardcoding
#     1 to 20.


# ============================================================
# WEDNESDAY: FOR LOOPS - only start this section once everything
# above already runs correctly.
# ============================================================

# ----- PROCESS: Off-by-one error (the wrong way, on purpose) -----
# Type this exactly as shown. We wanted 10 attempts.
'''
print("attempts allowed:")
for attempt in range(1, 10):
    print(attempt, end=" ")
print()
'''
# ADD THIS: as a comment, count how many numbers actually printed.
# Talk to your neighbor before moving on.


# ----- PROCESS: Off-by-one error (the correct, deliberate way) -----
# ADD THIS: write the same loop again, but fix the range() bounds so
# exactly 10 numbers print, 1 through 10.


# ----- PROCESS: Number Guessing Game, extended with a guess limit -----
# ADD THIS: set my_number using random.randint(1, 20) again. Set a
# variable called guessed_correctly to False.


# ADD THIS: write a for loop using range(1, 11) so the player gets
# exactly 10 attempts. Each time through: ask the player to guess
# with input() (convert to int), print "Too small!" or "Too large!"
# as needed, or if correct: print a message using attempt, set
# guessed_correctly to True, and break.


# ADD THIS: after the for loop ends, check if guessed_correctly is
# still False. If so, print a message revealing my_number and saying
# the player ran out of tries.


# ============================================================
# GUIDED PRACTICE
# ============================================================

# ADD THIS: modify the guess-limit version using range(). Some ideas:
#   - Change the number of allowed attempts, and make sure your
#     range() bounds actually match the number you intended.
#   - Print a running list of every guess made so far, using a
#     string you build up across iterations.
#   - Add a for loop that lets the player play the whole game 3
#     times in a row.
import random
my_number = random.randint(1, 21)  # computer picks a number 1-20
games = 0  # number of games
count = 0  # number of guesses
guessed_correctly = False

while guessed_correctly == False:
    for attempt in range(1, 4):
        print(f'Game #{games}')
        guess = int(input(f'Attempt {attempt}: '))  # user guesses the number
        if guess > my_number:
            print('Too large!')
            count += 1
        elif guess < my_number:
            print('Too small!')
            count += 1
        else:
            print(f'Correct! {attempt} tries!')
            guessed_correctly = True
            games += 1
            break

    if not guessed_correctly:
        while games < 3:
            print('Try again!')
            count = 0
        break
            
