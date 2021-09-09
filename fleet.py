from robot import Robo


robo_squish_one = Robo("squish","Mega Roomba ++", "Art", 80, 0, 5)
robo_squish_two = Robo("squish","Mega Roomba ++", "Mary", 80, 0, 5)
robo_basic = Robo("basic", "Roomba", "Bob", 100, 5, 0)
robo_tank_one = Robo("tank", "Armored Roomba +", "Patrick", 120, 10, 0)
robo_tank_two = Robo("tank","Armored Roomba +", "Anne", 120, 10, 0)
balanced_robots = [robo_squish_one, robo_basic, robo_tank_one]
squish_robots = [robo_squish_one, robo_squish_two, robo_basic]
tank_robots = [robo_tank_one, robo_tank_two]

class Fleet:
    def __init__(self):
        self.list = [ ]

    def choose_fleet_type(self):
        print("What type of fleet would you like to use today?  We have a balanced fleet ready, that has a sampling of each of our models.  We have a squish fleet that may not be able to take as much damage but can certainly deal it, and we have a tank fleet, that can withstand some damage but is slow and steady!")
        fleet_choice = input("type a 1 for a balanced fleet, 2 for tanky, and 3 for squishy.")
        if fleet_choice == "1":
            self.list =balanced_robots
            print("You have selected a balanced list of robots!")
        if fleet_choice == "2":
            self.list = tank_robots
            print("You have selected our fleet of tanky bots!")
        if fleet_choice == "3":
            self.list = squish_robots
            print("You have selected our squishy robots!")
            print(self.list)

    def assign_computer_to_fleet(self):
        self.list = balanced_robots
        
        print("Your opponent has chosen their list.")