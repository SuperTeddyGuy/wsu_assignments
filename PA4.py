# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 14:50:46 2016

@author: Teddy
"""

import time
import random

def random_phrases(tipo):
    '''
    This function chooses random phrases to interact with the player
    '''
    #tipo = type of sentence (win(1), loss(2))
    rand = random.randrange(1, 4)
    if tipo == 1:
        if rand == 1:
            print("Nice one! Double the money, double the fun!")
        elif rand == 2:
            print("What luck! Try another one, and make it double!")
        else:
            print("Congratiulations, you won!")
    if tipo == 2:
        if rand == 1:
            print("Shame... Try again, you definetely are wining the next one!")
        elif rand == 2:
            print("Unlucky, but the next one is yours!")
        else:
            print("Awwnn... Just try again, you surely will make your money back!")
    

def display_game_rules():
    print("RULES:\n A player rolls two dice.\n Each die has six faces.\n These faces contain 1, 2, 3, 4, 5, and 6 spots.\n After the dice have come to rest, the sum of the spots on the two upward faces is calculated.\n If the sum is 7 or 11 on the first throw, the player wins.\n If the sum is 2, 3, or 12 on the first throw (called -craps-), the player loses (i.e. the -house- wins).\n If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, then the sum becomes the player's -point.-\n To win, you must continue rolling the dice until you -make your point-.\n The player loses by rolling a 7 before making the point.")

def get_bank_balance():
    bank = 0
    while bank <= 0:
        bank = float(input("Please enter the value to add to the bank balance: $"))
        if bank <= 0:
            print("Please enter a value that is above $0.")
    return bank

def get_wager_amount():
    wager = -1
    while wager <= 0:
        wager = float(input("Please enter the wager(bet): $"))
        if wager <= 0:
            print("Please enter a value that is above $0.")
    return wager

def is_valid_wager_amount(wager, balance):
    if wager > balance:
        print("You do not have that much money to bet. \nPlease enter a value that is equal or lower to the money you have.")
        return False
    else:
        print("Valid amount")
        return True

def roll_die():
    '''
    Calcs the number of the die, randomly.
    '''
    roll = random.randrange(1, 7)
    return roll

def calculate_sum_dice(die1_value, die2_value):
    '''
    Calculates the sum of the dice together.
    '''
    sum_dice = die1_value + die2_value
    return sum_dice

def is_win_loss_or_point(sum_dice):
    '''
    Sees if the sum of both dice results on a win, loss or a point.
    '''
    if sum_dice == 7 or sum_dice == 11:
        print(random_phrases(1))
        return 'win'
        
    elif sum_dice == 2 or sum_dice == 3 or sum_dice == 12:
        print(random_phrases(2))
        return 'loss'
    
    else:
        print("You better make your point to win!")
        return 'point'

def is_point_loss_or_neither(sum_dice, point_value, wager):
    '''
    Sees if the player will win (getting the point value), lose (getting a 7), or keep playing (getting anything else).
    '''
    while sum_dice != 7 or sum_dice != point_value:
        die1 = roll_die()
        print("die1: %d" % (die1))
        die2 = roll_die()
        print("die2: %d" % (die2))
        print("die1: %d die2: %d" %(die1, die2))
        sum_dice = calculate_sum_dice(die1, die2)
        print("sum: %d" %(sum_dice))
        time.sleep(1)
        
        if sum_dice == 7:
            print(random_phrases(2))
            return 'loss'
            
        elif sum_dice == point_value:
            print(random_phrases(1))
            return 'win'

def calc_results(bank, wager, wlp):
    if wlp == 'win':
        bank += wager
        print("You got: %.2f\nTotal bank: %.2f" % (wager * 2, bank))
        return bank
    elif wlp == 'loss':
        bank -= wager
        print("You lost: %.2f\nTotal bank: %.2f" % (wager, bank))
        return bank   
    
def main():
    display_game_rules()
    play_again = 'y'
    while play_again == 'y':
        bank = get_bank_balance()
        run_flag = True
        while run_flag and bank > 0:
            wager = get_wager_amount()
            run_flag = is_valid_wager_amount(wager, bank)
            if run_flag:
                die1 = roll_die()
                die2 = roll_die()
                print("die1: %d die2: %d" %(die1, die2))
                sum_dice = calculate_sum_dice(die1, die2)
                print("sum: %d" %(sum_dice)) 
                #wlp = Win, loss or point; It determines if it is necessary to call the 'is_point_loss_or_neither' function. It them determines how to calculate the results for the play.
                wlp = is_win_loss_or_point(sum_dice)
                if wlp == 'point':
                    point = sum_dice
                    wlp = is_point_loss_or_neither(sum_dice, point, wager)
                bank = calc_results(bank, wager, wlp)
                time.sleep(1)
            else:
                run_flag = True
            
        time.sleep(1)
        if bank == 0:
            play_again = str(input("Looks like you are out of money...\nDo you wish to add more money to your bank so you can keep playing? (y/n)"))
    
main()