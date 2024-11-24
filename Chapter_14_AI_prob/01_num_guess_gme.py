""" Project 1.

    here we will make a random number guessing game, 
    take name of two users and then both play their chances 
    and in last who take less chances to guess the correct no. that player will win. 
"""

import random

ran_no1 = random.randint(1, 50)
ran_no2 = random.randint(1, 50)
print(ran_no1)
print(ran_no2)
chances= 10


def no_guess(ran_no, chances):
    i = 0

    while(i != chances):

        user_no = int(input("Guess a number to win the game:"))

        if(user_no>ran_no):
            print("\nYour guess is high, Please enter a lower guess!!!")
            print(f"You have {chances -(i+1)} chances left...")

        elif(user_no<ran_no):
            print("\nYour guess is low, Please enter a higher guess!!!")
            print(f"You have {chances -(i+1)} chances left...")
    
        elif(user_no==ran_no):
            print(f"\nHurray!!! \You have won the game in {chances -(i+1)} chances...")
            return i + 1
        
        i = i+1

    print("You lost the game... \nTry Next time")
    return i


def main():

    player1_name = input("Enter the player name:")
    result1 = no_guess(ran_no1, chances)

    print("\n")
    player2_name = input("Enter the player name:")
    result2 = no_guess(ran_no2, chances)

    if(result1<result2):
        print(f"First player {player1_name} won the game, \nBy {result2-result1} fewer guess.")

    elif(result1>result2):
        print(f"Second player {player2_name} won the game, \nBy {result1-result2} fewer guess.")

    else:
        print(f"Match is draw, Both player took same amount of guesses!!!")

if __name__ == "__main__":
    main()