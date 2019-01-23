from impl import Driver, Vehicle


class Competitor:
    driver: Driver
    vehicle: Vehicle
    points = 0

    def __init__(self, driver: Driver, vehicle: Vehicle, points):
        self.driver = driver
        self.vehicle = vehicle
        self.points = points

    def get_points(self) -> str:
        return f"Points: {self.points}"

    def add_points(self, points_from_race: int) -> None:
        self.points += points_from_race

    def __str__(self) -> str:
        # return f"Points: {self.points}; Driver: {self.driver.first_name} {self.driver.last_name}; Vehicle: {self.vehicle.manufacturer} {self.vehicle.model_name}"
        return f"({self.points}) {self.driver.first_name} {self.driver.last_name}"

    def __repr__(self):
        return str(self)