# -*- coding: utf-8 -*-
"""
Programming Assignment 3
Quiz about topic of choice
@author: Joao Victor "Teddy" Martins
"""
# The functions get_qx shows the question to the user and gets a right or wrong value for it.
def get_q1():
    print("1) Which one of these characters was not part of the original Overwatch Squad?\nPlease enter a character a-e.")
    ans = str(input("a-Aleksandra Zaryanova\nb-Jack Morrison\nc-Ana Amari\nd-Reinhardt Wilhelp\ne-Gabriel Reyes\n"))
    if ans == 'a' or ans == 'A':
        print("Right Answer!")
        return 1
    else:
        print("Wrong Answer, the right one is (a)")
        return 0
        
def get_q2():
    print("2) How many were the members of the original Overwatch team? Please enter an integer.")
    ans = int(input())
    if ans == 7:
        print("Right Answer!")
        return 1
    else:
        print("Wrong Answer, the right number is 7")
        return 0
        
def get_q3():
    print("3) What was the original purpose of Overwatch?\nPlease enter a character a-e.")
    ans = str(input("a-Robots rebeled against humanity and we needed special forces to fight them.\nb-Humanity needed a team for global warming research.\nc-The Alliance needed forces to fight in a third world war.\nd-US needed a new Super Soldier Program\ne-Europe was in dire need of a new space program group.\n"))
    if ans == 'a' or ans == 'A':
        print("Right Answer!")
        return 1
    else:
        print("Wrong Answer, the right one is (a)")
        return 0   
        
def get_q4():
    print("4) Widowmaker's real name is Julie Lacroix, true or false?  Please enter 1 for True or 0 for False.")
    answer = bool(int(input()))
    if answer == False: 
        print("Right Answer, her real name is Amelie Lacroix") 
        return 1
    else: 
        print("Wrong Answer, her real name is Amelie Lacroix")
        return 0
        
def get_q5():
    print("5) How many maps are playable in the latest game build? Please enter an integer.")
    ans = int(input())
    if ans == 13:
        print("Right Answer!")
        return 1
    else:
        print("Wrong Answer, the right number is 13")
        return 0
        
def get_q6():
    print("6) Where is Mercy from?\nPlease enter a character a-e.")
    ans = str(input("a-USA\nb-Brazil\nc-China\nd-Switzerland\ne-Russia\n"))
    if ans == 'd' or ans == 'D':
        print("Right Answer!")
        return 1
    else:
        print("Wrong Answer, the right one is (d)")
        return 0 
        
def get_q7():
    print("7) Tracer is the one how says: 'Cheers love, the cavalry is here!', true or false?  Please enter 1 for True or 0 for False.")
    ans = bool(int(input()))
    if ans == True: 
        print("Right Answer, her real name is Amelie Lacroix") 
        return 1
    else: 
        print("Wrong Answer, her real name is Amelie Lacroix")
        return 0
        
def get_q8():
    print("8) With which organization is D-Va affiliated with?\nPlease enter a character a-e.")
    ans = str(input("a-The Shimada Clan\nb-The Mobile Exo-Force of the Korean Army (MEKA)\nc-Helix Security International\nd-Overwatch\ne-Talon\n"))
    if ans == 'b' or ans == 'B':
        print("Right Answer!")
        return 1
    else:
        print("Wrong Answer, the right one is (b)")
        return 0 
        
def get_q9():
    print("9) Why was Mei stuck in her Watchpoint for many years?\nPlease enter a character a-e.")
    ans = str(input("a-Because of the fall of the country she was located in.\nb-Because of her organization forgeting about her\nc-Because of a horrible snowstorm and the fall of Overwatch\nd-Because of the Omnic Crisis\ne-Because of lack of investment in emergency services in the area\n"))
    if ans == 'c' or ans == 'c':
        print("Right Answer!")
        return 1
    else:
        print("Wrong Answer, the right one is (c)")
        return 0
        
def get_q10():
    print("10)Jack Morrison was presumed dead in the fall of Overwatch, true or false?  Please enter 1 for True or 0 for False.")
    ans = bool(int(input()))
    if ans == True: 
        print("Right Answer, he was indeed presumed dead.") 
        return 1
    else: 
        print("Wrong Answer, he was indeed presumed dead.")
        return 0

#The show_res function sees in which category the user falls into, depending on how many answers he/she/it/they got it right.
def show_res(total):
    if total == 10:
        print("You got all of them right! Are you sure you are not an Overwatch member?")
    elif total >= 8:
        print("You got %d right! You are an Overwatch Expert!" % (total))
    elif total >= 6:
        print("You got %d right. You have some good knowledge about the Overwatch Lore." % (total))
    elif total >= 4:
        print("You got %d right. Well, you know some stuff about Overwatch (but not enough!)" % (total))
    elif total >= 2:
        print("You got %d right. You should look more into Overwatch, it's a cool game I swear!" % (total))
    else:
        print("You got %d right. Overwatch, ever heard of it?" % (total))        
        

def main():
    print("Welcome to the Overwatch quiz!")

#The ax variable stores a 1 or 0 value for each question, depending if it is right or wrong.
    a1 = get_q1()
    a2 = get_q2()
    a3 = get_q3()
    a4 = get_q4()
    a5 = get_q5()
    a6 = get_q6()
    a7 = get_q7()
    a8 = get_q8()
    a9 = get_q9()
    a10 = get_q10()
    total = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
    
    show_res(total)
    
    print("Thanks for doing the Overwatch quiz! Hope you enjoyed and remember, the world could always use more heroes!")
    
main()