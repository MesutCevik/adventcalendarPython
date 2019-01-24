from impl.Driver import Driver
from impl.Vehicle import EngineType, Vehicle


class Competitor:
    driver: Driver
    vehicle: Vehicle
    points = 0
    unique_id = 0

    def __init__(self, driver: Driver, vehicle: Vehicle, points: int, unique_id: int):
        self.driver = driver
        self.vehicle = vehicle
        self.points = points
        self.unique_id = unique_id

    def get_points(self) -> str:
        return f"Points: {self.points}"

    def add_points(self, points_from_race: int) -> None:
        self.points += points_from_race

    def __str__(self) -> str:
        # return f"Points: {self.points}; Driver: {self.driver.first_name} {self.driver.last_name}; Vehicle: {self.vehicle.manufacturer} {self.vehicle.model_name}"
        return f"({self.points}) {self.driver.first_name} {self.driver.last_name}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.unique_id == other.unique_id and self.driver == other.driver


if __name__ == '__main__':
    michail_gorbatschow = Driver("Michail", "Gorbatschow", 0)
    peter = Driver("Michail1", "Gorbatschow1", 0)
    dodge_charger = Vehicle("Dodge", "Charger", 478, EngineType.diesel)

    c1 = Competitor(michail_gorbatschow, dodge_charger, 0, 0)
    c2 = Competitor(peter, dodge_charger, 0, 0)

    if c1 == c2:
        print(f"😀 {c1} and {c2} are equal")
    else:
        print(f"😔 {c1} and {c2} are NOT equal")

    print(michail_gorbatschow.first_name)
    print(michail_gorbatschow.last_name)
    print(michail_gorbatschow.starting_number)

    print(michail_gorbatschow)

    print(F"{michail_gorbatschow.first_name} {michail_gorbatschow.last_name}")