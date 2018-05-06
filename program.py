import random

print('--------------------------------------')
print('        GUESS THAT NUMBER GAME')
print('--------------------------------------')
print()

the_number = random.randint(0, 100)

guess_text = input('Guess a number between 0 and 100: ')
guess = int(guess_text)

def compareGuess(number, guess):
  if number == guess:
    print('You guessed correctly!')
  elif number >= guess:
    print('Your guess is HIGHER than the number; Guess again!')
  else number >= guess:
    print('Your guess is LOWER than the number; Guess again!')

# TODO - continue work