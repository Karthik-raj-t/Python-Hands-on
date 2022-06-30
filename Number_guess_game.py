# guessing game 
# provide input for starting and ending number. 
# start guessing the random number generated within the provided range



import random 

def guess(x,y):
    random_number = random.randint(x,y)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between {x} and {y}: '))
        if guess < random_number:
            print('Sorry, guess again. Too Low')
        elif guess > random_number:
            print('Sorry, guess again. Too High')
    
    print(f'Yay, Congrats. You have guessed the number {random_number} correctly')



guess(int(input('starting Number: ')),int(input('Ending Number: ')))