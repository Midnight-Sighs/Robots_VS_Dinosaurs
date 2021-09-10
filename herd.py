from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dino_list = []

    def create_dinos(self):
        dino1 = Dinosaur("Frankie the Allo", 120, 20)
        dino2 = Dinosaur("Daisy the Dilo", 70, 10)
        dino3 = Dinosaur("Ralph the Raptor", 100, 15)

        self.dino_list.append(dino1)
        self.dino_list.append(dino2)
        self.dino_list.append(dino3)

    def display_herd(self):
        print(self.dino_list)