from robot import Robot

class Fleet:
    def __init__(self):
        self.robot_list =   [(Robot("Roomba 1000 Bob", 80)), 
                            (Robot("Roomba 2000", 100)),
                            (Robot("Roomba 3000", 120))]

    def display_fleet(self):
        for robot in self.robot_list:
            print(robot.name)