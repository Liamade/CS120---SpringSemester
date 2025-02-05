"""
Liam Callahan
Number Guesser
February 2 2024
"""
#prerequisites
import random
import time
condition=(1)


#start
print("system starting...")
time.sleep(1)

#number.game
while condition==(1) or condition==(2):
    condition=(1)
    tries=(0)
    win_condition=(False)
    print("generating random rumber...")
    time.sleep(1.5)
    secret_number=(random.randint(1,100))
    print("--random number generated--")

    #guesser
    while condition==(1):
        invalidnum_condition=(True)
        user_txt=input("guess a number 1-100: ")

        #number.checker
        for x in range(1,101):
            if user_txt==(f"{x}"):
                invalidnum_condition=(False)
                if int(user_txt)==(secret_number):
                    win_condition=(True)
                    break
                elif abs(int(user_txt)-(secret_number))==(1):
                    tries+=1
                    tries_remaining=(7-tries)
                    print("---------------------------------------")
                    print("soooooo close")
                    print(f"tries remaining: {tries_remaining}")
                    print("---------------------------------------")
                    break
                elif (int(user_txt)-(secret_number))<(-30):
                    tries+=1
                    tries_remaining=(7-tries)
                    print("---------------------------------------")
                    print("wayyyy to low")
                    print(f"tries remaining: {tries_remaining}")
                    print("---------------------------------------")
                    break
                elif (int(user_txt)-(secret_number))>(30):
                    tries+=1
                    tries_remaining=(7-tries)
                    print("---------------------------------------")
                    print("wayyyy too high")
                    print(f"tries remaining: {tries_remaining}")
                    print("---------------------------------------")
                    break
                elif int(user_txt)>(secret_number):
                    tries+=1
                    tries_remaining=(7-tries)
                    print("---------------------------------------")
                    print("you're too high")
                    print(f"tries remaining: {tries_remaining}")
                    print("---------------------------------------")
                    break
                elif int(user_txt)<(secret_number):
                    tries+=1
                    tries_remaining=(7-tries)
                    print("---------------------------------------")
                    print("you're too low")
                    print(f"tries remaining: {tries_remaining}")
                    print("---------------------------------------")
                    break

        #invalid.response
        if invalidnum_condition==(True):
             print("--invalid response--")
             print("")
        
        #lose/win
        if win_condition==(True):
            print("")
            print("hooorayyy you won!")
            print("")
            while condition==(1):
                user_txt=input("play again? (y/n): ")
                if user_txt==("n") or user_txt==("no"):
                    print("")
                    condition=(3)
                if user_txt==("y") or user_txt==("yes"):
                    print("")
                    condition=(2)
        elif tries==(7):
            print("")
            print("oops ya failed")
            print(f"the number was: {secret_number}")
            print("")
            while condition==(1):
                user_txt=input("play again? (y/n): ")
                if user_txt==("n") or user_txt==("no"):
                    print("")
                    condition=(3)
                if user_txt==("y") or user_txt==("yes"):
                    print("")
                    condition=(2)


#shut.down
print("system shutting down...")
time.sleep(1)