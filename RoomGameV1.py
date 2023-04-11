rooms = {
    "Room1": {
        "description": "You are in the Room1. There is red door to the left and a green door to the right.",
        "directions": {"left": "Room2", "right": "Room3"},
        "items": [],
        "locked": False,
        "usable":[]
    },
    "Room2": {
        "description": "You are in the Room2. There is a yellow door to the right.",
        "directions": {"right": "Room1"},
        "items": ["red key","green key"],
        "locked": False,
        "usable":[]
    },
    "Room3": {
        "description": "You are in the Room3. There is a yellow door to the left and a dark door to the right",
        "directions": {"left": "Room1","right":"Room4"},
        "items": [],
        "locked": True,
        "usable":["green key","red key"]
    },
    "Room4":{
        "description": "You are in the Room4. Congratulations you Escaped :)",
        "directions":{},
        "items":[],
        "locked":False,
        "usable":[]
        }
}

inventaire = []
actualRoom = "Room1"
inExecution=True
command=[] # les commandes possibles
while inExecution is True:
    command.clear() # clear le tableau des commandes possibles
    
    for i in rooms[actualRoom]["directions"].keys():
        command.append(i)# ajouter les commandes possibles
    
    print("\n")
    print(rooms[actualRoom]["description"]) # description de la salle où est le joueur
    print("\n")
    print("Your Items:", inventaire)
    print("Room Items:", rooms[actualRoom]["items"]) # les items dans la piece
    print("Directions:", command) # les sortie possibles

    
    userMessage = input("\x1b[38;5;11m\nWhat do you want to do? \x1b[0m") # le message du joueur
    
    
    
    
    if userMessage == "quit":
        inExecution = False
        break
    
    
    if userMessage in rooms[actualRoom]["directions"]:# si l'utilisateur a entrée une commande valide
        nextRoom = rooms[actualRoom]["directions"][userMessage]
        
        #if rooms[nextRoom]["locked"] and "green key" not in inventaire:
        if rooms[nextRoom]["locked"] and not set(rooms[nextRoom]["usable"]).intersection(inventaire):
        #if (rooms[nextRoom]["locked"] and not (inventaire)):
            print("\x1b[3m\x1b[38;5;10mThe door is locked.\x1b[0m") # text en vert + italic
        else:
            actualRoom = nextRoom # on passe dans la salle suivante
            if rooms[nextRoom]["locked"]==True: # si la piece où on va est fermé
                for item in rooms[nextRoom]["usable"]:
                    if item in inventaire:
                        inventaire.remove(item)
                #inventaire.remove(inventaire[0]) # la cles ne peut plus etre utilisée
                rooms[nextRoom]["locked"] = False # la salle est maintenant tout le tant ouverte
                #print("\x1b[3m\x1b[38;5;10m-->You unlocked the door with the key.\x1b[0m")
                print("\x1b[3m\x1b[38;5;10m-->You unlocked the door with the key.\x1b[0m")
                
            if actualRoom == "Room4":# si on est dans la Room4 on a gagné on sort du programme
                print("\n",rooms[actualRoom]["description"])
                break
            
    #elif userMessage == "take key" and "green key" in rooms[actualRoom]["items"]: # si l'utilisateur ecrit take key et que ya une cles
    
    elif userMessage == "take key": # la commande take key est entrée
        detected=[x for x in rooms[actualRoom]["items"] if "key" in x] # regarde si les objet dedans c'est une cles
        if detected: # si ya un truc dans detected
            rooms[actualRoom]["items"].remove(detected[0]) # on enleve la cles dans la salle
            inventaire.append(detected[0]) # on ajoute la cles a l'inventaire du joueur
            print("\x1b[3m\x1b[38;5;10m-->You took an item.\x1b[0m")
        else: # ya pas de cles dans la salle
            print("\x1b[1m\x1b[38;5;1mThere is no key in here.\x1b[0m")
            
    elif userMessage == "help":
        print("You can use many commands to interact\n"
              +"take [anObject]: take an item\n"
              +"quit: quit the game\n and many other")
    
    else:
        print("\x1b[1m\x1b[38;5;1mINVALID COMMAND\x1b[0m")# Affiche en rouge Invalid command
    
    

