from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.player_name = self.display_welcome()
        self.fleet = Fleet
        self.herd = Herd

    def run_game(self):
        pass

    def display_welcome(self):
        print("Welcome to our feature battle of Dinosaurs vs Robots!  We have beings from across the galaxy that have prepared teams for you to battle with!  Today, we have the Roombers supplying fleets of modified (and enlarged!) Roombas!  From the planet Jurrrrasic, we have herds of dinosaurs for you to choose from!")
        self.player_name = input("Tell us, master commander, what would you like to be referred to as today?  You don't have to use a name.  You could be whoever or whatever you wish today!  ")
        print("Your name is " + self.player_name+".  Huh.  Interesting...")
        Battlefield.choose_your_side(self)

    def choose_your_side(self):
        choose_creatures = input("Okay, " + self.player_name + ".  Would you like to play as the dinosaurs or robots today?")
        if choose_creatures.lower() == "robots" or choose_creatures.lower() == "bots" or choose_creatures.lower() == "robos":
            player = Fleet()
            print("You have the following list: " + Fleet.display_fleet(player))
            computer = Herd
        if choose_creatures.lower()== "dinos" or choose_creatures.lower()== "dinosaurs" or choose_creatures.lower()== "dino":
            player = Herd
            computer = Fleet
        print("Now that you've chosen, your battle may commence!")

    def battle(self):
        pass
