import random;
def play_again():
  print("Do you want to play again? (yes/no)");
  play_again=input();
  if play_again=="yes" or play_again=="YES":
   correct_number=random.randint(1,100);
   difficulty(correct_number);
  else:  
   print("Thank you for playing the game, see you next time!");
def difficulty(correct_number):
       
       print("Select the level of difficulty:-");
       difficulty_level=int(input("1 for easy, 2 for medium, 3 hard:-"));
       if difficulty_level==1:
        print("You have selected easy level, you will get 10 attempts to guess the number");
        easy_level(correct_number);
   
       elif difficulty_level==2:
         print("You have selected medium level, you will get 5 attempts to guess the number");
         medium_level(correct_number);   
       elif difficulty_level==3:
          print("You have selected hard level, you will get 3 attempts to guess the number");
          hard_level(correct_number); 
     
       else:
          print("invalid choice");


def suggestion(guess_number,correct_number):
   if guess_number>100 or guess_number<1: 
      print("Out of Range");
   elif guess_number<correct_number:
      print("your guess is too low\n");
    
   elif guess_number>correct_number:
     print("your guess is too high\n");
    
   else: print("you win")

def easy_level(correct_number):
     global score;
     attempts=10;
     print("Guess Number Between 1-100");
     for i in range(attempts):
       guess_number=int(input("Attemp remaining  "+str(attempts-(i+1))+" try again:-"));
       if guess_number!=correct_number:
             suggestion(guess_number,correct_number);
       else:
            print("Congratulations! You guessed the correct number.");
            score=score+1;
            print("your score is:",score)
            print("Correct number was",guess_number)
            break;
       
     else:
      print("you ran ou off attempt");
     play_again(); 

  
def medium_level(correct_number):
    global score;
    attempts=5;
    print("Guess Number between 1-100");
    for i in range(attempts):
           guess_number=int(input("Attemp remaining  "+str(attempts-(i+1))+" try again:-"));
           if guess_number!=correct_number:
             suggestion(guess_number,correct_number);
           else:
             print("Congratulations! You guessed the correct number.");
             score=score+1;
             print("your score is:",score);
             print("Correct number was",guess_number)
             break;
    else:
      print("you ran out of Attempt");
    play_again();
   
def hard_level(correct_number):
    global score;
    attempts=3;
    print("Guess Number Between 1-100");
    for i in range(attempts):
             guess_number=int(input("Attemp remaining  "+str(attempts-(i+1))+" try again:-"));
             if guess_number!=correct_number:
                
                suggestion(guess_number,correct_number);
           
           
             else:
                print("Congratulations! You guessed the correct number.");
                score=score+1;
                print("your score is:",score)
                print("Correct number was",guess_number)
               
    else:
     print("you ran ou off attempt"); 
    play_again();
level_1="easy";
level_2="medium";
level_3="hard";
score=0;
correct_number=random.randint(1,100);
print("Welcome to the Number Guessing Game");
difficulty(correct_number);

print("your Total Score was",score);
