# import random;
# def user_dice(use_score):
#     global user_score
#     global taget
#     user_dice= random.randint(1,6)
#     print("your Score is", user_dice)
#     user_score= user_score + user_dice
#     return user_score
   
    
# def computer_dice(com_score):
#     global target
#     global computer_score
#     computer_dice = random.randint(1,6)
#     print("computer  score:- ", computer_dice)
#     computer_score= computer_score+computer_dice
#     print(" computer Current Score is :- ", computer_score)
#     return computer_score

        
    

# user_score =0;
# computer_score=0;
# target = 12
# print(" to win the game you need to score 12 , \t both computer and you will rol the dice turn by turn , one who meet the 12 first wins.")
# choice =input("Make a Choice, Do you want to roll the dice first Y/N:- ");
# if choice == 'y' or choice == 'Y':
#     user_dice(user_score);
#     while user_score<12 or computer_score<12:
#         user_score=user_dice(user_score)
#         if user_score>=12:
#             print("you win the race")
#         break
# elif choice == 'n' or choice =='N':
#     computer_dice(computer_score)
#     while user_score<12 or computer_score<12:
#         computer_score=user_dice(computer_score)
#         if computer_score>=12:
#             print("you win the race")
#         break
    
# else:
#     print("Invalid choice")

import random;
def roll_dice():
    return random.randint(1,6)

def user_roll(score):
    input("press the Enter to roll the dice")
    random_score=roll_dice()
    score+=random_score
    print("your current score:-", score)
    return score
def computer_roll(score):
    random_score=roll_dice()
    score+=random_score
    print(" computer current score:- ", score)
    return score
def play_game():
    user_score=0
    computer_score=0
    while computer_score<12 and user_score<12:
        user_score=user_roll(user_score)
        if user_score>= 12:
            print(" you won the race")
            break

        computer_score=computer_roll(computer_score)
        if computer_score>=12:
            print("you loose the race")
            break
    replay=input("DO you Wanna Race Again:-Y/N")
    if replay=='y' or replay=='Y':
        play_game()
    elif replay=='n' or replay=='N':
        print("Thank you for playing")
            
play_game();




