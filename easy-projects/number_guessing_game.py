import random

number_to_guess = random.randint(1, 100)
while True:
 try:
  guess = int(input("I'm thinking of a number between 1 and 100. Can you guess it?"))

  if guess < number_to_guess:
    print("Too low! Try again.")
  elif guess > number_to_guess:
    print("Too high! Try again.")
  else:
    print("Congratulations! You've guessed the number!")
    break
 except ValueError:
   print("Please enter a valid integer.")

