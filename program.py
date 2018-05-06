import random


def header():
  print('--------------------------------------')
  print('        GUESS THAT NUMBER GAME')
  print('--------------------------------------')
  print()


def compareGuess(number, name):
  guess_text = input('Guess a number between 0 and 100: ')
  guess = int(guess_text)
  if guess not in range(0,101):
    print('Your guess is out of range.')
    return False
  elif number == guess:
    print('Congrats, {}, you guessed correctly! Yay!'.format(name))
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
  name = input('What is your name? ')
  guess_correct = False
  try_counter = 0
  while guess_correct == False:
    guess_correct = compareGuess(number, name)
    try_counter += 1
  print('You\'ve guessed the number in {} guesses.'.format(try_counter))


mainLoop()
