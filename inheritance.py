class Veichle:
    def __init__(self,
                 brand : str,
                 speed : int
                 ) -> None:
        self.brand = brand
        self.speed = speed

    def honk(self):
        print(f"{self.brand} honked.")

class Motorcycle(Veichle):
    def info(self):
        print(f"{self.brand} has speed of {self.speed} km/s")

motor = Motorcycle("Honda", 30)
motor.honk()
motor.info()