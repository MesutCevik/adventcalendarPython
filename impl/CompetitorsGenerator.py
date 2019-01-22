import random
from typing import List

from impl.Vehicle import Vehicle, EngineType
from impl.Competitor import Competitor
from impl.Driver import Driver


class CompetitorsGenerator:
    starting_number: int = 0

    def get_random_driver(self) -> Driver:
        driver_firstnames: List[str] = ["Michael", "Niki", "Fernando", "Lewis", "Alain"]
        driver_lastnames: List[str] = ["Schumacher", "Lauda", "Alonso", "Hamilton", "Prost"]

        random_driver_firstname = random.choice(driver_firstnames)
        random_driver_lastname = random.choice(driver_lastnames)

        self.starting_number += 1

        return Driver(random_driver_firstname, random_driver_lastname, self.starting_number)

    def get_random_vehicle(self):
        vehicle_manufacturer: List[str] = ["Dodge", "Ford", "Porsche", "Mercedes"]
        vehicle_model_name: List[str] = ["Challenger", "GT20", "Carrera_GT4", "Silberpfeil"]
        vehicle_horsepower: List[int] = [379, 400, 323, 395]

        random_vehicle_manufacturer = random.choice(vehicle_manufacturer)
        random_vehicle_model_name = random.choice(vehicle_model_name)
        random_vehicle_horsepower = random.choice(vehicle_horsepower)
        random_vehicle_enginge_type = random.choice(list(EngineType))

        return Vehicle(random_vehicle_manufacturer, random_vehicle_model_name, random_vehicle_horsepower,
                       random_vehicle_enginge_type)

    def get_random_competitor(self):
        driver: Driver = self.get_random_driver()
        vehicle: Vehicle = self.get_random_vehicle()

        return Competitor(driver, vehicle, 0)
