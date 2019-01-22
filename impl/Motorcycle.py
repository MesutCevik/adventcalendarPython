from enum import Enum

from impl.Vehicle import Vehicle


class MotorcycleType(Enum):
    Allrounder = 1
    Chopper = 2
    Enduro = 3
    Dirtbike = 4
    Caferacer = 5
    Racer = 6


class Motorcycle(Vehicle):
    motorcycle_type: MotorcycleType

    def __init__(self, manufacturer, model_name, horsepower, engine_type, motorcycle_type: MotorcycleType):
        super().__init__(manufacturer, model_name, horsepower, engine_type)
        self.motorcycle_type = motorcycle_type

    def __str__(self):
        return f"{self.manufacturer} {self.model_name}, {self.engine_type.name}, {self.horsepower} hsp, " \
            f"{self.motorcycle_type.name}."
