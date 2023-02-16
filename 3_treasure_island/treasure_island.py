print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

path = input("You woke up in the middle of a road, there is two path, the left one leads you to a dark place, the right one leads you to a shinny place? Which path do you choose?\n")
path_lower = path.lower()
if path_lower == "right":
  print("Your path gets shinnier along the way, everything is gold.")
  river = input("You've entered a golden forest and come across a river made of gold. There is a boat next to it. How do you cross the river?\n")
  river_lower = river.lower()
  if river_lower == "boat" or "get the boat" or "use the boat":
    print("Suddenly a grim reaper appears next to the boat and offers you to get a ride on his boat to the other side of the river.")
    castle = input("At the end of the river, you see a giant castle. The grim reaper ask you to choose one of the entries of the castle. There are three doors, a red one, a black one and a golden one. Which one you choose?\n")
    castle_lower = castle.lower()
    if castle_lower == "red" or castle_lower == "red door":
      print("You've opened the gates of hell. Game over.")
    elif castle_lower == "black" or castle_lower == "black door":
      print("The grim reaper reaps your soul off. Game over.")
    elif castle_lower == "gold" or castle_lower == "golden door":
              print("You've found the treasure!")
  else:
        print("The golden river melted you away. Game over.")
else:
  print("Suddenly a elephant falls over your head. Game over.")
