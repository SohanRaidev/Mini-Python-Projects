import random

def rock_paper_scissors():
    choices = ['Rock', 'Paper', 'Scissors']
    
    while True:
        user_choice = input("Enter Rock, Paper, or Scissors (or 'quit' to exit): ").capitalize()
        
        if user_choice == 'Quit':
            print("Thanks for playing!")
            break
        elif user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("\nIt's a tie!\n")
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Paper' and computer_choice == 'Rock') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper'):
            print("\nYou win!\n")
        else:
            print("\nComputer wins!\n")

rock_paper_scissors()
