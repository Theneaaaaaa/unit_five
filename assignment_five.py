# Thenea Sun
# Oct. 11th
# This is a program which  simulate multiple instances of a game of craps to see what percentage of the time the player
# wins and what percentage of the time the house (the casino) wins.


import random


def roll_the_dice():
    number = random.randint(1, 6)
    return number
# get a random number in range 1 to 6, in order to simulate the dice


def re_roll():
    number = roll_the_dice()
    return number


def main():
    time_to_simulate = int(input("How many times would you like to simulate?"))
    win_time = 0
    for x in range(time_to_simulate):
        dice1 = roll_the_dice()
        dice2 = roll_the_dice()
        dice_total = dice1 + dice2
        if dice_total == 7 or dice_total == 11:
            win_time = win_time + 1
        elif dice_total == 2 or dice_total == 3 or dice_total == 12:
            pass
        # pass it pass it!
        else:
            dice3 = roll_the_dice()
            dice4 = roll_the_dice()
            dice_total1 = dice3 + dice4
            while dice_total1 != 7 and dice_total1 != dice_total:
                # The while loop is needed here for the situation when dice total does not equals to the number
                dice3 = roll_the_dice()
                dice4 = roll_the_dice()
                dice_total1 = dice3 + dice4
            if dice_total1 == dice_total:
                win_time = win_time + 1
    win_rate = win_time / time_to_simulate * 100
    print("You played", time_to_simulate, "times, you won", win_time, "times and lost", time_to_simulate - win_time, ".")
    print("you won", win_rate, "percent of the time.")
    print("Good bye!")


main()









