import random

def play_rock_paper_scissors():
   

    user_choice = input("Choose rock, paper, or scissors: ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

while True:
    play_rock_paper_scissors()
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")