from attacks import Attack


class Dino:
    def __init__(self,type, breed, name, health, scales, attack):
        self.type = type
        self.breed = breed
        self.name = name
        self.health = health
        self.scales = scales
        self.attack_power = attack
        self.stamina = 100
        

    attack_claws = Attack("Claws", 10)
    attack_bite = Attack("Bite", 15)
    attack_spit = Attack("Spit", 5)

    def define_dino_attacks(self, attack_claws, attack_bite, attack_spit):
        if self.type =="squish":
            self.attacks = (attack_claws, attack_bite)
        if self.type == "basic":
            self.attacks = (attack_claws, attack_spit)
        if self.type == "tank":   
            self.attacks = (attack_claws, attack_bite)

    def dino_attack(self, robot):
        attack_choice = input("Please choose which attack you would like your dino to do: " + self.attacks + "Please enter 1 or 2 for your weapon choice.")
        if attack_choice == 1:
            attack = self.attacks(0)
        if attack_choice == 2:
            attack = self.attacks(1)
        damage = attack.attack_power - robot.armor
        robot.health -= damage
        self.stamina -= 10

    def dino_defense(self):
        self.stamina += 20
        defense = self.scales +10
        return defense
