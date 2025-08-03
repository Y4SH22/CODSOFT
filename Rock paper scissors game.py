import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice.")
        choice = input("Please choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_round():
    user_choice = get_user_choice()  # Fixed: assignment operator used
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)  # Fixed: assignment

    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

# Run a single round
play_round()
