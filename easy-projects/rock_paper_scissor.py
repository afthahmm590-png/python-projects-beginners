import random
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {ROCK: '🪨', PAPER: '📄', SCISSORS: '✂️'}
choices = (tuple(emojis.keys()))

def get_user_choice():
    while True:
        user_choice = input('Rock,Paper, or Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        #if choice is not valid.print an error.
        else:
          print('Invalid choice! Please try again.')

def display_choices(user_choice, computer_choice):
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
   if user_choice == computer_choice:
    print("It's a tie!")
   elif (
     (user_choice == ROCK and computer_choice == SCISSORS) or 
     (user_choice == PAPER and computer_choice == ROCK) or 
     (user_choice == SCISSORS and computer_choice == PAPER)):
    print("You win!")
   else:
    print("You lose!")

def play_game():
   
 while True:

  user_choice = get_user_choice()

  computer_choice = random.choice(choices)

  display_choices(user_choice, computer_choice)

  determine_winner(user_choice, computer_choice)

 #ask the user if they want to continue
  play_again = input("Do you want to play again? (y/n): ").lower()
  if play_again == 'n':
    print("Thanks for playing!")
    break
  
play_game()