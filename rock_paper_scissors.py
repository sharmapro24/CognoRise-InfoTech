import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("It's a tie!")

def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors Game!")

    while True:
        print("\nSelect your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_input = input("Enter choice (1/2/3): ")

        choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}

        if user_input not in choices:
            print("Invalid choice. Please try again.")
            continue

        user_choice = choices[user_input]
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"\nCurrent Scores - You: {user_score}, Computer: {computer_score}")

        while True:
            play_again = input("\nDo you want to play another round? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == 'no':
            print(f"\nFinal Scores - You: {user_score}, Computer: {computer_score}")
            print("Thank you for playing Rock, Paper, Scissors! Goodbye!")
            break

if __name__ == "__main__":
    main()


