print(r'''
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

print("In which side will you go?")
first_move = input("Left or right?\n").lower()
if first_move == "left":
    print("There's a lake with shark, what will you do?")
    second_move = input("Swim or Wait?\n").lower()
    if second_move == "wait":
        print("There is 3 doors, in which door will you entry? ")
        third_move = input("Blue, Red or Yellow?\n").lower()
        if third_move == "yellow":
            print("There is two ways to get out, in which will you go?")
            fourth_move = input("First or Second?\n").lower()
            if fourth_move == "first":
                print("You won!")
        elif third_move == "blue":
            print("Eaten by beasts. Game over.")
        elif third_move == "red":
            print("Burned by fire. Game over.")
        else:
            print("Game over!")
    else:
        print("Attacked by a trout. Game over!")
else:
    print("You fell into a hole. Game over!")
