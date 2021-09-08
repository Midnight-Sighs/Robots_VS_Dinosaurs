from dino import Dino


class Herd:
    squish_dino_one = Dino("Ceolophysis","Squish",80,0,10 )
    squish_dino_two = Dino("Ceolophysis","Squeeze",80,0,10 )
    basic_dino = Dino("Dilophosaurus", "Spite", 100, 5, 0)
    tank_dino_one = Dino("Allosaurus", "Frankie", 120, 10, 5)
    tank_dino_two = Dino("Allosaurus", "Freaky", 120, 10, 5)
    balanced_list = [squish_dino_one, basic_dino, tank_dino_one]
    glass_cannon_list = [squish_dino_one, squish_dino_two, basic_dino]
    tank_list = [tank_dino_one, tank_dino_two, basic_dino]

    
    def __init__ (self):
        self.list = []

    def choose_herd_type(self):
        print("What type of herd would you like to use today?  We have a balanced herd ready to battle, showing you one of each of our favorite dinosaurs! Rawr!  We also have a tanky herd, *rawr* that *rawr*...excuse me.  We have a tanky herd that will certainly stand up to the best of foes!  We also have a squishy herd that may not be able to take a hit well, but can dish it out! RAAAWR!")
        fleet_choice = input("Type a 1 for a balanced her, 2 for tanky, and 3 for squishy.")
        if fleet_choice == "1":
            self.list =balanced_list
            print("You have selected a balanced list of dinosaurss!")
        if fleet_choice == "2":
            self.list = tank_list
            print("You have selected our fleet of tanky dinosaurs!")
        if fleet_choice == "3":
            self.list = glass_cannon_list
            print("You have selected our squishy dinosaurs!")