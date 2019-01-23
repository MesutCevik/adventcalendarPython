from enum import Enum

from impl.Vehicle import Vehicle, EngineType


class TrikeType(Enum):
    One_Seater = 1
    Two_Seater = 2
    Three_Seater = 3


class Trike(Vehicle):
    trike_type: TrikeType

    def __init__(self, manufacturer, model_name, horsepower, engine_type: EngineType, trike_type: TrikeType):
        super().__init__(manufacturer, model_name, horsepower, engine_type)
        self.trike_type = trike_type

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model_name}, {self.horsepower}hsp, " \
            f"{self.engine_type.name} {self.trike_type.name}."
