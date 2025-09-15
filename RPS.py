#RPS.py
#Name: Meg Aerni
#Date: 9/14/2025
#Assignment: Lab 3, Part 2
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  playAgain = "Yes"
  while playAgain == "Yes":
      #User can play as many games as they wish.
      #Randomly choose the computer between 'R', 'P', or 'S'
      computer = random.choice( ["R", "P", "S"] )
      #Prompt the user for their RPS selection
      person = input("Choose your weapon (R, P, or S): ")
      #Determine winner and state what happened to the user
      if computer == "R":
        print("Computer chose Rock")
      elif computer == "P":
        print("Computer chose Paper")
      else: 
        print("Computer chose Scissors")

      if person == "R":
        print("You chose Rock")
      elif person == "P":
        print("You chose Paper")
      elif person == "S":
        print("You chose Scissors")
      else:
        print("You did not successfully select a weapon. Try again.")

      if (computer == "R" and person == "S") or (computer == "S" and person == "P") or (computer == "P" and person == "R"):
        print("You lose.")
        losses = losses + 1

      if (computer == "R" and person == "P") or (computer == "S" and person == "R") or (computer == "P" and person == "S"):
        print("You win! Congratulations!")
        wins = wins + 1

      if (computer == "R" and person == "R") or (computer == "P" and person == "P") or (computer == "S" and person == "S"):
        print("It's a tie!")
        ties = ties + 1
      #Ask the user if they would like to play again.
      playAgain = input("Would you like to play again? (\"Yes or No\"): ")
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
