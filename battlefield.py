from fleet import Fleet
from herd import Herd

def dinosaur_attack(dinosaur, robot):
    robot.hp -= dinosaur.attack

def robot_attack(robot, dinosaur):
    dinosaur.hp -= robot.weapon.attack

class Battlefield:
    def __init__(self):
        self.player_name = self.display_welcome()
        self.fleet = Fleet()
        self.herd = Herd()
        self.commence = self.battle()

    def display_welcome(self):
        print("Welcome to our feature battle of Dinosaurs vs Robots!  We have beings from across the galaxy that have prepared teams for you to battle with!  Today, we have the Roombers supplying fleets of modified (and enlarged!) Roombas!  From the planet Jurrrrasic, we have herds of dinosaurs for you to choose from!")
        self.player_name = input("Tell us, master commander, what would you like to be referred to as today?  You don't have to use a name.  You could be whoever or whatever you wish today!  ")
        print("Your name is " + self.player_name+".  Huh.  Interesting...")

    def battle(self):
        d=0
        r=0
        while r <=2 or d <=2:
            print("The dinosaur gnaws at a Roomba.")
            self.herd.dino_list[d].dinosaur_attack(self.fleet.robot_list[r])
            print(self.fleet.robot_list[r].hp)
            if self.fleet.robot_list[r].hp >= 0:
                print("A robot has died.")
                r += 1
            if r == 2 and self.fleet.robot_list[2].hp >= 0:
                print("THE DINOSAURS ARE VICTORIOUS! RAWR!")
                break
            print("The roomba attempts to fire debris at the dinosaur.")
            self.fleet.robot_list[r].robot_attack(self.herd.dino_list[d])
            print(self.herd.dino_list[d].hp)
            if self.herd.dino_list[d].hp >= 0:
                print("NOOO!! A dino has fallen!!")
                d +=1
            if d == 2 and self.herd.dino_list[2].hp >= 0:
                print("The roombas are taking over the world.  ")