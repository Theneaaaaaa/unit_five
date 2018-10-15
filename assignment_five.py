# Thenea Sun
# Oct. 11th
# This is a program which  simulate multiple instances of a game of craps to see what percentage of the time the player
# wins and what percentage of the time the house (the casino) wins.


import random


time_to_simulate = int(input("How many times would you like to simulate?"))


def roll_the_dice():
    number = random(1, 6)
    return number
# get a random number in range 1 to 6, in order to simulate the dice


def re_roll():
    number = roll_the_dice()
    return number


def roll_point(point):
    dice1 = roll_the_dice()
    dice2 = roll_the_dice()
    dice_total = dice1 + dice2
    while dice_total != 7 or dice_total != point:
        dice1 = roll_the_dice()
        dice2 = roll_the_dice()
        dice_total = dice1 + dice2
    if dice_total == point:
        return 1
    elif dice_total == 7:
        return 0


def judgement():
    dice1 = roll_the_dice()
    dice2 = roll_the_dice()
    dice_total = dice1 + dice2
    win_time = 0
    if dice_total == 7 or 11:
        win_time = win_time + 1
    elif dice_total == 2 or 3 or 12:
        win_time = win_time + 0
    else:
        win_time = win_time + roll_point(dice_total)












