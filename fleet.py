from robot import Robo

class Fleet:
    def __init__(self, list):
        self.list = list


robo_squish_one = Robo("Mega Roomba ++", "Art", 80, 0, 5)
robo_squish_two = Robo("Mega Roomba ++", "Mary", 80, 0, 5)
robo_basic = Robo("Roomba", "Bob", 100, 5, 0)
robo_tank_one = Robo("Armored Roomba +", "Patrick", 120, 10, 0)
robo_tank_two = Robo("Armored Roomba +", "Anne", 120, 10, 0)

balanced_robots = [robo_squish_one, robo_basic, robo_tank_one]
squish_robots = [robo_squish_one, robo_squish_two, robo_basic]
tank_robots = [robo_tank_one, robo_tank_two]

#create fleet - pick from balanced, glass cannon, or tanky build