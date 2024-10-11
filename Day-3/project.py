"""
Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

Use the flow chart linked here to create the game logic.

Once you've completed the project, you can always extend the game and make it more interesting!
"""

# Write your code below this line 👇
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

direction = input('''\nYou are at a cross road. Where do you want to go?
    Type "left" or "right"
''')

if direction == "left" or direction == "Left":
    water = input('''\nYou've come to a lake. There is an island in the middle of the lake.
    Type "wait" to wait for a boat. Type "swim" to swim across.
''')
    if water == "wait" or water == "Wait":
        door = input('''\nYou arrive at the island unharmed. There is a house with 3 doors.
    One red, one yellow, and one blue. Which color do you choose?
''')
        if door == "red" or door == "Red":
            print("\nIt's a room full of fire. Game Over.")
        elif door == "yellow" or door == "Yellow":
            print("\nYou found the treasure! You Win!")
        elif door == "blue" or door == "Blue":
            print("\nYou enter a room of beasts. Game Over.")
        else:
            print("\nNo such room exists. Game Over")
    else:
        print("\nYou get attacked by an angry trout. Game Over.")
else:
    print("\nYou fell into a hole. Game Over.")
