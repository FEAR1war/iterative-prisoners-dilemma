
def validate():
     guess = '1' # initialization with a bad guess
     answer = 'hangman word'
     while guess not in answer:
         guess = raw_input('Name a letter in \'' + answer + '\': ')
     print('Thank you!')
  
     
        

import random

def goguess():
    print("I have a number between 1 and 20 inclusive. Can you guess it?")
    number = random.randint(1, 20)
    guess = int(raw_input())
    tries = 1
    while guess != number and tries <6:
	    tries += 1
	    if guess<number:
	       print ("the number you have entered is too low, guess again.")
	    else:
	       print ("the number you have entered is too high, guess again.")
	    guess = int(raw_input())
    if tries == 6:
        print ("you have taken too much time, restart")
    if guess == number:
	print ("you have guess the correct number in") ,tries, ("tries")