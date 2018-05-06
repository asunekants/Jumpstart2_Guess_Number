import random


def header():
  print('--------------------------------------')
  print('        GUESS THAT NUMBER GAME')
  print('--------------------------------------')
  print()


def compareGuess(number):
  guess_text = input('Guess a number between 0 and 100: ')
  guess = int(guess_text)
  if guess not in range(0,101):
    print('Your guess is out of range.')
    return False
  elif number == guess:
    print('You guessed correctly! Yay!')
    return True
  elif number < guess:
    print('Your guess is HIGHER than the number; Guess again!')
    return False
  elif number > guess:
    print('Your guess is LOWER than the number; Guess again!')
    return False


def mainLoop():
  header()
  number = random.randint(0, 100)
  guess_correct = False
  try_counter = 0
  while guess_correct == False:
    guess_correct = compareGuess(number)
    try_counter += 1
  print('You\'ve guessed the number in {0} guesses.'.format(try_counter))


mainLoop()
