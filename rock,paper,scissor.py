#rock,paper and scissor

import random



user = input("rock,paper,scissor:")
action = ["rock","paper","scissor"]
computer =random.choice(action)
print(f"\nYou chose {user},computer chose {computer}.\n")
if user == computer:
    print(f"both the player selected {user}. its a tie!!")
elif user == "rock":
    if computer == "scissor":
        print("rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print("paper covers rock!you Win.")
    else:
        print("scissor cuts paper! you lose.")
elif user == "scissor":
    if computer == "paper":
        print("scissor cuts paper! you win.")
    else:
        print("rock smashes scissors! You lose.")

    