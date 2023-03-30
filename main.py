import random

def get_choices():
  sign = ["rock","paper","scissor"]
  player_choice = input("enter a choice rock paper scissor: \n")
  computer_choice = random.choice(sign)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player,computer):
  if player == computer:
    print(f"match tied computer chose {computer} and player chose {player}")
  elif player == "rock":
    if computer == "paper":
      print(f"computer won computer chose {computer} and player chose {player}")
    else:
      print(f"player won computer chose {computer} and player chose {player}")
  elif player == "paper":
    if computer == "scissor":
      print(f"computer won computer chose {computer} and player chose {player}")
    else:
      print(f"player won computer chose {computer} and player chose {player}")
  elif player == "scissor":
    if computer == "rock":
      print(f"computer won computer chose {computer} and player chose {player}")
    else:
      print(f"player won computer chose {computer} and player chose {player}")

choices = get_choices()
check_win(choices["player"],choices["computer"])