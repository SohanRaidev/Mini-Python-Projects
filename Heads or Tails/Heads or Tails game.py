import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

print("Welcome to the Heads or Tails game!")

rounds = int(input("Enter the number of rounds you'd like to play: "))

user_score = 0
computer_score = 0

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}/{rounds}")
    
    user_choice = input("Choose Heads (H) or Tails (T): ").strip().lower()
    
    if user_choice in ["h", "heads"]:
        user_choice = "Heads"
    elif user_choice in ["t", "tails"]:
        user_choice = "Tails"
    else:
        print("Invalid choice! Please choose Heads (H) or Tails (T).")
        continue
    
    result = flip_coin()
    print(f"The coin landed on: {result}")
    
    if user_choice == result:
        print("You WIN this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print("\nGame Over!")
print(f"Final Score - You: {user_score}, Computer: {computer_score}")

if rounds > 0:
    win_percentage = (user_score / rounds) * 100
else:
    win_percentage = 0

print(f"Your win percentage: {win_percentage:.2f}%")

if user_score > computer_score:
    print("\nCongratulations, you won the game!\n")
elif user_score < computer_score:
    print("\nComputer wins the game. Better luck next time!\n")
else:
    print("It's a tie!")
 