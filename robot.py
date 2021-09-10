from weapon import Weapon

class Robot:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.weapon = Weapon("Super Sucker", 15)

    def robot_attack(self, dinosaur):
        dinosaur.hp -= self.weapon.attack
