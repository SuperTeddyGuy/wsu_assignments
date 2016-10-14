# -*- coding: utf-8 -*-
"""
Joao Victor "Teddy" Martins - 11537480
CptS 111-8108, Fall 2016
Programming Assignment #1
01/09/16
Lab Section 10

Program that "talks" to the user and compute some informations for him about numbers and cars.
"""
import time

print("DISCLAIMER: THIS CODE IS SUPOSED TO BE READ IN A BRITISH ACCENT.")
# time.sleep makes the code stop and continue for a specified ammount of seconds, used in here so the user can read without being bombarded with code
time.sleep(5)
print("(...) ...Greetings my friend! I didn't see you there! Come in my dear, lets have some tea and biscuits!\n")
time.sleep(3)
name = input("I'm terribly sorry, but I do not recall your name.\n What was it again my dear?\n")
print("I'm deeply sorry about this mistake %s! \n" % (name))
time.sleep(3)
print("As you probably do recall, my name is Charles Sherington, Duke of the Python Code.\n")
time.sleep(3)
print("If I do evoke correctly, you are from that lovely place called... called... Oh Bollocks.\n")
time.sleep(3)
print("You will have to forgive me again %s, but my age is not helping me with these memory endeavours.\n" % (name))
time.sleep(3)
city = input("Where did you say you were from again my dear?\n")
print("Oh, yes of course! Little %s! That ever-lovely place.\n" % (city))
time.sleep(3)

num = float(input("Anyhow, Blaine Lynch told me you are a big fan of numbers. \nIf I may ask, what happen to be your favourite one?\n"))
print("Oh %d! What an exquisite choice!\n" % (num))
time.sleep(3)

#times is determining if the number is bigger or smaller than Charles' favourite number
times = num / 42
if times > 1:
    print("If my math does not fail me at the moment, your favourite number, %d, is %.2f times bigger than mine, which is 42!\n" % (num, times))
    time.sleep(3)
if times < 1:
    print("If my math does not fail me at the moment, your favourite number, which is %d, is %.2f times smaller than mine, which is 42!\n" % (num, times))
    time.sleep(3)
if times == 1:
    print("Oh Dear, just noticed that it is the same as my favourite number, 42. How dandy!\n")
    time.sleep(3)

car = input("That was a lovely conversation, but if I do recall correctly, you are a big fan of cars. What was you model of choice again?\n")
print("Oh of course! The delightful %s! What a marvelous choice of automotive vehicle.\n" % (car))
time.sleep(3)
price = float(input("And what is the price tag on such feat of the mecchanical engineering world?\n"))
print("For a gentleman like me, %.2f would be no hastle dealing with, but you might have to deal with some filthy bankers ho ho ho!\n" % (price))
time.sleep(3)
rate = float(input("What would be the interest rate on such fine piece of machinery?\n"))
years = float(input("And for how many years do you pretend on paying?\n"))

final_rate = (rate / 100) / 12

#math1 calculates the upper part of the equation's fraction for calculating monthly payments and math2 the bottom part.
math1 = final_rate * price
math2 = 1 - (1 + final_rate) ** (-12 * years)
payment = math1 / math2

time.sleep(1)
print("Well my dear %s, if you desire The %s with a passion, you will have to make monthly payments of %.2f, something quite small by my eyes.\n" % (name, car, payment))
time.sleep(3)

cost = payment * 12 * years

print("The total would be %.2f, the same I spent with my colleagues when we go pigeon shooting at the club.\n" % (cost))
time.sleep(3)
print("Anyhow my dear, I have a meeting to attend at this moment, so if you excuse me I will withdraw myself from the room.\nHope to come in contact with you again my friend. Hopefully I will see you around these areas hunting or maybe having a cup of tea.")
time.sleep(3)
