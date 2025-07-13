

import random

item_list = ["rock", "paper", "scissors"]

user_choice = input("Enter your move (rock, paper, scissors): ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice not in item_list:
    print("Invalid input. Please choose rock, paper, or scissors.")

elif user_choice == comp_choice:
    print("Both chose the same: Match Tie")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("Paper covers rock = Computer wins")
    else:
        print("Rock smashes scissors = You win")

elif user_choice == "paper":
    if comp_choice == "scissors":
        print("Scissors cuts paper = Computer wins")
    else:
        print("Paper covers rock = You win")

elif user_choice == "scissors":
    if comp_choice == "paper":
        print("Scissors cuts paper = You win")
    else:
        print("Rock smashes scissors = Computer wins")


