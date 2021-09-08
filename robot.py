from weapon import Weapon

class Robo:
    def __init__(self, type, name, health, armor, attack):
        self.type = type
        self.name = name
        self.health = health
        self.armor = armor
        self.attack_power = attack
        self.battery_charge = 100

super_sucker = Weapon("Super Sucker", 20)
debris_cannon = Weapon("Debris Cannon", 15)
debris_blaster = Weapon("Debris Blaster", 5)
debris_sucker = Weapon("Debris Sucker", 10)

squish_equipable_weapons = (super_sucker, debris_cannon)
basic_equipable_weapons = (debris_cannon, super_sucker)
tank_equipable_weapons = (debris_cannon, super_sucker)

#What can each robot do?
#They can equip an item that stays the same through the battle
# they can attack on their turn
#they can defend on their turn