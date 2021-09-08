from attacks import Attack


class Dino:
    def __init__(self, breed, name, health, scales, attack):
        self.breed = breed
        self.name = name
        self.health = health
        self.scales = scales
        self.attack_power = attack
        self.stamina = 100

    attack_claws = Attack("Claws", 10)
    attack_bite = Attack("Bite", 15)
    attack_spit = Attack("Spit", 5)

    squish_attacks = (attack_claws, attack_bite)
    basic_attacks = (attack_claws, attack_bite)
    tank_attacks = (attack_claws, attack_bite)

#What can the dino do?
#attack
#choose attack each turn
#def choose_attack(self):


#defend - double scales, no attack