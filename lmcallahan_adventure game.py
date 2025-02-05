# -*- coding: utf-8 -*-
"""
Liam Callahan
February 16 2024
Adventure Game
"""
#prerequisites
condition=1
condition_1=1
exit_condition=False
shutdown_condition=False

#choices

def choice1():
    print("you fall down into a pit into a bed of flowers")
    print("a flower props up and begins to talk")
    print("do you wish to talk to it?")
    print("1: yes")
    print("2: no")
    while condition == 1:
        userinput= input("user: ")
        
        if userinput == ("1"):
            choice2()
            break
            
        elif userinput == ("2"):
            choice3()
            break
        else:
            print("invalid input")

def choice2():
    print("flowey: howdy, I'm flowey")
    print("flowey: what's your name?")
    print("1: tell name")
    print("2: yell wtf you're a talking flower")
    while condition == 1:
        userinput= input("user: ")
        
        if userinput == ("1"):
            print("flowey: yes :)")
            choice4()
            break
            
        elif userinput == ("2"):
            print("tell name")
            choice4()
            break
        
        else:
            print("invalid input")
    
        
def choice3():
    print("you run deep into the cave and discover two opening.  Which one do you go down")
    print("1: the warm one")
    print("2: the cold one")
    while condition==1:
        userinput= input("user: ")
        
        if userinput == ("2"):
            choice5()
            break
            
        elif userinput == ("1"):
            print("as you walk into the dark warm tunnel a jet of fire consumes you, killing you")
            break
        
        else:
            print("invalid input")

def choice4():
    print("flowey: could you please give me a hug?")
    print("1: yes")
    print("2: no and run away")
    while condition==1:
        userinput= input("user: ")
        
        if userinput == ("1"):
            print("oops ya lost, better luck next time")
            print("play again?(y/n)")
            while condition==1:
               userinput=input("user:")
               if userinput==("y"):
                   break
               elif userinput==("n"):
                   exit_condition=True
                   break
            break
        elif userinput == ("2"):
            choice3()
            break
        
        else:
            print("invalid input")

def choice5():
    print("you run down the cool path and see a faint glow ahead")
    print("as you make ur way into the cavern you see a glowing sword atop a rock in the middle")
    print("do you take the sword?")
    print("1: yes")
    print("2: no, check the other tunnel")
    while condition==1:
        userinput= input("user: ")
        
        if userinput == ("1"):
            choice6()
            break
            
        elif userinput == ("2"):
            print("as you walk into the dark warm tunnel a jet of fire consumes you, killing you")
            print("oops ya lost, better luck next time")
            print("play again?(y/n)")
            while condition == 1:
               userinput=input("user:")
               if userinput==("y"):
                   break
               elif userinput==("n"):
                   break
            break
        else:
            print("invalid input")
def choice6():
    print("with the sword in hand you feel powerful")
    print("do you check the other tunnel or go back to flowey")
    print("1: check other tunnel")
    print("2:return to flowey")
    while condition==1:
        userinput= input("user: ")
        
        if userinput == ("1"):
            print("as you walk into the dark warm tunnel a jet of fire consumes you, killing you")
            print("oops ya lost, better luck next time")
            print("play again?(y/n)")
            while condition == 1:
                userinput=input("user:")
                if userinput==("y"):
                    break
                elif userinput==("n"):
                    break
            break
        elif userinput == ("2"):
            choice7()
            break
        
        else:
            print("invalid input")
def choice7():
    print("as you return to flowey again he begins to talk")
    print("flowey: are you back to give me a hug?")
    print("1: yes")
    print("2: no chop him down")
    while condition==1:
        userinput= input("user: ")
        
        if userinput == ("1"):
            print("oops ya lost, better luck next time")
            print("play again?(y/n)")
            while condition == 1:
                userinput=input("user:")
                if userinput==("y"):
                    break
                elif userinput==("n"):
                    break
            break
        elif userinput == ("2"):
            print("yayyy you won!")
            print("play again?(y/n)")
            while condition == 1:
                userinput=input("user:")
                if userinput==("y"):
                    break
                elif userinput==("n"):
                    break
                   
        else:
            print("invalid input")

def main():
    print("welcome to amazing adventure game")
    while condition==1:
        if exit_condition==True:
            break
        userinput=input("do you want to begin? (y/n):")
        if userinput=="y":
            while condition==1:
                if exit_condition==True:
                    break
                choice1()
        elif userinput=="n":
            print("okay goodbye")
            break
        else:
            print("invalid input")
    

main()
                    
        
    
