# -*- coding: utf-8 -*-
"""
Liam Callahan
Knock Knock Joke
January 19, 2024
"""

firstname = input("What is your name? ")
output = f"""Hi, {firstname} do you want to hear a joke? (y/n): """

answer = input(output)

if answer == "y":
        whos_there = input("knock knock: ")
        if whos_there == "who's there?":
            boowho = input("boo: ")
            if boowho == "boo who":
                print("No need to cry")
            else:
                imsorry = input("you did it wrong :( : ")
                if imsorry == "im sorry":
                    print("its okay <3")
                    answer1 = input("do you want me to start over? (y/n): ")
                    if answer1 == "y":
                        whos_there = input("knock knock: ")
                        if whos_there == "who's there?":
                            boowho = input("boo: ")
                            if boowho == "boo who":
                                print("No need to cry")
                            else:
                                print("im done")
                        else:
                            print("im done")
                    else:
                        print("good i didn't even want to tell you anyways")
                else:
                    print("whatever")
        else:
            imsorry1 = input("you're supposed to say who's there: ")
            if imsorry1 == "im sorry":
                answer1 = input("do you want me to start over? (y/n): ")
                if answer1 == "y":
                    whos_there = input("knock knock: ")
                    if whos_there == "who's there?":
                        boowho = input("boo: ")
                        if boowho == "boo who":
                            print("No need to cry")
                        else:
                            print("im done")
                    else:
                        print("im done")
                else:
                    print("good i didn't even want to tell you anyways")
            else:
                print("you hurt my feelings :(")
                    
else:
    print("okay whatever, i don't even care")