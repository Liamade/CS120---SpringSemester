#eight.ball
"""
Liam Callahan
Magic Eightball
January 26 2024
"""
#prerequisites
import random
import time
fortune_list = ("no","yes","maybe","i don't know","probably not","for sure","definitely not","try again")
number_range = ("1","2","3","4","5","6","7","0")
condition = (1)

#extra.functions
def helpsequence():
    time.sleep(1)
    print("----------------------------------------------------------------------------------------")
    print("p -- print")
    print("     -application that allows user to print specific fortune")
    print("pa -- print all")
    print("     -application that prints all fortunes")
    print("c -- calculator")
    print("     -application that determines probablity of question and converts it into a fortune")
    print("q -- quit")
    print("     -exits application")
    print("sd -- shutdown")
    print("     -shuts the system down")
    print("h -- help")
    print("     -shows various commands and applications")
    print("----------------------------------------------------------------------------------------")
def menuselector():
    time.sleep(1)
    print("----------------------------------------------------------------------------------------")
    print("print                                 print all                               calculator")
    print("----------------------------------------------------------------------------------------")
def shutdown():
    print("fortune teller 5000 shutting down...")
    time.sleep(2)
    print(f"goodbye {username}.")
 #main.functions   
def fortuneprint():
    time.sleep(1)
    print("----------------------------------------------------------------------------------------")
    print(fortune_list[int(fortuneselect)])
    print("----------------------------------------------------------------------------------------")
def fortuneteller():
    print("processing probability...")
    time.sleep(2)
    yourfortune = (random.choices(fortune_list))
    print("----------------------------------------------------------------------------------------")
    print(f"                                {yourfortune}")
    print("----------------------------------------------------------------------------------------")
def printall():
    time.sleep(2)
    for i, fortune in enumerate(fortune_list):
        print(f"{i} {fortune}")
    
    

#boot up
print("fortune teller 5000 starting...")
time.sleep(2)
username = input("username: ")
print(f"welcome {username}.")
menuselector()

#system running
while condition == (1):
        commandinput = input(f"{username}: ")
       
        #command.help
        if commandinput == ("help") or commandinput == ("h"):
            helpsequence()
        
        #app.help
        elif commandinput == ("print") or commandinput == ("p"):
            print("||||||||||||||||||||||||||||||||||||||PRINT|||||||||||||||||||||||||||||||||||||||||||||")
            while condition == (1):
                print("please select a number (0-7)")
                fortuneselect = (input(f"{username}: "))
                if fortuneselect in (number_range):
                    fortuneprint()
                elif fortuneselect == ("quit") or fortuneselect == ("q"):
                    print("shutting print off...")
                    menuselector()
                    break
                elif fortuneselect == ("help") or fortuneselect == ("h"):
                    helpsequence()
                elif fortuneselect == ("shutdown") or fortuneselect == ("sd"):
                    shutdown()
                    condition = (2)
                else:
                    print("*uknown input*")
        
        #app.print all       
        elif commandinput == ("print all") or commandinput == ("pa"):
            print("||||||||||||||||||||||||||||||||||||||PRINT ALL|||||||||||||||||||||||||||||||||||||||||")
            time.sleep(2)
            printall()
        
        #app.calculator
        elif commandinput == ("calculator") or commandinput == ("c"):
            print("||||||||||||||||||||||||||||||||||||||CALCULATOR||||||||||||||||||||||||||||||||||||||||")
            print("")
            while condition == (1):
                print("please ask a question")
                commandinput = input(f"{username}: ")
                if commandinput == ("help") or commandinput == ("h"):
                    helpsequence()
                elif commandinput == ("quit") or commandinput == ("q"):
                    print("shutting calculator off...")
                    menuselector()
                    break
                elif commandinput == ("shutdown") or commandinput == ("sd"):
                   shutdown()
                   condition = (2)
                else:
                    fortuneteller()
        
        #command.shutdown
        elif commandinput == ("shutdown") or commandinput == ("sd"):
            shutdown()
            condition = (2)
       
        #misinput    
        else:
            print("*uknown input*")
            