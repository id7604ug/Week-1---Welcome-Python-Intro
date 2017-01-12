# This program is a random number guessing game
import random

print('Can you guess the number 1 to 20?')
randomNumber = random.randrange(1, 20)
guess = input('Your guess: ')
# Convert string to int http://www.jquery-az.com/convert-a-python-string-to-int-and-float-by-using-int-and-float-class/
while (guess != randomNumber):
    if int(guess) < randomNumber:
        print('Too low')
    if int(guess) > randomNumber:
        print('Too high')
    if int(guess) == randomNumber:
        break
    guess = input('Your guess: ')
print('Good guess, you got it!', randomNumber)
