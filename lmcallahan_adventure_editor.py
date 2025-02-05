"""
Liam Callahan
Adventure Editor
February 23 2024
"""

#CONDITIONS
import json
condition=1
break_condition=False
#GAME FILES
game_files={
    }
#where i am supposed to have the json file and then load json file into game files


#GAME EDITOR/CREATOR SELECTOR
def gameFilesEditor():
    #file.selector
    while condition==1:
        #game.files.showcase
        showallgames()
        print("back(B)")
        print("")
        user_input=input(f"{username}: ")
        #file.selected
        for key in game_files:
            #active.file
            if user_input==(f"{key}"):
                game_file_active_edited=(f"{key}")
                #gameEditor
                gameEditor(game_file_active_edited)
                break
        #file.creation
        if user_input==("n") or user_input==("new save"):
            createGame()
        #exit
        elif user_input==("b") or user_input==("back"):
            break
        else:
            print("invalid input")
            print("")
            print("")
#GAME CREATOR
def createGame():
    user_input=input("NEW SAVE NAME: ")
    #save.name
    new_game= {
        (f"{user_input}"):{
        }
        }
    #add.dictionary.to.gamefiles
    game_files.update(new_game)

#GAME EDITOR
def gameEditor(x):
    game_file_active_edited=(f"{x}")
    #showcase
    editor_selection= """
         1) add new node
         2) edit current nodes
         3) show all nodes
         4) back"""
    #selection
    while condition==1:
        print("------------------------------")
        print(editor_selection)
        print("------------------------------")
        user_input=input(f"{username}: ")
        #adding.node
        if user_input=="1":
            addNode(x)
        #editing.node
        elif user_input=="2":
            editNode(x)
        elif user_input=="3":
            allNodes(x)
        elif user_input==("4"):
            break
        else:
            print("invalid input")
                                          

        
      
            
#ALL NODES
def allNodes(x):
    for keys in (game_files[f"{x}"]):
        print("-------------")
        print(keys)
        print("-------------")

def showallgames():
    #showing files
    for key in game_files:
        print("     ----------------")
        print(f"         {key}      ")
        print("     ----------------")
    print("     ----------------")
    print("        new save(N)  ")
    print("     ----------------")

#ADD NODE
def addNode(x):
    game_file_active_edited=(f"{x}")
    #node.creation
    node_name = input("node name: ")
    node_description = input("description: ")
    node_choice_a = input("choice A: ")
    node_choiceA_node = input("choice A output: ")
    node_choice_b = input("choice B: ")
    node_choiceB_node = input("choice B output: ")
    #node.created
    new_node={
        f"{node_name}" : {
            
            "question": f"{node_description}",
        
            "choice_a" : {
                "description": f"{node_choice_a}",
                "choice_output": f"{node_choiceA_node}"
                },
            
            "choice_b" : {
                "description": f"{node_choice_b}",
                "choice_output": f"{node_choiceB_node}"
                }
        }
        }
    #add.new.node.to.file(dictionary)
    game_files[f"{x}"].update(new_node)
    print(f"{node_name} saved to {x}")
    print("")
    
#EDIT FIELDS
def editNode(x):
    game_file_active_edited=(f"{x}")
    while condition==1:
        print("NODE EDITOR")
        allNodes(game_file_active_edited)
        print("back(B)")
        print("---------------")
        print("")
        user_input=input(f"{username}: ")
        for key in (game_files[f"{x}"]):
            if user_input==(f"{key}"):
                the_key=(f"{key}")
                question=(game_files[game_file_active_edited][f"{key}"]["question"])
                choiceA=(game_files[game_file_active_edited][f"{key}"]["choice_a"]["description"])
                choiceAnode=(game_files[game_file_active_edited][f"{key}"]["choice_a"]["choice_output"])
                choiceB=(game_files[game_file_active_edited][f"{key}"]["choice_b"]["description"])
                choiceBnode=(game_files[game_file_active_edited][f"{key}"]["choice_b"]["choice_output"])
                print("-----------------------------------------")
                print(f"(q)question: {question}")
                print(f"(a)choice A: {choiceA}")
                print(f"(an)choice A Node: {choiceAnode}")
                print(f"(b)choice B: {choiceB}")
                print(f"(bn)choice B Node: {choiceBnode}")
                print("-----------------------------------------")
                print("exit(e)")
                print("-----------------------------------------")
                while condition==1:
                    user_input=input("field: ")
                    if user_input==("question") or user_input==("q"):
                        user_input=input("new value: ")
                        game_files[game_file_active_edited][the_key].update({"question" : f"{user_input}"})
                        print("new value saved")
                        break
                    elif user_input==("a"):
                        user_input=input("new value: ")
                        game_files[game_file_active_edited][the_key]["choice_a"].update({"description" : f"{user_input}"})
                        print("new value saved")
                        break
                    elif user_input==("an"):
                        user_input=input("new value: ")
                        game_files[game_file_active_edited][the_key]["choice_a"].update({"choice_output" : f"{user_input}"})
                        print("new value saved")
                        break
                    elif user_input==("b"):
                        user_input=input("new value: ")
                        game_files[game_file_active_edited][the_key]["choice_b"].update({"desciption" : f"{user_input}"})
                        print("new value saved")
                        break
                    elif user_input==("bn"):
                        user_input=input("new value: ")
                        game_files[game_file_active_edited][the_key]["choice_b"].update({"choice_output" : f"{user_input}"})
                        print("new value saved")
                        break
                    elif user_input==("e"):
                        break
                    else:
                        print("invalid input")
                        print("")
                    
        if user_input==("b"):
            break

def defaultGame():
    while condition==1:
        print("do you want to win or lose?")
        default_options= """
            1) win
            2) lose"""
        print(default_options)
        user_input=input(f"{username}: ")
        if user_input==("1"):
            print("hooooray you won! play again?(y/n)")
            user_input=input(f"{username}: ")
            if user_input==("y"):
                print("another one")
            if user_input==("n"):
                break
        if user_input==("2"):
            print("ooops ya lost! play again?(y/n)")
            user_input=input(f"{username}: ")
            if user_input==("y"):
                print("another one")
            if user_input==("n"):
                break
        
def saveGame():
    while condition==1:
        #game.files.showcase
        showallgames()
        print("back(B)")
        print("")
        user_input=input(f"{username}: ")
        #file.selected
        for key in game_files:
            #active.file
            if user_input==(f"{key}"):
                key=(f"{key}")
                with open(f"{key}.json", "a") as file:
                    print("idk what to do")
                    #where im supposed to save it to a json file

#MAIN
print("adventure editor starting...")
print("")
username=input("username: ")
print("hi {username}, what would you like to do?")
print("")

while condition==1:
    main_selector= """
        1) create/edit game
        2) play default game
        3) play created game
        4) save game
        5) quit
    """
    print("------------------------------")
    print(main_selector)
    print("------------------------------")
    user_input=input(f"{username}: ")
    
    if user_input==("1"):
        gameFilesEditor()
    
    elif user_input==("2"):
        defaultGame()
        
    #PLAY LOCAL GAME
    elif user_input==("3"):
        while condition==1:
            #game.files.showcase
            showallgames()
            print("back(B)")
            print("")
            user_input=input("GAME: ")
            if user_input==("b"):
                break
            for key in game_files:
                #active.file
                if user_input==(f"{key}"):
                    while condition==1:
                        if break_condition==True:
                            break
                        elif break_condition==False:
                            game_file_active=(f"{key}")
                            game_file_key=("start")
                            while condition==1:
                                if game_file_key==("lose"):
                                    print("oops ya lost! play again?(y/n)")
                                    user_input=input(f"{username}: ")
                                    if user_input==("y"):
                                        break
                                    elif user_input==("n"):
                                        break_condition=True
                                        break
                                elif game_file_key==("win"):
                                    print("yayyy you won! play again?(y/n)")
                                    user_input=input(f"{username}: ")
                                    if user_input==("y"):
                                        break
                                    elif user_input==("n"):
                                        break_condition=True
                                        break
                                else:
                                    question=(game_files[game_file_active][game_file_key]["question"])
                                    choiceA=(game_files[game_file_active][game_file_key]["choice_a"]["description"])
                                    choiceAnode=(game_files[game_file_active][game_file_key]["choice_a"]["choice_output"])
                                    choiceB=(game_files[game_file_active][game_file_key]["choice_b"]["description"])
                                    choiceBnode=(game_files[game_file_active][game_file_key]["choice_b"]["choice_output"])
                                    print(question)
                                    print("")
                                    print(f"1) {choiceA}")
                                    print(f"2) {choiceB}")
                                    user_input=input(f"{username}: ")
                                    if user_input==("1"):
                                        game_file_key=(f"{choiceAnode}")
                                    elif user_input==("2"):
                                        game_file_key=(f"{choiceBnode}")
                    break_condition=False
                        
    elif user_input==("4"):
        print("hello")
    elif user_input==("5"):
        break
    else:
        print("invalid input")
        print("")