import random

# Function to get the computer's choice
def computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Main function for the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Get user input
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'exit' to quit): ").lower()
        
        if user_choice == "exit":
            print("Thanks for playing!")
            break

        # Check if input is valid
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        # Get computer's choice
        comp_choice = computer_choice()
        print(f"Computer chose: {comp_choice}")
        
        # Determine the winner
        result = determine_winner(user_choice, comp_choice)
        print(result)

# Run the game
if __name__ == "__main__":
    play_game()
