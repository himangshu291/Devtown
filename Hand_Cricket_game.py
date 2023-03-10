#hand cricket
import random
print("Welcome to hand cricket!! You have to defend/chase the score inorder to win like real cricket.")
print("The condition for getting out is that the computer and the user have to produce the same number.")
print("-----------------------------------------------------------------------------------------------------")
def toss():
    opt=input("What do you want to choose(Even/Odd): ").upper()
    if (opt=="EVEN"):
        print("You choose Even")
        comp_choose=random.choice(["Even","Odd"])
        print("Computer choose ",comp_choose)
    elif (opt=="ODD"):
        print("You choose Odd")
        if(opt==2 or opt==4 or opt==6):
            print("please enter the odd number, you choose odd")
    else:
        print("-------Invalid Input-------Game Restarting-----")
        toss_again()
    comp_choose=random.choice(["Even","Odd"])
    print("Computer choose:",comp_choose)
    print("After adding User's number and the Computer's number if it's even then user wins the toss!")
    user_toss=int(input("Choose the number between 1 and 6:"))
    if user_toss>6 :
        print("-------Invalid Input-------Game Restarting-----")
        toss_again()
    comp_toss=random.choice([1,2,3,4,5,6])
    print("You choose:",user_toss,"Computer choose:",comp_toss)
    toss=user_toss+comp_toss
    if toss%2==0: 
        print("You have won the toss!")
        select=input("Great..!!, You have won the toss!! What would you wanna choose? Bat/Bowl: ").upper()
        print("You choose to ",select,"first")
        if (select == 'BAT'):
            #print("User has chosen to bat first....")
            print("GAME STARTS!")
            batting_first()
        elif (select == 'BOWL') :
            #print("User has chosen to bowl first....")
            #print("To get the computer out chose the same number as the computer!!")
            print("GAME STARTS!")
            batting_second()
        else :
            print("-------Invalid Input-------Game Restarting-----")
            toss_again()
    else :
        print("Computer have won the toss!")
        select=random.choice(["Bat","Bowl"])
        print("Computer has to ",select,"first")
        if select == 'bat':
            print("Computer has chosen to bat first!! GAME STARTS!!")
            batting_second()
        else:
            print("Computer has chosen to bowl first!! GAME STARTS!!")
            batting_first()
def batting_first():
    print("you will have to bat now, choose a number between 1 and 6.")
    print("Choosing a number higher than 6 isn't allowed and you will be sent back!")
    print("If you choose a number the same as the computer you will be out!!")
    runs=0
    while True:
        comp_number = random.choice([1,2,3,4,5,6])
        user_number = int(input("Bat: "))
        if user_number>6 :
            print("-------Invalid Input-------Game Restarting-----")
            toss()
        print("Computer Bowls",comp_number)
        runs+=user_number
        print("Your total score: ",runs)
        print("---------------------------------------------------------------------------------------------------------------")
        if comp_number == user_number:
            print("OUT!!")
            print("You have scored",runs)
            break    
    print("Computer require",runs+1,"runs to win..!")
    print("Computer is ready to chase down the target..!")
    comp_score = 0
    while (True) :
        comp_bat = random.choice([1,2,3,4,5,6])
        user_bowl = int(input("Bowl: "))
        if user_bowl>6 :
            print("-------Invalid Input-------Game Restarting-----")
            toss()
        print("Computer bats: ",comp_bat)
        comp_score = comp_score+comp_bat
        print("Computer's total score: ",comp_score)
        print("---------------------------------------------------------------------------------------------------------------")
        if comp_score>runs :
            print("Computer total score: ",comp_score)
            print("Hard luck! That was a close one... The Computer has win this game!!")
            print("---------------------------------------------------------------------------------------------------------------")
            break
        if comp_bat == user_bowl :
            print("Gone!..You dismissed computer!..Out!")
            print("Computer score: ",comp_score)
            if runs>comp_score :
                print("Well done, what a great win! You won by",((runs)-(comp_score)),"runs, Congratulations..!!")
                print("---------------------------------------------------------------------------------------------------------------")
            else :
                print("-----Match Tied----")
                print("---------------------------------------------------------------------------------------------------------------")
            break

def batting_second():
    print("Computer will have to bat now...")
    comp_score=0
    while (True) :
        comp_number = random.choice([1,2,3,4,5,6])
        user_bowl = int(input("Bowl: "))
        if user_bowl>6 :
            print("-------Invalid Input-------Game Restarting-----")
            print("---------------------------------------------------------------------------------------------------------------")
            toss()
        print("Computer bats: ",comp_number)
        comp_score=comp_score+comp_number
        print("Computer's total score: ",comp_score)
        print("---------------------------------------------------------------------------------------------------------------")
        if (comp_number == user_bowl) :
            print("Gone!..You dismissed computer!..Out!")
            print("Computer score: ",comp_score)
            break
    print("Computer is ready to bowl, All the best...")
    runs=0
    while (True):
        comp_number = random.choice([1,2,3,4,5,6])
        user_number = int(input("Bat: "))
        if user_number>6 :
            print("-------Invalid Input-------Game Restarting-----")
            print("---------------------------------------------------------------------------------------------------------------")
            toss()
        print("Computer Bowls",comp_number)
        runs=runs+user_number
        print("Your total score: ",runs)
        print("---------------------------------------------------------------------------------------------------------------")
        if comp_score<runs :
            print("Well done, what a great win! Chased down the target perfectly..You won by",((runs)-(comp_score)),"runs, Congratulations..!!")
            print("---------------------------------------------------------------------------------------------------------------")
            break
        if comp_number == user_number :
            print("OUT!! Computer dismissed you..")
            print("You have scored",runs)
            if comp_score>runs :
                print("Computer total score: ",comp_score)
                print("Hard luck! That was a close one... The Computer has win by",((comp_score)-(runs)),"runs..")
                print("---------------------------------------------------------------------------------------------------------------")
            else :
                print("------Match Tied-------")
                print("---------------------------------------------------------------------------------------------------------------")
            break
         
def toss_again():        
    print("Let's toss!!")
    toss()
 
def end():
        answer = input(("Would you like a rematch? (Y/N): ")).upper()
        if answer == "Y":
            print("Ok!! Let's do the toss!!")
            toss()
        if answer == "N":
          print("Thanks for playing! You were an excellent cricketer!")
toss_again()               