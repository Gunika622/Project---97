import random

number  = random.randint(1,9)

chances = 0

while chances < 5:
    guess = int(input("Enter your guess:-"))
    
    if guess == number :
        print("you won!!")
elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    # The user entered number is greater than the generated number
    else:
        print("Your guess was too high: Guess a number lower than", guess)

    # Increase the value of chance by 1
    chances += 1


# Check whether the user guessed the correct number
if not chances < 5:
    print("YOU LOSE!!! The number is", number)
