class Dinosaur:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = 100
        self.scales = 5
    
    def dinosaur_attack(self, robot):
        robot.hp -= (self.attack - robot.armor)
        self.stamina -= 10