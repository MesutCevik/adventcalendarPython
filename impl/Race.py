from typing import List

from impl import CompetitorsList, Driver, Vehicle, Competitor


class Race:
    competitors: CompetitorsList
    starting_lineup: str = list()

    driver: Driver
    vehicle: Vehicle

    def race(self, competitors):
        self.competitors = competitors
        self.starting_lineup = 0

    def generate_starting_lineup(self, competitors):
        for competitor in self.competitors:  # Nehme jedes Element in einer Liste competitor.
            self.starting_lineup.__add__(competitor.driver.last_name + competitor.driver.first_name + competitor.vehicle.manufacturer)

        return self.starting_lineup

    def get_starting_lineup(self):
        return self.starting_lineup

    def __str__(self):
        nice_competitors = self.competitors
        return f"{self.manufacturer} {self.model_name}, {self.horsepower}hsp, {self.engine_type.name}."




"""
### Exercise 14 - Racing game lineup

  Implement the race with it's starting lineup.

  1. Add and implement following methods to class `Race`:
      * _generateStartingLineup()_ => in the 1st race, the starting lineup is ordered by _drivers last name_, _drivers first name_, _vehicles manufacturer_.
      * _getStartingLineup()_ => returns the ordered `CompetitorsList`.
      * _toString()_ => starting lineup as String, like '[Position in StartingLineup] [Competitor]'
  2. Add useful unit tests
  3. Visualize created classes with plantuml as class diagram, inclusive associations.
"""