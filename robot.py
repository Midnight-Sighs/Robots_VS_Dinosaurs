from weapon import Weapon

super_sucker = Weapon("Super Sucker", 20)
debris_cannon = Weapon("Debris Cannon", 15)
debris_blaster = Weapon("Debris Blaster", 5)
debris_sucker = Weapon("Debris Sucker", 10)

class Robo:
    def __init__(self, type, model, name, health, armor, attack):
        self.type = type
        self.model = model
        self.name = name
        self.health = health
        self.armor = armor
        self.attack_power = attack
        self.battery_charge = 100
        self.weapon = Weapon
        self.damage = 0

    def equip_weapon(self):
        if self.type == "tank":
            print("You have the options of equipping a Debris Cannon or a Super Sucker.  For a Roomba, there're both pretty impressive.")
            choice = input("Type a 1 if you want the Debris Cannon and type a 2 if you want a Super Sucker.")
            if choice == 1:
                self.weapon = debris_cannon
                self.damage = self.weapon.attack_power + self.attack_power
            if choice == 2:
                self.weapon = super_sucker
                self.damage = self.weapon.attack_power + self.attack_power
        if self.type == "squish":
            print("You have the weapon choices between a Debris Cannon and a Super Sucker.  Who said Roombas weren't cool?")
            choice = input("Type a 1 if you want the Debris Cannon and type a 2 if you want a Super Sucker.")
            if choice == 1:
                self.weapon = debris_cannon
                self.damage = self.weapon.attack_power + self.attack_power
            if choice == 2:
                self.weapon = super_sucker
                self.damage = self.weapon.attack_power + self.attack_power
        if self.type == "basic":
            print("You can choose a Debris Blaster or a Debris Sucker.  This is just a basic Roomba!")
            choice = input("Type a 1 for a Debris Blaster and a 2 for the Debris Sucker")
            if choice == 1:
                self.weapon = debris_blaster
                self.damage = self.weapon.attack_power + self.attack_power
            if choice == 2:
                self.weapon = debris_sucker
                self.damage = self.weapon.attack_power + self.attack_power

    def equip_weapon_for_computer(self):
        if self.type == "squish":
            self.weapon = super_sucker
            self.damage = self.weapon.attack_power + self.attack_power
        if self.type == "tank":
            self.weapon = debris_cannon
            self.damage = self.weapon.attack_power + self.attack_power
        if self.type == "basic":
            self.weapon = debris_sucker
            self.damage = self.weapon.attack_power + self.attack_power

    def robot_attack(self, dino):
        damage = self.damage - dino.scales
        dino.health -= damage
        self.battery_charge -=10

    def robot_defense(self):
        self.battery_charge += 20
        defense = self.armor + 10
        return defense

