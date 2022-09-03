import random 
small = 1
big = 100
print(f'I thought of a number between {small} and {big}')

number= random.randint(small, big)
guess= 0

while guess != number:
    guess=int(input("Guess the number:"))
    if guess < number:
        print("Too small")
    elif guess > number:
        print("Too big")
    else:
        print(f'you won!, The number was {number}')
        
