# Uses Random Module for random values
import random as rd

print("Rock,Paper,Scissor\n")

draw_games = 0
computer_score = 0
player_score = 0

# Function Definition
def theGame(pl,cp):
  if(player == computer_action):
    return 'draw'
  elif(player == "Rock" and computer == "Paper"):
    return 'lose'
  elif(player == "Rock" and computer == "Scissor"):
    return 'win'
  elif(player == "Paper" and computer == "Rock"):
    return 'win'
  elif(player == "Paper" and computer == "Scissor"):
    return 'lose'
  elif(player == "Scissor" and computer == "Rock"):
    return 'lose'
  elif(player == "Scissor" and computer == "Paper"):
    return 'win'

# The Game Structure
i = 1
while(i<=5):
  # Asking for Player Responses

  print("            1=Rock , 2=Paper & 3= Scissor\n ")
  print()
  action = int(input(f"{i}. Enter your Action : "))
  # Making Computer Part using random

  cp_actions = ['Rock','Paper','Scissor','Paper','Scissor','Rock','Scissor','Paper','Rock']
  computer = rd.choice(cp_actions)
  cp = ''.join(computer)

# Conditionals
  if(action==1):
    player = "Rock"
    computer_action = cp
    print(f"The Computer : {computer_action} & Player : {player}")
    result = theGame(player,computer_action)
  
  elif(action==2):
    player = "Paper"
    computer_action = cp
    print(f"The Computer : {computer_action} & Player : {player}")
    result = theGame(player,computer_action)

  elif(action==3):
    player = "Scissor"
    computer_action = cp
    print(f"The Computer : {computer_action} & Player : {player}")
    result = theGame(player,computer_action)

  else:
    print("Enter Correct Action :")
    print("SKIPPED")
    continue
  if result == "draw":
    print("Game ended in a DRAW")
    draw_games += 1
  elif result == "lose":
    print("You LOSE to Computer")
    computer_score += 1
  else:
    print("You WIN from Computer")
    player_score += 1
  
  i += 1

print(f"\nFinal Scores - Player: {player_score}, Computer: {computer_score}, Draw: {draw_games}")

# Enjoy 
# @Hamzamalik

