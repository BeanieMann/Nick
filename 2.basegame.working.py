import time
import random

Battle=""

                                        #FIGHTING STATS

catch=""
adv=""
fight_count=0
Starter=""
Pokemon_out=""
Pokemon_health=0.
Pokemon_max_health=0.
Pokemon_move={}
Pokemon_buff={}
Pokemon_debuff={}
PokemonDefeMulti=1.
PokemonAtkMulti=1.

                                        #POKEMON AND THEIR STARTER STATS/MOVES

Char_health=24.0
Char_health_max=24.0
Char_move={"Scratch":4.0,}
Char_buff={"Hone Claws":{"atk":1.25},}
Char_debuff={"Growl":{"atk":.75,},}
Bulb_health=20.0
Bulb_health_max=20.0
Bulb_move={"Tackle":5.0,}
Bulb_buff={"Flower Shield":{"def":1.25,},}
Bulb_debuff={"Tail Whip":{"def":.75,},}
Squirtle_health=16.0
Squirtle_health_max=16.0
Squirtle_move={"Headbutt":6.0,}
Squirtle_buff={"Swords Dance":{"atk":1.25},}
Squirtle_debuff={"Tail Whip":{"def":.75,},}

                                        #POKEDEX

Pokedex={"Charmander":"Charmander, the Lizard Pokemon. Charmander's health can be gauged by the fire on the tip of its tail, which burns intensely when it's in good health.","Bulbasaur":"Bulbasaur, the Seed Pokemon. A young Bulbasaur uses the nutriens from it's seed for the energy it needs to grow.","Squirtle":"Squirtle, the Tiny Turtle Pokemon. During battle, Squirtle hides in it's shell and sprays water at its opponent whenever it can.",}

                                        #ENEMIES AND STATS/MOVES

En_out=""
EnDefeMulti=1.0
EnAtkMulti=1.0

e_Party={}
e1_Party={"Bidoof":{"health":15.0,"move":{"attack":{"Bite":3.0}}}}
e2_Party={"Growlithe":{"health":18.0,"move":{"attack":{"Ember":4.0},"debuff":{"Leer":{"def":.8}}}},"Mareep":{"health":14.0,"move":{"attack":{"Thunder Shock":4.0},"buff":{"Charge":{"atk":1.2}}}}}
e3_Party={"Rattata":{"health":14.0,"move":{"attack":{"Crunch":4.0}}},"Zubat":{"health":14.0,"move":{"attack":{"Air Slash":4.0},"debuff":{"Screech":{"def":.75}}}},"Haunter":{"health":22.0,"move":{"attack":{"Lick":5.0},"buff":{"Curse":{"atk":1.25}},"debuff":{"Confuse Ray":{"atk":.75}}}}}
Rayquaza={"Rayquaza":{"health":50.0,"move":{"attack":{"Extreme Speed":5.5},"buff":{"Dragon Dance":{"atk":1.25}},"debuff":{"Scary Face":{"atk":.75}}}}}

                                        #BAG

Bag={"Potion":999.0,"Pokeball":5,}
Pokeball=5


                                        #CHOOSING STARTERS

def starter_choice():
    global Starter
    global Pokemon_out
    global Pokemon_health
    global Pokemon_move
    global Pokemon_buff
    global Pokemon_debuff
    global Pokemon_max_health
    Starter=raw_input("\nCharmander, Bulbasaur, or Squirtle? Type C for Charmander, B for Bulbasaur, and S for Squirtle.\n\n").title()
    if Starter=="C":
        Pokemon_out="Charmander"
        Pokemon_health=Char_health              #If the starter is Charmander, set all the player stats and moves to Charmander stats and moves
        Pokemon_move=Char_move
        Pokemon_buff=Char_buff
        Pokemon_debuff=Char_debuff
        Pokemon_max_health=Char_health_max
    elif Starter=="B":
        Pokemon_out="Bulbasaur"
        Pokemon_health=Bulb_health              #If the starter is Bulbasaur, set all the player stats and moves to Bulbasaur stats and moves
        Pokemon_move=Bulb_move
        Pokemon_buff=Bulb_buff
        Pokemon_debuff=Bulb_debuff
        Pokemon_max_health=Bulb_health_max
    elif Starter=="S":
        Pokemon_out="Squirtle"
        Pokemon_health=Squirtle_health              #If the starter is Squirtle, set all the player stats and moves to Squirtle stats and moves
        Pokemon_move=Squirtle_move
        Pokemon_buff=Squirtle_buff
        Pokemon_debuff=Squirtle_debuff
        Pokemon_max_health=Squirtle_health_max
    else:
        print "\nI don't quite understand... "              #Error handling
        starter_choice()
    Poke_name=raw_input("\nWhat would you like to name it? If would not like to name it, press r to continue\n\n")
    if Poke_name=="r":
        print "\nIf you say so..."
    else:
        Pokemon_out=Poke_name
        time.sleep(1)
        print "\nVery Well"
    time.sleep(3)
    print "\nProf Oak: Also, here are some Pokeballs and a Potion in case you need them!"
    time.sleep(4)
    print "Potion Added to bag!"
    print "5 Pokeballs Added to Bag!"
    time.sleep(3)
    print "\nProf Oak: Excellent choice, "+name+". Now that you have your very own Pokemon, let's have a battle!"
    time.sleep(3.5)
    pre_start_fight()


                                        #BEFORE 1ST FIGHT

def pre_start_fight():
    global Pokemon_out
    global PokemonAtkMulti
    global PokemonDefeMulti
    global EnDefeMulti
    global EnAtkMulti
    global Pokedex
    global e2_Party
    global e_Party
    global En_out
    global name
    global fight_count
    fight_count=1
    e_Party=e1_Party                        #Sets up enemy variables and randomly chooses which one to send out first
    En_out=random.choice(e_Party.keys())
    print "\nProfessor Oak sent out "+En_out+"!"
    time.sleep(1.5)
    print name+" sent out "+Pokemon_out+"!"
    time.sleep(1.5)
    Pokedex["Bidoof"]="Bidoof, The Plump Mouse Pokemon. It gnaws on trees and rocks with its strong front teeth and lives near the water."
    PokemonAtkMulti=1.0                     #Adds Pokedex Enrty
    PokemonDefeMulti=1.0
    EnAtkMulti=1.0
    EnDefeMulti=1.0
    fight()

                                        #POST 1ST FIGHT

def post_start_fight():
    global Battle
    global Starter
    global Bag
    global Pokemon_max_health
    global Pokemon_health
    if Battle=="W":
        time.sleep(1)
        if Starter=="C":                     #Determines which starter was chosen, and changes stats accordingly
            Pokemon_max_health=26.0
            Pokemon_health=26.0
            print "\nCharmander Leveled Up!"
            print "Max Health="+str(Pokemon_max_health)
        elif Starter=="B":
            Pokemon_max_health=22.0
            Pokemon_health=22.0
            print "\nBulbasaur Leveled Up!"
            print "Max Health="+str(Pokemon_max_health)
        elif Starter=="S":
            Pokemon_max_health=18.0
            Pokemon_health=18.0
            print "\nSquirtle Leveled Up!"
            print "Max Health="+str(Pokemon_max_health)
        time.sleep(2)
        Bag["Potion"]=999                               #Potion restocked and story continues
        print "You refilled your Potion!\n"
        time.sleep(1)
        text2()
    else:
        print "Man, that's pretty rough... losing the Tutuorial Fight like that..."
        time.sleep(2.5)
        print "I mean... "
        time.sleep(3.5)
        print "wow."
        time.sleep(3)
        ans=raw_input("Would you like to restart? I won't tell.").title()
        if ans=="Yes":
            print "Have fun"
            Bag={"Potion":15.0,"Pokeball":1,}
            if Starter=="C":
                Pokemon_health=24
            elif Starter=="B":
                Pokemon_health=20
            else:
                Pokemon_health=16
            time.sleep(3)
            text1()
        elif ans=="No":
            print "Well... Thanks for Playing!"
            quit()
        else:
            print "What?"
            post_start_fight()

                                        #PRE 2ND FIGHT

def pre_second_fight():
    global fight_count
    global Pokemon_out
    global PokemonAtkMulti
    global PokemonDefeMulti
    global EnAtkMulti
    global EnDefeMulti
    global Pokedex
    global e2_Party
    global e_Party
    global En_out
    global name
    fight_count=2
    e_Party=e2_Party                        #Sets up enemy variables and randomly chooses which one to send out first
    En_out=random.choice(e2_Party.keys())
    print "\nShady Homeless Dude sent out "+En_out+"!"
    time.sleep(2.5)
    print name+" sent out "+Pokemon_out+"!"
    time.sleep(2.5)
    Pokedex["Growlithe"]="Growlithe, the Puppy Pokemon. While loyal to its master, the Growlithe will drive away enemies by barking and biting."
    Pokedex["Mareep"]="Mareep, the Wool Pokemon. Mareep stores static eletricity in its wooly coat. "
    PokemonAtkMulti=1.0                     #Adds Pokedex Enrty
    PokemonDefeMulti=1.0
    EnDefeMulti=1.0
    EnAtkMulti=1.0
    fight()
    
                                        #POST 2ND FIGHT

def post_second_fight():
    global Battle
    global Starter
    global Pokemon_max_health
    global Pokemon_health
    if Battle=="W":    
        print "\nYou have defeated Shady Homeless Dude!"
        time.sleep(1)
        if Starter=="C":                     #Determines which starter was chosen, and changes stats and moves accordingly
            Pokemon_max_health=31.0
            Pokemon_health=31.0
            print "\nCharmander Leveled Up!"
            print "Max Health="+str(Pokemon_max_health)
            Pokemon_move["Scratch"]=5
            print "Scratch's Power Increased!"
            Char_buff["Defense Curl"]={"def":1.25}
            print "Charmander learned Defense Curl!"
        if Starter=="B":
            Pokemon_max_health=27.0
            Pokemon_health=27.0
            print "\nBulbasaur Leveled Up!"
            print "Max Health="+str(Pokemon_max_health)
            Pokemon_move["Tackle"]=6
            print "Tackle's Power Increased!"
            Bulb_buff["Growth"]={"atk":1.25}
            print "Bulbasaur learned Growth!"
        if Starter=="S":
            Pokemon_max_health=23.0
            Pokemon_health=23.0
            print "\nSquirtle Leveled Up!"
            print "Max Health="+str(Pokemon_max_health)
            Pokemon_move["Headbutt"]=7
            print "Headbutt's Power Increased!"
            Squirtle_buff["Defense Curl"]={"def":1.25}
            print "Squirtle learned Withdraw!"
        time.sleep(2)
        Bag["Potion"]=999                               #Potion restocked and story continues
        print "You refilled your Potion!"
        time.sleep(1)
        text3Hallway()
    else:
        print "\nBig oof"
        time.sleep(2)
        print "Welp..."
        time.sleep(3)
        print "I don't have time to let you try again..."
        time.sleep(3)
        print "So....."
        time.sleep(2)
        print "Better luck next time!"
        quit()

                                        #PRE 3ND FIGHT

def pre_third_fight():
    global fight_count
    global Pokemon_out
    global PokemonAtkMulti
    global PokemonDefeMulti
    global EnAtkMulti
    global EnDefeMulti
    global Pokedex
    global e3_Party
    global e_Party
    global En_out
    global name
    global adv
    fight_count=3
    e_Party=e3_Party                        #Sets up enemy variables and randomly chooses which one to send out first
    En_out="Rattata"
    print "\nNightmare Lady sent out "+En_out+"!"
    time.sleep(2.5)
    print name+" sent out "+Pokemon_out+"!"
    time.sleep(2.5)
    Pokedex["Rattata"]="Rattata, the Forest Pokemon. It likes cheese, nuts, fruits, berries, and stealing from STUPID travelers."
    Pokedex["Zubat"]="Zubat, the Blind Pokemon. Zubat lives in caves and hates to fly outside in daylight."
    Pokedex["Haunter"]="Haunter, the Gas Pokemon. Haunter can watch opponents by hiding in walls and slips through anything in its way."
    PokemonAtkMulti=1.0                     #Adds Pokedex Enrty
    PokemonDefeMulti=1.0
    if adv=="True":
        EnDefeMulti=.8
        EnAtkMulti=.8
    else:
        EnDefeMulti=1.0
        EnAtkMulti=1.0
    fight()
    
                                        #POST 3RD FIGHT

def post_third_fight():
    global Battle
    global Starter
    global Pokemon_max_health
    global Pokemon_health
    print "You have defeated Nightmare Lady!"
    time.sleep(1)
    if Starter=="C":                     #Determines which starter was chosen, and changes stats and moves accordingly
        Pokemon_max_health=40.0
        Pokemon_health=40.0
        print "\nCharmander Leveled Up!"
        print "Max Health="+str(Pokemon_max_health)
        Pokemon_move["Scratch"]=6
        print "Scratch's Power Increased!"
        Char_debuff["Smokescreen"]={"def":.75}
        print "Charmander learned Smokescreen!"
    if Starter=="B":
        Pokemon_max_health=35.0
        Pokemon_health=35.0
        print "\nBulbasaur Leveled Up!"
        print "Max Health="+str(Pokemon_max_health)
        Pokemon_move["Tackle"]=7
        print "Tackle's Power Increased!"
        Bulb_debuff["Tangle"]={"atk":.75}
        print "Bulbasaur learned Tangle!"
    if Starter=="S":
        Pokemon_max_health=30.0
        Pokemon_health=30.0
        print "\nSquirtle Leveled Up!"
        print "Max Health="+str(Pokemon_max_health)
        Pokemon_move["Headbutt"]=8
        print "Headbutt's Power Increased!"
        Squirtle_debuff["Splash"]={"atk":.75}
        print "Squirtle learned Splash!"
    time.sleep(3)
    Bag["Potion"]=999                               #Potion restocked and story continues
    print "You refilled your Potion!\n"
    time.sleep(1)
    text4()

                                        #PRE LAST FIGHT

def pre_last_fight():
    global fight_count
    global Pokemon_out
    global PokemonAtkMulti
    global PokemonDefeMulti
    global EnAtkMulti
    global EnDefeMulti
    global Pokedex
    global Rayquaza
    global e_Party
    global En_out
    global name
    fight_count=4
    e_Party=Rayquaza                     #Sets up enemy variables and starts fight
    En_out="Rayquaza"
    print "\nRayquaza has been Challenged!"
    time.sleep(2.5)
    print name+" sent out "+Pokemon_out+"!"
    time.sleep(2.5)
    Pokedex["Rayquaza"]="Rayquaza, the Sky High Pokemon. It flies in the ozone layer, way up high in the sky. Until recently, no one had ever seen it."
    PokemonAtkMulti=1.0                     #Adds Pokedex Enrty
    PokemonDefeMulti=1.0
    EnDefeMulti=1.0
    EnAtkMulti=1.0
    fight()
    
                                        #POST LAST FIGHT

def post_last_fight():
    global Pokeball
    global name
    global Pokemon_out
    global catch
    catch_chance=21         #Chance of catching the pokemon is 30 out of 100
    catch="False"
    print "*Rayquaza falls to the ground, weakened from the fight*"
    time.sleep(2)
    print "Now's my chance!"
    time.sleep(1.5)
    print "*You fumble through your bag and pull out "+str(Pokeball)+" Pokeballs*"
    time.sleep(3)
    while catch == "False":
        throw=random.randint(1,100)                 #Randomly chooses number 1-100, if number is less than or equal to the catch requirements, it will be caught. 
        print name+" threw a Pokeball!"
        time.sleep(2)
        print "ding"
        time.sleep(1)
        print "ding"
        time.sleep(2)
        if throw<=catch_chance:
            print "ding"
            time.sleep(3)
            print "DING!"
            time.sleep(3)
            print "Rayquaza Was Caught!"
            catch="True"
            pre_good_ending()
        else:
            print "Rayquaza Breaks Free!"            #Otherwise, you lose a Pokeball and try again untill you either catch it or run out of Pokeballs
            time.sleep(2)
            Pokeball=Pokeball-1
            if Pokeball==0:
                time.sleep(1)
                print "Rayquaza gets recovers and soars into the sky, and you run back with your Pokemon into the tower to escape the storm"
                time.sleep(3)
                bad_ending()
            else:
                print "You only see "+str(Pokeball)+" Pokeballs left on the ground"
                time.sleep(2)
                catch="False"
    
                                        #BASIC FIGHT FORMAT

def fight():
    global fight_count
    global Pokedex
    global Battle
    global Pokemon_out
    global Pokemon_health
    global Pokemon_max_health
    global Pokemon_move                     #look at all those variables
    global Pokemon_buff
    global Pokemon_debuff
    global PokemonAtkMulti
    global PokemonDefeMulti
    global e_Party
    global En_out
    global adv
    global En_health
    global EnAtkMulti
    global EnDefeMulti
    response=0
    response=raw_input("\nType the number next to the desired action to use.\n\n1. Fight \n2. Item \n3. Run\n\n")
    if response=="1":
        print "\nType the name of the attack to use. You can press R to Return to the Actions Menu.\n\nMoves:"
        for item in Pokemon_move:
            print item
        for item in Pokemon_buff:                   #Prints out all attacks, buffs, and debuffs that the user can choose from to make their attack
            print item
        for item in Pokemon_debuff:
            print item
        Attack=raw_input("\n").title()
        if Attack=="R":
            fight()
        print "\n"+Pokemon_out+" used "+Attack+"!"
        time.sleep(1)
        if Attack in Pokemon_move:                    #checks if attack is a damage move and then subtracts enemy health accordingly
            e_Party[En_out]["health"]=round(e_Party[En_out]["health"]-((Pokemon_move[Attack]*PokemonAtkMulti)/EnDefeMulti))
        elif Attack in Pokemon_buff:
            if "atk" in Pokemon_buff[Attack]:           #Checks if attack is a buff, then if it buffs atk multiplier or defense multiplier, and then multiplies it to the player.
                PokemonAtkMulti=PokemonAtkMulti*Pokemon_buff[Attack]["atk"]
                print Pokemon_out+" raised its Attack!"
                time.sleep(1)
            else:
                PokemonDefeMulti=PokemonDefeMulti*Pokemon_buff[Attack]["def"]
                print Pokemon_out+" raised its Defense!"
                time.sleep(1)
        elif Attack in Pokemon_debuff:
            if "atk" in Pokemon_debuff[Attack]:           #Checks if attack is a debuff, then if it debuffs atk multiplier or defense multiplier, and then multiplies it to the enemy.
                EnAtkMulti=EnAtkMulti*Pokemon_debuff[Attack]["atk"]
                print En_out+"'s Attack was lowered!"
                time.sleep(1)
            else:
                EnDefeMulti=EnDefeMulti*Pokemon_debuff[Attack]["def"]
                print En_out+"'s Defense was lowered!"
                time.sleep(1)
        else:
            print "\nThat's not an attack."
            time.sleep(1)                       #If attack is not any available option
            fight()
        if e_Party[En_out]["health"]<=0:
            print En_out+" has fainted!"        #If enemy has no health, will either prompt win, unless more pokemon on enemy party
            time.sleep(1)
            e_Party.pop(En_out)
            if e_Party=={}:
                print "\n       You Win!!!"
                time.sleep(3)
                Battle="W"
                if fight_count==1:
                    post_start_fight()
                elif fight_count==2:
                    post_second_fight()         #Checks which fight was played, and then brings player to appropriate area in story
                elif fight_count==3:
                    post_third_fight()
                elif fight_count==4:
                    post_last_fight()
            else:
                En_out=random.choice(e_Party.keys())
                if fight_count==2:
                    print "Shady Homeless Dude sent out "+En_out+"!"         #Checks which fight was played, and then brings player to appropriate area in story
                    EnDefeMulti=1.0
                    EnAtkMulti=1.0
                    time.sleep(1)
                    fight()
                elif fight_count==3:
                    if adv=="True":
                        print "Nightmare Lady sent out "+En_out+"!"             #If enemy still has pokemon in dictionary, it would pop out the fainted enemy and swap in a new one
                        EnDefeMulti=.8
                        EnAtkMulti=.8
                        time.sleep(1)
                        fight()
                    else:
                        EnDefeMulti=1.0
                        EnAtkMulti=1.0
                        time.sleep(1)
                        fight()
                else:
                    EnDefeMulti=1.0
                    EnAtkMulti=1.0
                    time.sleep(1)
                    fight()
        else:
            print "Enemy Health Remaining: "+str(e_Party[En_out]["health"])
            time.sleep(1)
            e_choice=random.choice(e_Party[En_out]["move"].keys())          #If enemy doesn't faint, then it randomly chooses between an damage move, buff, or debuff move
            if e_choice=="attack":
                eAttack=random.choice(e_Party[En_out]["move"]["attack"].keys())         #If damage, attack subtracts player health accordingly
                print En_out+" used "+eAttack+"!"
                time.sleep(1)
                Pokemon_health=round(Pokemon_health-((e_Party[En_out]["move"]["attack"][eAttack]*EnAtkMulti)/PokemonDefeMulti))
                if Pokemon_health<=0:
                    print Pokemon_out+" has fainted!"                    #If player dies, it brings them to the lose screen
                    Battle="L"
                    if fight_count==1:
                        post_start_fight()
                    elif fight_count==4:
                        print "Rayquaza gets back up and soars into the sky, and you run back into the tower to escape the storm"
                        time.sleep(3)
                        bad_ending()
                    else:
                        post_second_fight()
                else:
                    print Pokemon_out+" has "+str(Pokemon_health)+" Health Remaining"           #prints out health remaining
                    time.sleep(1)
                    fight()
            elif e_choice=="buff":
                eAttack=random.choice(e_Party[En_out]["move"]["buff"].keys())                   #If move is a buff, checks if it buffs attack or defense multiplier
                print En_out+" used "+eAttack+"!"
                time.sleep(1)
                if "atk" in e_Party[En_out]["move"]["buff"][eAttack]:
                    EnAtkMulti=EnAtkMulti*e_Party[En_out]["move"]["buff"][eAttack]["atk"]           #If attack, changes enemy attack multiplier
                    print En_out+"'s Attack was raised!"
                    time.sleep(1)
                else:
                    EnDefeMulti=EnDefeMulti*e_Party[En_out]["move"]["buff"][eAttack]["def"]         #If defense, changes enemy defense multiplier
                    print En_out+"'s Defense was raised!"
                    time.sleep(1)
            elif e_choice=="debuff":
                eAttack=random.choice(e_Party[En_out]["move"]["debuff"].keys())                 #If move is a buff, checks if it buffs attack or defense multiplier
                print En_out+" used "+eAttack+"!"
                time.sleep(1)
                if "atk" in e_Party[En_out]["move"]["debuff"][eAttack]:
                    PokemonAtkMulti=PokemonAtkMulti*e_Party[En_out]["move"]["debuff"][eAttack]["atk"]               #If attack, changes player attack multiplier
                    print Pokemon_out+"'s Attack was lowered!"
                    time.sleep(1)
                else:
                    PokemonDefeMulti=PokemonDefeMulti*e_Party[En_out]["move"]["debuff"][eAttack]["def"]         #If defense, changes player defense multiplier
                    print Pokemon_out+"'s Defense was lowered!"
                    time.sleep(1)
        fight()
    elif response=="2":
        print "\nType the name of the Item you would like to use. You can press R to Return to the Actions Menu.\n"
        for item in Bag:
            print item                          #prints keys in list of bag and asks for which key the player wants
        Item=raw_input("\n").title()
        if Item=="Potion":
            if Pokemon_health==Pokemon_max_health:
                print "\nYou can't heal your Pokemon at full health!"           #If Potion, checks if the health is already at max, and if not, it adds health until it hits the maximum
                fight()
            elif Pokemon_health<Pokemon_max_health:
                Pokemon_health=Pokemon_health+Bag["Potion"]
                if Pokemon_health>Pokemon_max_health:
                    Pokemon_health=Pokemon_max_health
                print "\nYou used a potion and recovered "+Pokemon_out+" to "+str(Pokemon_health)+" hitpoints!"
                Bag.pop("Potion")
                eAttack=random.choice(e_Party[En_out]["move"]["attack"].keys())         #Removes potion from bag and makes enemy use a random damage attack
                time.sleep(1)
                print En_out+" used "+eAttack+"!"
                time.sleep(1)
                Pokemon_health=round(Pokemon_health-((e_Party[En_out]["move"]["attack"][eAttack]*EnAtkMulti)/PokemonDefeMulti))
                print Pokemon_out+" has "+str(Pokemon_health)+" Health Remaining"
                time.sleep(1)
                fight()
                if Pokemon_health<=0:
                    print Pokemon_out+" has fainted!"           #Checks if player health is 0 and if so brings up lose screen
                    Battle="L"
                    if fight_count==1:
                        post_start_fight()
                    elif fight_count==4:
                        print "Rayquaza gets back up and soars into the sky, and you run back into the tower to escape the storm"
                        time.sleep(3)
                        bad_ending()
                    else:
                        post_second_fight()
            else:
                print Pokemon_out+" has "+str(Pokemon_health)+" Health Remaining"
                time.sleep(1)
                fight()
            fight()
        elif Item=="Pokeball":
            print "\nYou can't capture another trainer's Pokemon!"          #No real use in battles
            time.sleep(1)
            fight()
        elif Item=="Pokedex":
            print "\nPrint the name of the Pokemon that you would like to read about, otherwise press R\n"
            for item in Pokedex:
                print item
            Read=raw_input("\n").title()                    #Prints list of Pokedex, and if response is one of the options in Pokedex, Pokedex entry is printed out and fight resumes
            if Read in Pokedex:
                print "\n"+Pokedex[Read]
                time.sleep(4)
                fight()
            else:
                print "\nThat's not a Pokemon that I have seen before..."           #Error handling
                time.sleep(1)
                fight()
        elif Item=="R":                     #Exit back to fight
            fight()
        else:
            print "\nThat's not an item"           #Error handling
            time.sleep(1)
            fight()
    elif response=="3":
        print "\nThere is no running from a trainer battle!"          #No real use in battles           
        time.sleep(1)
        fight()
    elif response=="R":             #Exit back to fight
        fight()
    else:
        print "\nThat's not an available option"           #Error handling
        time.sleep(1)
        fight()

                                        #OPTIONS WITHIN ROOMS

def room_options():
    global room
    global option
    global Doorknob
    global Hammer
    global Pokeball
    global adv
    global painting
    if room == 1:                       #Checks which room the player is in and then begins the dialouge
        print "What would you like to do now?\n"
        print "\n1. explore room \n2. go back to the door \n3. Inspect the couch \n4. walk up to the man \n5. open Pokedex\n"
        print "\nType the number associated with the option"
        user_input = raw_input("\n")
        if user_input == "1":                   #Checks which choice the user decided to use and the continues story in the chosen path
            print "\n*You start making your way around the room, making sure to keep one hand on the wall at all times*\nWhen all of a sudden you brush over a button and the lights turn on"
            time.sleep(5)
            print "*At this, the man in the center falls to the ground and shreaks.*"
            time.sleep(3)
            print "*You run to the center to make sure he's okay*\n*When you reach him he starts laughing...*"
            time.sleep(4)
            print "*He stands up and takes a pokeball out of his pocket*"
            time.sleep(3.5)
            print "oh no..."
            Doorknob="False"
            Hammer="False"
            time.sleep(2)
            pre_second_fight()
        elif user_input == "2":
            print "\n*You try to open the door but as you try the door knob falls off*"
            time.sleep(4)
            Doorknob= "True"
            Hammer="False"
            print "Doorknob added to Bag!"
            time.sleep(3)
            print "*You scream for someone to help, but all you hear is your own voice echo softly* \nThis place must be made to trap someone inside..."
            time.sleep(6)
            print "*You all of a sudden hear a stur of noise behind you* \n*You look and you see that the man who had been sitting is now standing, staring at you*"
            time.sleep(6)
            print "*You can't make out his face but you can see a pokeball on his hands*"
            time.sleep(4)
            print "oh no..."
            time.sleep(2)
            pre_second_fight()
        elif user_input == "3":
            print "\n*You walk up to the couch...* \nIts old and dusty... but it looks comfortable."
            time.sleep(4)  
            print "*You sit down...* \nHmmm... this is kinda nice... i could just... fall... asleep... here"
            time.sleep(6)
            print "*YAAAWWWWNNNN*"
            time.sleep(3)
            print "*When you lay your head back, but you hit something hard...* \n *When you look, you see you hit your head on a hammer.*"
            time.sleep(5)
            Hammer = "True"
            Doorknob="False"
            print "Hammer has been added to your bag"
            time.sleep(3)
            print "*The shady character in the corner approaches you from the shadows with an angry look in his eye*"
            time.sleep(4)
            print "*You cant make out his face but you can see a pokeball on his hands*"
            time.sleep(3)
            print "oh no..."
            time.sleep(3)
            pre_second_fight()
        elif user_input == "4":
            print "\n*You walk up to the man* \num... hello?"
            time.sleep(4)
            print "*He doesnt respond* \nummmmm, hel..."
            time.sleep(3)
            print "*All of a sudden he stands up at an insane speed and pulls a pokeball out of his pocket*"
            time.sleep(4)
            print "*You stumble back and almost catch yourself but hit the ground hard* \nWhen you look up you see he's staring you down, obviously waiting for you to make the first move.*"
            time.sleep(7)
            Hammer = "False"
            Doorknob="False"
            pre_second_fight()
        elif user_input == "5":
            print "\nPrint the name of the Pokemon that you would like to read about\n"
            for item in Pokedex:
                print item
            Read=raw_input("\n").title()
            if Read in Pokedex:
                print "\n"+Pokedex[Read]
                time.sleep(4)
                room_options()
            else:
                print "\nThat's not a Pokemon that I have seen before..."               #Error handling
                time.sleep(1)
                room_options()
        else:
            print "Hmmmm?\n\n"              #Error handling
            room_options()
    elif room == "Hallway":              #Checks which room the player is in and then begins the dialouge
        print "What you like to do now?\n\n"
        print "1. Go inspect painting \n2. Go to the door at the end of the hallway \n3. Try the door behind you\n4. Pokedex"
        user_input = raw_input("\n")
        if user_input == "1":
            if painting == 0:
                print "\nYou walk up to the painting, inspecting the melting figure"
                time.sleep(3.5)
                print "Its reminiscent of something from your nightmares"
                time.sleep(4)
                print "Then all of a sudden you get an idea..."
                time.sleep(3)
                print "You grab a alight off the wall and realize its a burning torch."
                time.sleep(4)
                print "You hold the torch up to the painting and after a second the image begins to shift."
                time.sleep(4)
                print "The figure in the image eventually melts away and then you hear a click..."
                time.sleep(4)
                print "The painting swings open and you see a storage space behind it"
                time.sleep(4)
                print "You look in the area and notice that there is a pokeball inside there"
                time.sleep(3.5)
                print "A Pokeball has been added to your bag"
                Pokeball = Pokeball+1
                painting = 1
                time.sleep(3)
                room_options()
            elif painting == 1:
                print "\nYou've already been here, theres nothing new from what was there before."
                time.sleep(2)
                room_options()
        elif user_input == "2":
            print "\nYou walk to the door and the end of the hallway"
            time.sleep(3)
            print "You open the door and move on into the next rooom"
            time.sleep(3)
            text3NextRoom()
        elif user_input == "3":
            print "\nthe lock made you feel unreasonably trapped..."
            time.sleep(3)
            print "you turn around try turning the door handle"
            time.sleep(3)
            print "yep, you were right, locked from the other side, no way back now..."
            time.sleep(4)
            room_options()
        elif user_input == "4":
            print "\nPrint the name of the Pokemon that you would like to read about\n"
            for item in Pokedex:
                print item
            Read=raw_input("\n").title()
            if Read in Pokedex:
                print "\n"+Pokedex[Read]
                time.sleep(4)
                room_options()
            else:
                print "\nThat's not a Pokemon that I have seen before..."               #Error handling
                time.sleep(1)
                room_options()
        else:
            print "Hmmmm?\n\n"              #Error handling
            room_options()
    elif room == 2:                       #Checks which room the player is in and then begins the dialouge
        print "What would you like to do now?\n\n"
        print "1. Go look at the pack of UNICORNS \n2. Look around the room \n3. Go talk to the woman \n4. Pokedex"
        user_input = raw_input("\n")
        if user_input == "1":                   #Checks which choice the user decided to use and the continues story in the chosen path
            print "\nYou carefully approach the blessing of unicorns, slowly pulling a Pokeball out from your bag"
            time.sleep(4)
            print "When you get within catching distance, you wind up a throw and CHUCK the Pokeball at the nearest unicorn."
            time.sleep(4)
            print "The Pokeball harmlessly bounces off of the unicorn and rolls on the ground."
            Pokeball=4
            time.sleep(3)
            print "???: Aren't they beautiful? Unicorn's aren't Pokemon, so that won't work here. This place is my home..."
            time.sleep(5)
            print "*You turn, startled, and see the lady once in the middle of the room now behind you"
            time.sleep(4)
            print "Rainbow Lady: this place is just sooooo lovely. Wouldn't you agree?"
            time.sleep(4)
            print "I don't know... I just need to find my way out of here, so I'm going to have to leav-"
            time.sleep(4)
            print "Rainbow Lady: NO!"
            time.sleep(3)
            print "*Suddenly, her eyes turn red you see the unicorns in the background all turn towards you as well, all eyes blood red and fixated on you...*"
            time.sleep(5)
            print "WOOAH! I need to get out. Now. Bye!"
            time.sleep(3)
            print "*You turn to run, but the room switches instantly to dark* \n*You look up and you see that the once clear sky is now brewing up a storm*"
            time.sleep(6)
            print "oh no"
            time.sleep(2)
            print "Nightmare Lady: Wait, trying to leave so soon?... the party has just begun... "
            time.sleep(5)
            pre_third_fight()
        if user_input == "2":
            print "\n*You starting looking around, walking lazily through the grass... this room is oddly relax1ing now that you think about it*"
            time.sleep(5)
            print "*As you spin in a circle taking in the view, you spot something out of the corner of your eye*"
            time.sleep(4.5)
            print "Over on the other side of the room in a pannel of wires... on what appears to be nothing... \n*You approach the wires*"
            time.sleep(5)
            if Hammer == "True":
                print "\n*You go up and inspect the wires... you can hear the hum of electricity...* \nWhat is this place"
                time.sleep(5)
                print "Wait... you get an idea all of a sudden."
                time.sleep(3)
                print "You pull the hammer out of your bag and, because it seems like the most logical course of action, hit the pannel with the hammer!"
                time.sleep(5)
                print "At this the room changes completely... \nWhat was previously bright and peaceful has turned into a dark concrete room with no windows and only a single light hanging from the center."
                time.sleep(5)
                print "Rainbow Lady: WHAT DID YOU DO!!! MY OASIS!!!!"
                time.sleep(3.5)
                print "*At this her eyes turn red you see the unicorns in the background all turn towards you as well, all eyes blood red and fixated on you...*"
                time.sleep(5)
                print "...oh come on"
                time.sleep(2)
                print "*She seems very uncomfortable with the new envoirnment"
                adv="True"
                time.sleep(3)
                pre_third_fight()
            else:
                print "\nWhat is this..."
                time.sleep(3.5)
                print "*You walk up to the pannel, trying to make sense of the array of wires*"
                time.sleep(4.5)
                print "???: Isn't it beautiful? This place is my home..."
                time.sleep(3)
                print "*You turn, startled, and see the lady once in the middle of the room now behind you"
                time.sleep(4)
                print "Rainbow Lady: Its just sooooo lovely. Wouldn't you agree?"
                time.sleep(4)
                print "I don't know... I just need to find my way out of here, so I'm going to have to leav-"
                time.sleep(4)
                print "Rainbow Lady: NO!"
                time.sleep(3)
                print "*Suddenly, her eyes turn red you see the unicorns in the background all turn towards you as well, all eyes blood red and fixated on you...*"
                time.sleep(5)
                print "WOOAH! I need to get out. Now. Bye!"
                time.sleep(3)
                print "*You turn to run, but the room switches instantly to dark* \n*You look up and you see that the once clear sky is now brewing up a storm*"
                time.sleep(6)
                print "oh no"
                time.sleep(2)
                print "Nightmare Lady: Wait, trying to leave so soon?... the party has just begun... "
                time.sleep(5)
                pre_third_fight()
        if user_input == "3":
            print "You approach the lady standing peacefully at the center, and she seems to notice you"
            time.sleep(5)
            print "Rainbow Lady: Isn't it beautiful? This place is my home..."
            time.sleep(3)
            print "Uhhh... Yeah. Where is 'this' exactly?"
            time.sleep(4)
            print "Rainbow Lady: Does it matter? Come on, enjoy yourself"
            time.sleep(4)
            print "I don't know... I just need to find my way out of here, so I'm going to have to leav-"
            time.sleep(4)
            print "Rainbow Lady: NO!"
            time.sleep(3)
            print "*Suddenly, her eyes turn red you see the unicorns in the background all turn towards you as well, all eyes blood red and fixated on you...*"
            time.sleep(5)
            print "WOOAH! I need to get out. Now. Bye!"
            time.sleep(3)
            print "*You turn to run, but the room switches instantly to dark* \n*You look up and you see that the once clear sky is now brewing up a storm*"
            time.sleep(6)
            print "oh no"
            time.sleep(2)
            print "Nightmare Lady: Wait, trying to leave so soon?... the party has just begun... "
            time.sleep(5)
            pre_third_fight()
        if user_input == "4":
            print "\nPrint the name of the Pokemon that you would like to read about\n"
            for item in Pokedex:
                print item
            Read=raw_input("\n").title()
            if Read in Pokedex:
                print "\n"+Pokedex[Read]
                time.sleep(4)
                room_options()
            else:
                print "\nThat's not a Pokemon that I have seen before..."           #Error handling
                time.sleep(1)
                room_options()
        else:
            print "Hmmmm?\n\n"          #Error handling
            room_options()
    elif room == 3:
        print "What would you like to do now?\n\n"
        print "1. Approach the Skeletons \n2. Inspect the markings on the walls \n3. Enter through the door \n4. Pokedex"
        user_input = raw_input("\n")
        if user_input == "1":                   #Checks which choice the user decided to use and the continues story in the chosen path
            print "\nAs you get closer to the skeletons, the you recognize the shape and size of the skeletons to be a human laying over their Pokemon"
            time.sleep(5)
            print "No shred of evidence is left of their previous lives except for a tattered red and white hat on the ground beside them and a smashed up Pokedex"
            time.sleep(6)
            print "You feel like you probably shouldn't disturb them..."
            time.sleep(2)
            room_options()
        if user_input == "2":
            print "\nYou walk over to the walls, and see huge scratch marks covering fifteen feet across, torn deep into the cement"
            time.sleep(4)
            print "It looks as if a tornado came through the room and threw everything around into chaos"
            time.sleep(4)
            print "Whatever caused..."
            time.sleep(2)
            print "this..."
            time.sleep(2)
            print "must be very powerful"
            time.sleep(2)
            room_options()
        if user_input == "3":
            print "\nYou muster up the courage and approach the door"
            time.sleep(2.5)
            print "The winds pick up drastically once you step out, and you see yourself now on the rooftop of the tower facing a raging storm"
            time.sleep(5)
            print "You look around, but the winds become so strong that you are forced to your hands and knees."
            time.sleep(4)
            print "When you and try to regain your footing, the floor beneath you begins to shake as a massive figure rises, coiling around the tower"
            time.sleep(5)
            print "As lighning cracks, you catch a glimpse of the beast, with its wicked sharp smile and peircing yellow eyes"
            time.sleep(4)
            print "You look back, but there is no way you can get back to the door before the monster could reach you"
            time.sleep(3)
            print "Finally, you stand up before the mighty beast and challenge its power"
            time.sleep(3)
            pre_last_fight()
        if user_input == "4":
            print "\nPrint the name of the Pokemon that you would like to read about\n"
            for item in Pokedex:
                print item
            Read=raw_input("\n").title()
            if Read in Pokedex:
                print "\n"+Pokedex[Read]
                time.sleep(4)
                room_options()
            else:
                print "\nThat's not a Pokemon that I have seen before..."           #Error handling
                time.sleep(1)
                room_options()
        else:
            print "Hmmmm?\n\n"          #Error handling
            room_options()
        
                                                    #good ending

def pre_good_ending():
    global name
    global Pokemon_out                  #Plays text and brings player to final decision
    print "I DID IT!"
    time.sleep(2.5)
    print "Immediately after Rayquaza is captured, the storm dies down and the sun shines through the clouds "
    time.sleep(4)
    print "You pick up the Pokeball off of the ground and walk back over to the door"
    time.sleep(3)
    print "When you walk out to the other side, you recognize the area as back outside of the tower where you began"
    time.sleep(4)
    print "At this point, you don't even question it and just walk out into the town square where you see people slowly getting out of their houses and looking around at the wreckage"
    time.sleep(6)
    print "Professor Oak is the first to see you out in the open, and rushes over to you"
    time.sleep(3)
    print "Prof Oak: You did it! I honestly wasn't expecting much, with my last test dying on me, but you came back!"
    time.sleep(5)
    print "Prof Oak: Now, "+name+", Where is the Pokeball? Give him to me.\n"
    time.sleep(4)
    good_ending()
    
def good_ending():
    global name
    global Pokemon_out
    global Hammer
    if Hammer=="True":              #Final decision determines outcome of game. If player picked up hammer, extra options
        ans=raw_input("1. Give Professor Oak the the real Rayquaza\n2. Give Prof Oak an empty fake\n3. Use the Hammer...\n")
    else:
        ans=raw_input("1. Give Professor Oak the the real Rayquaza\n2. Give Prof Oak an empty fake\n")
    if ans=="1":
        print "\nYou reluctantly hold out the Pokeball in your hands, and Professor Oak snatches it away"
        time.sleep(3)
        print "Prof Oak: IDIOT! I CAN'T BELIEVE YOU ACTUALLY GAVE ME HIM!\nNOW I CAN TAKE OVER THIS STUPID REGION AND THEN THE REST OF THE WORLD!!!"
        time.sleep(5)
        print "Professor Oak relases Rayquaza, and with him the storm picks back up"
        time.sleep(2)
        print "Prof Oak: HEAR ME, FOR I AM YOUR MASTER! YOU WILL DO AS I SAY AND WE WILL CONQUER THIS LAND!"
        time.sleep(3)
        print "Prof Oak: COME, WE HAVE MUCH TO D-"
        time.sleep(1.5)
        print "Rayquaza smacks Professor Oak, sending him flying acroos the square, and Rayquaza and ascends up into the clouds"
        time.sleep(3)
        print "You run inside the lab with "+Pokemon_out+" to escape the storm, but you fear for the worst"
        time.sleep(3)
        bad_ending()
    elif ans=="2":
        print "\nYou shuffle through your bag and present Professor Oak with an empty Pokeball"
        time.sleep(3)
        print "Prof Oak: IDIOT! I CAN'T BELIEVE YOU ACTUALLY GAVE ME HIM!\nNOW I CAN TAKE OVER THIS STUPID REGION AND THEN THE REST OF THE WORLD!!!"
        time.sleep(5)
        print "Professor Oak relases the Pokeball, and nothing happens"
        time.sleep(3)
        print "Prof Oak: HEAR ME, FOR I AM YOUR MASTER... "
        time.sleep(4)
        print "Prof Oak: and... "
        time.sleep(3)
        print "Prof Oak: WHAT!"
        time.sleep(3)
        print "He stares at you intensely, but before he can get to you, a crowd, now formed around you and this raving professor, starts yelling accusations at the Professor"
        time.sleep(5)
        print "Prof Oak: Get away! All of you! You would never understand!"
        time.sleep(4)
        print "Police emerge from the crowd and handcuff the Professor, dispersing the crowd and leaving you alone in the town square"
        time.sleep(6)
        print "I think its time to go home, "+Pokemon_out+"."
        time.sleep(3)
        print "You walk back home and get a snack out to the kitchen"
        time.sleep(4)
        print "You have won!\n\n    GOOD ENDING"
        quit()          #Ends code
    elif ans=="3" and Hammer=="True":
        print "\nYou take off your bag and set it on the ground..."
        time.sleep(4)
        print "Okay yeah, its right here, come over so you can take it"
        time.sleep(3.5)
        print "Prof Oak: Yes, alright."
        time.sleep(3.5)
        print "As he walks over you pull out your hammer and CRACK HIM IN THE KNEECAPPS!"
        time.sleep(4)
        print "Prof Oak: AHHHHHHHHHHHHH! MY KNEEEEEES! WHYYYYYYYYY!"
        time.sleep(4)
        print "As he falls you make a run for Route 1, not daring to look back..."
        time.sleep(5)
        print "You have won!\n\n    FUGITIVE ENDING"
        quit()
    else:
        print "\nHmmm?"
        good_ending()
    
                                                    #bad ending
    
def bad_ending():
    print "\nAs Rayquaza rises up, the storm back picks up, even harder than before"
    time.sleep(5)
    print "The town erupts into chaos as cars and debris ar tossed like toys by the winds and rain hurtles from the sky"
    time.sleep(6)
    print "When you look up, you see Rayquaza fly out through a thick blanket of clouds and dissapear..."
    time.sleep(5)
    print "You look back to your Pokemon, and then run to them as the walls tear from the foundation"
    time.sleep(6)
    print "The end of the world has begun. Rayquaza has escaped from the tower imprisioning his power and has reclaimed the sky"
    time.sleep(6)
    print "Hurricanes and tropical stroms erupt all over the world and people are stuck frightened in their homes"
    time.sleep(6)
    print "You have lost\n\n    BAD ENDING"
    quit()          #Ends code
    
    

                                                    #Fourth set of text

def text4():
    global room
    global option
    print "Nightmare Lady: WHAT HAVE YOU DONE, YOU STUPID STUPID CHILD"
    time.sleep(3)
    print "*As she speaks she starts slowly turning into dust, blowing away in the wind*"
    time.sleep(4)
    print "oh..."
    time.sleep(1.5)
    print "*As the final parts of her deteriorate, the wall behind her opens reveling another door... (im starting to see a trend here)*"
    time.sleep(4)
    print "*thankfully, this one has a doorknob and you walk through...*"
    time.sleep(3)                               # claw marks, destroyed, leads to final boss, ash/pikatchu skeleton
    print "*You've seen a lot of weird things today but nothing can prepare you for this...*"
    time.sleep(3)
    print "*When you open the door to the door, youre hit in the face by a smell you can only describe as rotting flesh..."
    time.sleep(3)
    print "*The room is torn up, with claw marks littered across cracked walls. \nAcross the room you see a skeleton in the corner, infested with flies"
    time.sleep(3.5)
    print "There is a door on the other end of the room hanging open, allowing a cool breeze to blow through the room."
    room = 3
    room_options()

def text3NextRoom():
    global room
    global Doorknob
    print "\nYou move on to the next room"
    time.sleep(2)
    print "The next room is nothing like the last..."
    time.sleep(2)
    print "As you open the door you are blinded by a bright light"
    time.sleep(2.5)
    print "You give yourself a second to adjust and when you do you are faced by a room (if you can call it that) of beautiful flowers \n You look over and you see a heard of unicorns prancng off into the distance..."
    time.sleep(5)
    print "...wait, how are they going into the distance... and how is the sun out...?? Isnt this a building???"
    time.sleep(3)
    print "As your eyes finish adjusting, you make out a woman, dressed in mostly tie dye, sitting on a picnic blanket in the middle of the... 'room'?"
    time.sleep(4)
    room = 2
    room_options()                        #Sets up the code for the next room
    
                                                    #Third set of Text

def text3Hallway():
    global room
    global option
    global Doorknob
    global Pokemon_out
    global Pokemon_health
    global painting
    print "\nShady Homeless Dude: Since you defeated me, you have now gained access to the next room. "        #use doorknob to open door/take damage
    time.sleep(5)
    print "*Though this is the first time you heard his voice, it doesnt suprise you. The raspy tone reminds you of someone... you just dont know who*"
    time.sleep(6)
    print "*The wall behind the mysterious man opens, revealing a door*"
    time.sleep(3.5)
    print "Thank you strange shadow man?"
    time.sleep(3)
    print "*You walk up to the door and push...*"
    time.sleep(3.5)
    print "*It doesn't budge*"
    time.sleep(3)
    print "*You look down thinking maybe you have to turn the handle, only to see there an empty hole..."
    time.sleep(4)
    if Doorknob == "True":      #Checks to see if the user picked up the doorknob in the previous room
        print "*Wait... all of a sudden you get an idea*"
        time.sleep(3)
        print "*You dig into your bad and pull out the doorknob from the front door*"
        time.sleep(3)
        print "HA HA HA, get rekt shady dude, in your face! \n"
        time.sleep(3)
        print "You insert the doorknob and move on..."
        time.sleep(3)
    elif Doorknob == "False":
        print "Ummm... okay, lets try this."
        time.sleep(3)
        print "You send out "+ Pokemon_out
        time.sleep(3)
        print "Okay "+ Pokemon_out + " ...um, like, break down the door... or something"
        time.sleep(4)
        print "*" +Pokemon_out + " looks at you with a look of complete confusion, and then... reluctantly... breaks down the door.*"
        time.sleep(6)
        print "*This worked!... Kinda...*\nDoor debris hurts "+Pokemon_out+ " a little bit and takes 2 damage."
        time.sleep(6)
        Pokemon_health = Pokemon_health-2
    print "The next area is a long hallway, with a series of lights spaced along it to make it look dark but still bright enough to see clearly... which makes no sense."
    time.sleep(4)
    print "As you walk forward the door behind you closes loudly and you hear the click of it locking"
    time.sleep(3.5)
    print "You look and you see a paining on the wall resembling what looks like a model of a person melting sourounded by darkness..."
    time.sleep(4)
    room = "Hallway"
    painting = 0
    room_options()


                                        #SECOND TEXT SET

def text2():
    global room
    print "Congrats, since you now know how to fight, it is time to enter the world of Pokemon! \nYour first stop will be rou..."
    time.sleep(6)
    print "Random Person in the street: WOAH, LOOK AT THAT SCARY BUILDING!"
    time.sleep(3)
    print "*You look and there is, in fact, a scary looking building that youve never seen before*"
    time.sleep(4)
    print "Prof Oak: Woah... thats pretty scary, you go check it out."
    time.sleep(3)
    print "*Prof Oak picks you up and throws you through the front door and closes it behind you*"
    time.sleep(3.5)
    print "CRASH BOOM KER-PLUNK"
    time.sleep(2.5)
    print "..."
    time.sleep(3.5)
    print "*it is completely dark, and you see a man sitting in the middle of the room, though you can not make out his face...*\n*There is nothing else in the room besides a couch sitting in the darkness.*"
    time.sleep(5)
    room = 1
    room_options()
    


                                        #First Set of Text for Start of Game-Tutorial Battle

def text1():
    global name
    global Bag
    global room
    print "When answering a question, type out 'yes' or 'no' unless prompted otherwise."
    time.sleep(3)
    print "\nWhy Hello! Welcome to the world of Pokemon! My name is Professor Oak, but people call me the Pokemon Professor. \nThis world is inhabited by creatures called Pokemon."
    time.sleep(6)
    print "For some people, Pokemon are pets. Others use them for fights. \nMyself... I study Pokemon as a profession\n"
    time.sleep(4)
    name = str(raw_input("What is your name? "))
    print "Well "+name+", it is wonderful to meet you. "
    time.sleep(3)
    print "Anyway, you better get going, there's a whole world waiting for you out there! \n"
    time.sleep(5)
    print "Mom: "+name+"! Wake up! Today's the big day! Professor Oak expects that you will be there to get your first Pokemon soon! "
    time.sleep(5)
    print "*You get out of bed... reluctantly, and get dressed.*"
    time.sleep(3)
    print "Mom: "+name.upper()+"!!!"
    time.sleep(2.5)
    print "IM COMING! JEEEEEEEEZ!"
    time.sleep(2.5)
    print "*You walk down the stairs*"
    time.sleep(2)
    print "Mom: Before you go, take this!" 
    time.sleep(2)
    print "*Your mom hands you a 'Pokedex'"
    time.sleep(2)
    print "Pokedex added to Bag!"
    Bag["Pokedex"]=0
    time.sleep(3)
    print "Mom: Okay, go ahead now, Professor Oak will be waiting."
    time.sleep(2)
    print "*You walk outside and see clouds in the sky*"
    time.sleep(2)
    choice = raw_input("Would you like to go straight to the Professor's? ").title()
    while choice !="Yes":                   #If you chooses to not go to the professor's, you will be stuck in an endless loop until you say yes
        if choice=="No":
            print "*You stand in front of the door... waiting*"
            time.sleep(3)
            choice = raw_input("Would you like to go straight to the Professor's? ").title()
        else:
            print "Excuse Me?"
            time.sleep(1)
            choice = raw_input("Would you like to go straight to the Professor's? ").title()
    time.sleep(1)
    print "You make your way over to the Professor's"
    time.sleep(3)
    print "\nWhen you arrive, you are brought to the back and presented with three Pokeballs strewn across a table"
    time.sleep(5)
    print "Prof Oak: Hello, it's wonderful to meet you, "+name+".\nIn each of these Pokeballs is a unique Pokemon that you may take on your journey."
    time.sleep(5)
    print "I know you've been waiting for this day for a long time, so I wont keep you waiting..."
    time.sleep(4.5)
    starter_choice()

text1()