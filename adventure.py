Lives = 3
Sword = False
Bones = True
Trap = True
lvl = 0
Orc = True
SwordBoss = False
def IntroScene():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    print("Welcome to the Dungeon! Your goal is to escape but beware there are monsters lurking.")
    ISAsk = input("You see a pathway. Go forward(yes/no)? ").lower()
    if ISAsk == "yes":
        Mainroom()
    elif ISAsk == "no":
        Lives -= 3
        print("As you wait for nothing, Monsters swarm in your little space and kills you.(Lives -3)")
        print(f"Lives: {Lives}")
        print("Game Over")
    elif ISAsk == "alainpogi":
        Lives += 1
        print("The creator smiles upon you giving you an extra life (Lives +1)")
        print("You proceed forwards.")
        Mainroom()

def Mainroom():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    print(f"Lives: {Lives}")
    print(f"Lvl: {lvl}")
    MRAsk = input("You enter a big room and see 3 pathways. Which will you enter(left/right/middle)? ").lower()
    if MRAsk == "left" and Bones == True:
        Skeleton()
    elif MRAsk == "left" and Bones == False:
        EmptyRoom()
    elif MRAsk == "right" and Trap == True:
        SwordRoom()
    elif MRAsk == "right" and Trap == False:
        EmptyRoom()
    elif MRAsk == "middle":
        MiddleRoom()

def Skeleton():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    Skele = input("You encounter a moving Skeleton. What will you do(fight/go back)? ").lower()
    if Skele == "fight" and Sword == False:
        Lives -= 1
        if Lives == 0:
            print("Game Over! Lives: 0")
        else:
            print("You fight the skeleton but it beats you.(Lives -1)")
            print("You return to the Mainroom")
            Mainroom()
    elif Skele == "go back":
        Mainroom()
    elif Skele == "fight" and Sword == True:
        Bones = False
        print("You slice the Skeleton with your sword and a path opens up.")
        lvl += 1
        print(f"Level Up! Lvl +1")
        ask = input("Will you enter or go back(enter/go back)? ").lower()
        if ask == "enter":
            HeartRoom()
        elif ask == "go back":
            Mainroom()

def SwordRoom():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    Lives -= 1
    print("You see a sword but as you pick it up, you were shot by an arrow trap.(Lives -1)")
    if Lives == 0:
        print("Game Over! Lives: 0")
    else:
        Trap = False
        Sword = True
        print("Sword Acquired!")
        print("You go back to the Mainroom.")
        Mainroom()

def HeartRoom():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    Lives += 1
    print("You gain an extra Heart!(Lives +1)")
    print("You return to the mainroom.")
    Mainroom()

def EmptyRoom():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    print("It is an empty room.")
    print("You went back to the main room.")
    Mainroom()

def MiddleRoom():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    print(f"Lives: {Lives}")
    print(f"Lvl: {lvl}")
    print("You encounter 3 new paths.")
    mid = input("Which way will you go(left/right/middle/go back)? ").lower()
    if mid == "left" and SwordBoss == False:
        Enchant()
    elif mid == "left" and SwordBoss == True:
        EmptyRoom1()
    elif mid == "right" and Orc == True:
        OrcRoom()
    elif mid == "right" and Orc == False:
        EmptyRoom1()    
    elif mid == "middle":
        BossRoom()
    elif mid == "go back":
        print("You return to the previous area.")
        Mainroom()

def OrcRoom():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    OF = input("You encounter an Orc. Will you fight it(yes/no)? ").lower()
    if OF == "yes" and Sword == True:
        Orc = False
        print("You've defeated an Orc!")
        lvl += 1
        print("Level Up! Lvl +1")
        print("You return to the previous room.")
        MiddleRoom()
    elif OF == "no":
        print("You return to the previous room.")
        MiddleRoom()
    elif OF == "yes" and Sword == False:
        Lives -= 1
        if Lives == 0:
            print("Game Over! Lives: 0")
        else:
            print("You fight the Orc but it beats you.(Lives -1)")
            print("You return to the previous room")
            MiddleRoom()

def Enchant():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    print("You see an Enchanment Table(1 use only and 2 Lvls required).")
    encha = input("Enchant your Sword(yes/no)? ").lower()
    if encha == "yes" and lvl == 2:
        print("Sword Successfully enchanted(More effective against Boss).")
        SwordBoss = True
        print("You return to the previous area.")
        MiddleRoom()
    elif encha == "no":
        print("You return to the previous room.")
        MiddleRoom()
    elif encha == "yes" and lvl != 2:
        print("Insufficient amount of Levels. You return to the previous room.")
        MiddleRoom()

def BossRoom():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    print("You enter a peculiar door. Once you've entered, the door closes leaving no room for escape.")
    BR = input("The Boss emerges from the shadows. What will you do(fight/run)? ").lower()
    if BR == "fight":
        if Sword == True and SwordBoss == True:
            print("You destroyed the Boss in one slice. YOU WIN!")
            Ending()
        elif Sword == True and SwordBoss == False:
            Lives -= 2
            print("You slice the boss but didn't deal enough damage. He retaliates(Lives -2).")
            if Lives <= 0:
                print("Game Over! Lives: 0")
            elif Lives > 0:
                print(f"Lives: {Lives}")
                ask2 = input("Will you fight again(yes/no)? ").lower()
                if ask2 == "yes":
                    print("You've finally slain the boss. YOU WIN")
                    Ending()
                if ask2 == "no":
                    print("It hits you as you flee dealing the finishing blow.")
                    print("Game Over! Lives: 0")
        elif Sword == False:
            print("You tried to hit it with your fists dealing no damage. He smashes you.")
            print("Game Over! Lives: 0")
    elif BR == "run":
        print("It hits you as you flee dealing the finishing blow.")
        print("Game Over! Lives: 0")

def EmptyRoom1():
    global Lives, Sword, Bones, Trap, lvl, Orc, SwordBoss
    print("It is an empty room.")
    print("You went back to the previous room.")
    MiddleRoom()

def Ending():
    end = input("An exit opens. Will you leave(yes/no)? ")
    if end == "yes":
        print("You've finally escaped the Dungeon and lived to tell the tale. The End")
    elif end == "no":
        print("The exit closes. You are left alone in this cold dark dungeon.")
        print("The dungeon appoints you as the new guardian.")
        print("You now defend the exit from lost travelers who wish to escape the dungeon. The End")

IntroScene()