from fleet import Fleet

from herd import Herd


#__init__

def welcome():
    print("Welcome to our feature battle of Dinosaurs vs Robots!  We have beings from across the galaxy that have prepared teams for you to battle with!  Today, we have the Roombers supplying fleets of modified (and enlarged!) Roombas!  From the planet Jurrrrasic, we have herds of dinosaurs for you to choose from!")
    player_name = input("Tell us, master commander, what would you like to be referred to as today?  You don't have to use a name.  You could be whoever or whatever you wish today!")
    print("Your name is " + player_name+".  Huh.  Interesting...")
    return player_name

#select robots or dinos
def choose_your_side():
    choose_creatures = input("Okay, " + player_name + ".  Would you like to play as the dinosaurs or robots today?")
    if choose_creatures.lower() == "robots" or choose_creatures.lower() == "bots" or choose_creatures.lower() == "robos":
        player = Fleet
        player.choose_fleet_type(player)
        print(player.list)
        computer = Herd
        computer.list = balanced_list
    if choose_creatures.lower()== "dinos" or choose_creatures.lower()== "dinosaurs" or choose_creatures.lower()== "dino":
        player = Herd
        player.choose_herd_type(player)
        print(player.list)
        computer = Fleet
        computer.list = balanced_robots

        
        
        

#player goes first (we're nice around here)
#player turn, select attack(choose for dinos) or defend
#computer turn alternate between attacking and defending
#if creature is out of energy, have to swap creatures
#if creature out of HP, creature is removed from the list


#show dino opponent options

# show robo opponent options

#display winners

#run game
player_name = welcome()
choose_your_side()