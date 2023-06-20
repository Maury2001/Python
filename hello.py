import random

def play():
 user= input("what your choice? 'r' is for rock 'p' is for paper 's' is for scissors--")
 computer = random.choice(['r','p','s'])

 if user==computer:
    print('tie')
    

 if is_win(user, computer):
    print('winner')

 if is_win(computer, user):
     print ('loser')



def is_win(player, opponent):
   if (player=='r' and opponent=='s') or (player =='s' and opponent=='p') or (player=='p' and opponent=='r'):
       return True

print(play())
