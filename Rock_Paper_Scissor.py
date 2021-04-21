import random

def iswin(user,computer):
    if (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
        return True

def game():
    user=input("Select any one out of the three: 'r' for Rock, 'p' for Paper or 's' for Scissor: ",)
    computer=random.choice(['r','p','s'])
    if user==computer:
        print("It's a tie!")
    elif iswin(user,computer) == True:
        print("Congrats! You won")
    else:
        print("Oops! You lose. Try again.")

game()