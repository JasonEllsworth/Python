#guess number game
 import random

print('Hello! What is you name')
user_name = input()

print(user_name + " I'm thinking of a number between 1 and 20, can you guess what it is in time?")

number = str(random.randint(1, 20))
print(number)
for guessTaken in range(6):
    guess = input()
    user_guess = str(guess)

    if user_guess < number:
        print("whoops! Too low!")
    if user_guess > number:
        print("whoops! Too high!")
    if user_guess == number:
        print("Congratulations, " + user_name + " you guessed " + user_guess + " !")
        print("it took you ")
        break
if user_guess != number:      
    print("Sorry, you ran out of tries, better luck next time!")
    
    
         
    

