class Attack:
    def __init__ (self, name, attack):
        self.name = name
        self.attack_power = attack

attack_claws = Attack("Claws", 10)
attack_bite = Attack("Bite", 15)
attack_spit = Attack("Spit", 5)

squish_attacks = (attack_claws, attack_bite)
basic_attacks = (attack_claws, attack_bite)
tank_attacks = (attack_claws, attack_bite)