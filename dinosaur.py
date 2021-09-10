class Dinosaur:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def dinosaur_attack(self, robot):
        robot.hp -= self.attack