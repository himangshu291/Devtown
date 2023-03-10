'''
Game rule-R,P,S
R P->P
R S->R
R R->-(TIE)
P S->S
'''
import random
times_of_play=int(input("How many times do you want to play?:"))
user_points=0
computer_points=0
for i in range(times_of_play):
    user=input("Enter the input(R/P/S): ").upper()
    comp=random.choice(['R','P','S'])
    if(user=='R' and comp=='S') or (user=='S' and comp=='P') or (user=='P' and comp=='R'):
        user_points+=1
        print('--------------------------------------------------------------------')
        print(f"User choose: {user} and Computer choose: {comp}")
        print("User Won!")
        print(f"User score: {user_points} and Computer score: {computer_points}")
        print('--------------------------------------------------------------------')
    elif(user=='P' and comp=='S') or (user=='S' and comp=='R') or (user=='R' and comp=='P'):
        computer_points+=1
        print('--------------------------------------------------------------------')
        print(f"User choose: {user} and Computer choose: {comp}")
        print("Computer Won!")
        print(f"User score: {user_points} and Computer score: {computer_points}")
        print('--------------------------------------------------------------------')
    else:
        print('--------------------------------------------------------------------')
        print(f"User choose: {user} and computer choose: {comp}")
        print("Match Draw!")
        print(f"User score: {user_points} and Computer score: {computer_points}")
        print('--------------------------------------------------------------------')
if user_points > computer_points:
  print('--------------------------------------------------------------------')
  print("User won the game!!!!!!")
  print('--------------------------------------------------------------------')
elif user_points < computer_points:
  print('--------------------------------------------------------------------')
  print("Computer won the game!!!!!!")
  print('--------------------------------------------------------------------')
else:
  print('--------------------------------------------------------------------')
  print("Match Draw!!")
  print('--------------------------------------------------------------------')