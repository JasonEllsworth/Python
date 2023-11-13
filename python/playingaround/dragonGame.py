import random
import time

#the isle of dragons game

# User should be prompted by a series of print statements to a cave.
# The user should than be given the choice for which cave to enter.
# One cave will have a dragon which wishes to consume them, the other is a dragon that will share its hoard.
# The user will than be givn the choice to play through the game again or quit.

# Create an intro statement into the game
    # Should be something about the adventuer having an important choice
# enter into a looping function. This is where the user will input the choice of which cave to enter
# the loop will check a random number variable and see which cave contains which dragon.
    # import random generater which till give the user which cave, each loop will be different this way.
# at the end the user should be given a choice
    # depending on which choice the user selects they will either loop back to the beginning or exit the game.


print(" welcome adventurer, you have entered the isle of dragons...")
print()
print("tell me, brave adventurer, what is thine name?")
print()
ad_name = input()

def dragon_den() :
    
    player_choice = ''
    danger = random.randint(1,2)
    result = ""
    
    first_section = print(ad_name + ''' you have traveled far to make it to the dragons isle.
          As you journey nears its end, a large mountain looms before you...
          ''')
    print()
    time.sleep(3)
    
    second_section = print(''' you have heard a great many stories of the mighty dragons which live within.
                           one dragon, red in color, defends a mighty hoard of treasure and is willing to give those who go past a share of its loot...''')
    print()
    time.sleep(3)
    
    third_section = print('''However, its brother, the black dragon, jelious of its brothers hoard devours any advtuerers foolish enough to enter''')
    
    print()
    time.sleep(3)
    
    fourth_section = print(ad_name + '''Which path will you choose? 
                           left
                           or
                           right''')
    print()
    input()
    
    if danger == 1:
        print('''You enter the cave and a might red dragon greets you! 
              it shares its great hoard with you, and wishes you well on your journey home''')
        result = 'white'
    else :
        print('''you enter the cave, soon a might black dragon swoops down on you.
              the last sound you hear is its laughter before devoring you in one bite''')
        result = 'black'
    
    #print('Play again?')
    #playAgain = input()
         
    


playAgain='yes'


while playAgain == 'yes' or playAgain == 'y':
    dragon_den()
    print('Play again?')
    playAgain = input()
        
        
        
        



