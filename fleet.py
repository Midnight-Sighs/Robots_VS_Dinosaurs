from robot import Robot


class Fleet:
    def __init__(self):
        self.robot_list =   [(Robot("Roomba 1000: Bob", 80)), 
                            (Robot("Roomba 2000: Anne", 100)),
                            (Robot("Roomba 3000: Rog", 120))]

    def display_fleet(self):
        for robot in self.robot_list:
            print(robot.name)
    
    def equip_fleet_weapons(self):
        for robot in self.robot_list:
            Robot.equip_weapon(robot)
            # print(robot.weapon.name) Printed for testing but don't want to forget how I called across