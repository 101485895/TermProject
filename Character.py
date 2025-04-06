import random
class Character:
    def __init__(self):
        combat_roll = random.randint(0,6)
        health_roll = random.randint(0,6)
        self.__combat_strength =combat_roll
        self.__health_points = health_roll

    
    @property
    def combat_strength(self):
        return self.__combat_strength
    @combat_strength.setter
    def combat_strength(self, new_value):
        self.__combat_strength = new_value
    @property
    def health_points(self):
        return self.__health_points
    @health_points.setter
    def health_points(self, new_health):
        self.__health_points = new_health

    def __del__(self):
        print("The garbage collector has automatically destroyed the Character object")