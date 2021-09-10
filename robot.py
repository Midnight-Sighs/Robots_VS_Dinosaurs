from weapon import Weapon

class Robot:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.weapon = Weapon("Super Sucker", 15)
        self.armor = 5
        self.battery_charge = 100

    def robot_attack(self, dinosaur):
        dinosaur.hp -= (self.weapon.attack - dinosaur.scales)
        self.battery_charge -= 10