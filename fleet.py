from robot import Robot

class Fleet:
    def __init__(self):
        self.robot_list = []

    def add_robots_to_list(self):
        robot1 = Robot("Roomba 1000 Bob", 80)
        robot2 = Robot("Roomba 2000", 100)
        robot3 = Robot("Roomba 3000", 120)

        self.robot_list.append(robot1) 
        self.robot_list.append(robot2)
        self.robot_list.append(robot3)

    def display_fleet(self):
        for robot in self.robot_list:
            print(robot)