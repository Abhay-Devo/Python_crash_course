"""The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi-
score whenever the game() function breaks the Hi-score..."""


import random

def game():

    with open("ch_9_practice_prob_result.txt") as hiscore_file:
        hiscore = hiscore_file.read()

    score = random.randint(1, 50)

    if(hiscore!=""):
        hiscore = int(hiscore)
    else:
        hiscore = 0
    
    if(score > hiscore):
        print("Your New high score is:", score)
        with open("ch_9_practice_prob_result.txt", "w") as f:
            f.write(str(score))

    else:
        print(f"Your current score is: {score}, and your current high score is {hiscore}")


game()

