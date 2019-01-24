from random import shuffle
from typing import List, Any

from impl import CompetitorsList, Driver, Vehicle, Competitor


class Race:
    mesutsCompetitorListVariable: List['Competitor']
    starting_lineup: List['Competitor'] = []
    race_result: List['Competitor'] = []
    race_number: int
    amount_of_races: int

    def __init__(self, competitors: List['Competitor'], race_number: int, amount_of_races: int):
        self.mesutsCompetitorListVariable = competitors
        self.race_number = race_number
        self.amount_of_races = amount_of_races

    def race(self) -> None:
        self.race_result = list(self.starting_lineup)
        shuffle(self.race_result)

        for place, _ in enumerate(self.race_result, start=0):
            if place == 0:
                points = (len(self.race_result) - place + 1) * 2
            else:
                points = (len(self.race_result) - place + 1) * 1

            self.race_result[place].add_points(points)

        self.starting_lineup = list(self.race_result)

    def generate_starting_lineup(self) -> List['Competitor']:
        self.starting_lineup = list(self.mesutsCompetitorListVariable)
        return self.starting_lineup

    def __str__(self) -> str:
        nice_competitors: str = ""
        for place in range(0, len(self.race_result)):
            competitor = self.race_result[place]
            nice_competitors += f"{place + 1} {competitor.points}, {competitor.driver.first_name} {competitor.driver.last_name}; "

        return nice_competitors



"""
### Exercise 15 - Racing game race()
  
  Let'em race!
   
  1. Add and implement following methods to class `Race`:
      * enhance the constructor with the last result so that the starting lineup can be setup correctly.
      * _race()_ => run's the race - generate the final placement randomly
      * _getResult()_ => race result as an ordered list of competitors. The list is ordered by the placement, like 1s is first, 2nd is second, ....
      * _toString()_ => race result as string, like '[Result Position] [Competitor]'
  2. Store the race result points to the `Competitor`
      * for the first place the driver gets '[count of drivers - place + 1] * 2' points
      * all other placements gives the drivers '[count of drivers - place + 1] * 1' points
  3. Generate the next starting lineup from the drivers last race position.
  4. Add useful unit tests
  3. Visualize created classes with plantuml as class diagram, inclusive associations.
"""