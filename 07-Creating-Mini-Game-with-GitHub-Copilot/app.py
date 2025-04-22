#!/usr/bin/env python3

# Import necessary libraries
import random

def main():
    """
    Main function to run the rock, paper, scissors game
    """
    print("Welcome to Rock, Paper, Scissors!")
    print("--------------------------------")
    
    # Initialize scores
    player_wins = 0
    computer_wins = 0
    ties = 0
    rounds_played = 0
    
    # Game loop
    play_again = True
    while play_again:
        # Get player's choice
        player_choice = get_player_choice()
        
        # Generate computer's choice
        computer_choice = get_computer_choice()
        
        # Display choices
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(player_choice, computer_choice)
        
        # Update scores
        if result == "win":
            player_wins += 1
            print("You win this round!")
        elif result == "lose":
            computer_wins += 1
            print("Computer wins this round!")
        else:
            ties += 1
            print("It's a tie!")
        
        rounds_played += 1
        
        # Ask to play again
        play_again = ask_play_again()
    
    # Display final score
    display_final_score(player_wins, computer_wins, ties, rounds_played)

def get_player_choice():
    """
    Get the player's choice (rock, paper, or scissors)
    
    Returns:
        str: The player's choice in lowercase
    """
    valid_choices = ["rock", "paper", "scissors"]
    
    while True:
        choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
        
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    """
    Generate a random choice for the computer
    
    Returns:
        str: The computer's choice
    """
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    """
    Determine the winner based on the choices
    
    Args:
        player_choice (str): The player's choice
        computer_choice (str): The computer's choice
        
    Returns:
        str: 'win' if player wins, 'lose' if computer wins, 'tie' if it's a tie
    """
    # If choices are the same, it's a tie
    if player_choice == computer_choice:
        return "tie"
    
    # Define the winning combinations (player choice vs computer choice)
    winning_combinations = {
        "rock": "scissors",     # Rock beats scissors
        "scissors": "paper",    # Scissors beats paper
        "paper": "rock"         # Paper beats rock
    }
    
    # Check if the player wins
    if winning_combinations[player_choice] == computer_choice:
        return "win"
    else:
        return "lose"

def ask_play_again():
    """
    Ask the player if they want to play another round
    
    Returns:
        bool: True if the player wants to play again, False otherwise
    """
    while True:
        response = input("\nDo you want to play again? (yes/no): ").lower()
        
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

def display_final_score(player_wins, computer_wins, ties, rounds_played):
    """
    Display the final score of the game
    
    Args:
        player_wins (int): Number of player wins
        computer_wins (int): Number of computer wins
        ties (int): Number of ties
        rounds_played (int): Total number of rounds played
    """
    print("\n===== GAME OVER =====")
    print(f"Total rounds played: {rounds_played}")
    print(f"Your wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Ties: {ties}")
    
    # Determine the overall winner
    if player_wins > computer_wins:
        print("\nCongratulations! You won the game!")
    elif computer_wins > player_wins:
        print("\nComputer won the game! Better luck next time.")
    else:
        print("\nThe game ended in a tie!")
    
    print("Thanks for playing!")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()

