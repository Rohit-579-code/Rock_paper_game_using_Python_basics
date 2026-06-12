
def playground():
    options = int(input("List of Things you can try to guess:-\n 1).Animal\n 2).Bollyhood Star\n 3).Mobile Game\n"))
    if options==1:
        animal();
    elif options==2:
        hero();
    elif options==3:
        game();

def animal():
    hint=1
    while hint<=3:
        if hint==1:
            print("it is and carnivoras Animal")
        elif hint==2:
            print("it is also known as king of jungle")
        elif hint==3:
            print("it is a wild animal")
        guess= int(input("1).want guess\n2).want more hint \n"))
        if guess==1:
            correct=input("Enter your guess:-\n")
            if correct=='lion' or correct== 'Lion':
                print("Your guess was correct")
                break
        elif guess==2:
            hint+=1
    if hint>3:
        print(" You ran out of hint, the correct Answer was Lion")


def hero():
    hint=1
    while hint<=3:
        if hint==1:
            print("Male Actor")
        elif hint==2:
            print("Plays Hindi FLim")
        elif hint==3:
            print("Also known as Bhai-jhan")
        guess= int(input("1).want guess\n2).want more hint \n"))
        if guess==1:
            correct=input("Enter your guess:- \n")
            if correct=='salman khan' or correct== 'Salman Khan':
                print("Your guess was correct")
                break
        elif guess==2:
            hint+=1
    if hint>3:
        print(" You ran out of hint, correct answer was:- Salman Khan")


def game():
    hint=1
    while hint<=3:
        if hint==1:
            print("Corona Time Popular Game")
        elif hint==2:
            print("Booyah")
        elif hint==3:
            print("Related to Name:- Fire")
        guess= int(input("1).want guess\n2).want more hint \n"))
        if guess==1:
            correct=input("Enter your guess:- \n")
            if correct=='Free Fire' or correct== 'free fire':
                print("Your guess was correct")
                break
        elif guess==2:
            hint+=1
    if hint>3:
        print(" You ran out of hint, correct answer was:- Free Fire")
playground();