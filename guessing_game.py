import random

number = random.randint(0,100)
while True:
    guess = input("Type your guess (0-100): ")
    if not guess.isdigit():
        print( "Invalid input. Enter a number")
        continue
    elif 100 < int(guess) < 0 :
        print("Enter a number in the range")
        continue
        
        
    if int(guess) > number:
        print("Too High")
    elif int(guess) < number:
        print("Too Low")
    else:
        print( "You guess it")
        break
