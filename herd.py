from dino import Dino

class Herd:
    def __init__ (self, list):
        self.list = list


squish_dino_one = Dino("Ceolophysis","Squish",80,0,10 )
squish_dino_two = Dino("Ceolophysis","Squeeze",80,0,10 )
basic_dino = Dino("Dilophosaurus", "Spite", 100, 5, 0)
tank_dino_one = Dino("Allosaurus", "Frankie", 120, 10, 5)
tank_dino_two = Dino("Allosaurus", "Freaky", 120, 10, 5)

balanced_list = [squish_dino_one, basic_dino, tank_dino_one]
glass_cannon_list = [squish_dino_one, squish_dino_two, basic_dino]
tank_list = [tank_dino_one, tank_dino_two, basic_dino]

#create herd - pick from balanced, glass cannon, or tanky build