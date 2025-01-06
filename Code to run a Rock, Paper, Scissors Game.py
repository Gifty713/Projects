#Code to run a Rock, Paper, Scissors Game
import random

options=('rock', 'paper', 'scissors')

play = True
while play:
    player = None    
    computer = random.choice(options)
    player = input('Enter a choice: ').lower()
    while player not in options:
        print('Pick an option between rock, paper, scissors')
        player = input('Enter a choice: ')

    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player == computer:
        print("It's a tie!")
    elif player == 'rock' and computer == 'scissors':
        print('You win!') 
    elif player == 'paper' and computer == 'rock':
        print('You win!')
    elif player == 'scissors' and computer == 'paper':
        print('You win!')
    else: print('You lose')

    play_again = input('Do you want to play again? (y/n): ').lower() 
    if play_again != 'y':
        play = False
        print('Thanks for playing!')