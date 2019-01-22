from impl import Driver, Vehicle


class Competitor:
    driver: Driver
    vehicle: Vehicle
    points = 0

    def __init__(self, driver: Driver, vehicle: Vehicle, points):
        self.driver = driver
        self.vehicle = vehicle
        self.points = points

    def get_points(self):
        return f"Points: {self.points}"

    def add_points(self, points_from_race: int):
        self.points += points_from_race

    def __str__(self) -> str:
        return f"Points: {self.points}; Driver: {self.driver.first_name} {self.driver.last_name}; Vehicle: {self.vehicle.manufacturer} {self.vehicle.model_name}"


"""
### Exercise 13 - Racing game competitors
 
 Generate a CompetitorsList which holds a Competitor with a Driver and Vehicle.
  
  1. Create class `CompetitorsGenerator`, which randomly generates drivers and related vehicles as a `Competitor`.
  2. Create class `Competitor` storing the assigment of the derived classes of `Vehicle` and `Driver` with:
     * _getPoints()_ => returns the actual points as int
     * _addPoints(int)_ => add's points from a race
  3. Create class `CompetitorsList` storing `Competitor`:
     * _addCompetitor(Competitor competitors)_
     * _getCompetitors()_ => which returns a list of `Competitor`
     * _toString()_ => method, which concatenate the contained toString() methods. This will generate a String like '[Points] [Driver] [Vehicle]'
  4. Add useful unit tests
  5. Visualize created classes with plantuml as class diagram, inclusive associations.

"""