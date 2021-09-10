from robot import random_int
from attack import Attack
import random

class Dinosaur:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = 100
        self.scales = 5
    
    possible_attacks = [Attack("Claws", 10),
                    Attack("Bite", 15),
                    Attack("Spit", 5)]

    def dinosaur_attack(self, robot):
        i = random_int(0, 2)
        robot.hp -= (self.attack + self.possible_attacks[i].attack) - (robot.armor + robot.flux_shield())
        self.stamina -= 10