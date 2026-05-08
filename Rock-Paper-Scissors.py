import random
computer_score=0;
user_score=0;
rock = "rock"
paper = "paper"
scissors = "scissors"

def choice():
    user_choice = input("Enter your choice " + rock + ", " + paper + ", or " + scissors + ": ")#user input

    while user_choice not in [rock, paper, scissors]:#check if the user input is valid
        user_choice = input("Invalid choice. Please enter " + rock + ", " + paper + ", or " + scissors + ": ")#ask the user to enter a valid choice until they do

    return user_choice #return the user's choice

while True:
  computer = random.choice([rock, paper, scissors]);#computer randomly chooses rock, paper, or scissors
  user = choice()
  if user==computer:#check if it's a tie
    print("Computer's choice:", computer)
    print("Your choice:", user)
  
    print("It's a tie!");
    print("Computer score:",computer_score);
    print("Your score:",user_score);

    

  elif(user==rock and computer==scissors)or(user==paper and computer==rock)or(user==scissors and computer==paper):#check if the user wins
    print("Computer's choice:", computer)
    print("Your choice:", user)
    print("You win!");
    user_score+=1;
    print("Computer score:",computer_score);
    print("Your score:",user_score);
   
  else:   #if the computer wins
    print("Computer's choice:", computer)
    print("Your choice:", user)
    print("Computer wins!");
    computer_score+=1;
    print("computer score:", computer_score);
    print("Your score:", user_score);
    choice();
 