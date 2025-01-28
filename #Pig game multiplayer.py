#Pig game
#Multiplayer
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
   players = input('Enter numbers of players(2-4): ') #Enter the numbers of players playing the game
   if players.isdigit():#Check whether or not numbers of players is a number
       players = int(players)#To convert numbers of players from a string to an integer
       if 2<= players<=4: #If number of players less than 4 and greater than 2
             break #Break the loop
       else: 
             print('Invalid, try again. Must be between 2-4 players') #If a number outside the range
       
   else:
       print('Not a number, pick a number between 2-4')#If not a number
                    
max_score = 50
player_scores =[0 for _ in range(players)]#Initializing the scores of the players

while max(player_scores)<max_score:
     
     for player_idx in range(players): #To run this code for every player in the players range
        current_score = 0
        print(f'\n Player number {player_idx+1}, turn just started!\n ')#To show the turn of each player
        print('Your total score is:', player_scores[player_idx])
        while True:
    
            should_roll = input ('Would you like to roll? (y/n) ').lower()# Request on whether to end the game or continue
            if should_roll != "y":
                break #If no, end the loop
            
            value = roll() #Calling the roll function, to get a random rolled number
            if value == 1:
                print('You rolled a 1, turn done.')
                current_score = 0 #Resetting the scores, if player rolls a 1
            
                break
            else:
                current_score += value #Addition of a players score
                print(f'You rolled a: {value}')
                

            print(f'Your score is: {current_score}')

        player_scores[player_idx] += current_score
        print("Your total score is:",player_scores[player_idx])
        
max_score = max(player_scores)
winning_idx = player_scores.index(max_score) #Select the index of the element with the highest score
print(f"\nPlayer number", winning_idx+1, f"is the winner with a score of: {max_score}\n")

for player_idx in range(players):
    print(f'The result of player number {player_idx+1} at the end of the game: {player_scores[player_idx]}')
print('Thank you for playing my game!')
        
        
        
       
