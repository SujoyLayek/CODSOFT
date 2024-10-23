import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Main function to play the game
def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("Welcome to Rock-Paper-Scissors!")
    
    while True:
        print(f"\nRound {round_number}:")
        # User input with validation
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please choose rock, paper, or scissors.")
            continue

        # Computer's choice
        computer_choice = get_computer_choice()

        # Display both choices
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display current scores
        print(f"Current Score -> You: {user_score} | Computer: {computer_score}")

        # Ask the user if they want to play again
        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != "y":
            print("\nFinal Score:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            print("Thank you for playing!")
            break

        # Increment round number
        round_number += 1

if __name__ == "__main__":
    play_game()
