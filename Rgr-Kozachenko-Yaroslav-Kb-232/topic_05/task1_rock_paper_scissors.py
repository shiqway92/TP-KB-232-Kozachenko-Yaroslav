
import random

def play_game():
    choices = ["rock", "scissor", "paper"]
    user_choice = input("Enter rock, scissor, or paper: ").strip().lower()
    if user_choice not in choices:
        print("Invalid choice.")
        return
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissor") or          (user_choice == "scissor" and computer_choice == "paper") or          (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose.")

if __name__ == "__main__":
    play_game()
