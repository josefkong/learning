rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

rock_paper_scissors = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if player >= 3 or player < 0:
  print("You put an invalid number. You lost!")
else:
  print(rock_paper_scissors[player])
  computer = random.randint(0, 2)
  print("Computer choose:\n")
  print(rock_paper_scissors[computer])
  if player == 0 and computer == 2:
    print("You won!")
  elif player == 2 and computer == 0:
    print("You lost!")
  elif player > computer:
    print("You won!")
  elif player < computer:
    print("You lost!")
  elif player == computer:
    print("It's a draw!")