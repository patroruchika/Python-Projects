import random

n=int(input("Enter upper range limit: "))
def comp_guess(x):
    low=1
    high=x
    feedback=""
    while feedback!='C':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high (H), too low (L) or correct (C)? ")
        if feedback == 'H':
            high = guess-1
        elif feedback == 'L':
            low = guess+1
    print(f"Computer guessed {guess} correctly!")

comp_guess(n)
