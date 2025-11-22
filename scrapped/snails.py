import random

class Snail:
    def __init__(self, name : str, speed : int, distance : int) -> None:
        self.name = name
        self.speed = speed
        self.distance = distance
    
    def randomizer_speed(self):
        return random.randrange(1,6) * self.speed

    def move(self) -> None:
        self.distance += self.randomizer_speed()
