import random
game = ["stone","paper","scissor"]
computer = random.choice(game)
user=input("Enter your choice\n")
if user==computer:
    print("Tie")
    print("No one wins")
elif user=="stone" and computer=="paper":
    print("You loose")
    print("computer choice is paper")
elif user=="stone" and computer=="scissor":
    print("you win")
    print("computer choice is scissor")
elif user=="paper" and computer=="stone":
    print("you wins")
    print("computer choice is stoone")
elif user=="paper" and computer=="scissor":
    print("You loose")
    print("computer choice is scissor")
elif user=="scissor" and computer=="stone":
    print("you loose")
    print("computer choice is stone")
elif user=="scissor" and computer=="paper":
    print("you wins")
    print("computer choice is paper")
else:
    print("Error value")