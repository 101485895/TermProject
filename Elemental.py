from Monster import Monster
import random
class Elemental(Monster):
    def __init__(self):
        super().__init__()


    def control_weather(self):
        weather_conditions = ["rainy", "sunny", "snowy"]
        current_weather = random.choice(weather_conditions)
        print("    |", end="    ")
        input("The Elemental is controlling the weather!!(press enter)")
        print("    |", end="    ")
        input(f"The current weather is {current_weather}!(press enter)")
        return current_weather