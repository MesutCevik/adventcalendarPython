from random import shuffle
from typing import List, Any

from impl import CompetitorsList, Driver, Vehicle, Competitor


class Race:
    mesutsCompetitorListVariable: CompetitorsList
    starting_lineup: List['Competitor'] = []
    race_result: List['Competitor'] = []

    def __init__(self, competitors: CompetitorsList):
        self.mesutsCompetitorListVariable = competitors

    def race(self) -> None:
        self.race_result = self.starting_lineup
        shuffle(self.race_result)

        places = self.race_result
        for place, _ in enumerate(places, start=0):
            if place == 0:
                points = (len(self.race_result) - place + 1) * 2
            else:
                points = (len(self.race_result) - place + 1) * 1

            self.race_result[place].add_points(points)

        self.starting_lineup = self.race_result

    def generate_starting_lineup(self) -> List['Competitor']:
        for competitor in self.mesutsCompetitorListVariable.competitors:  # Nehme jedes Element in einer Liste competitor.
            self.starting_lineup.append(competitor)

        return self.starting_lineup

    def __str__(self) -> str:
        nice_competitors: str = ""
        for competitor in self.race_result:
            nice_competitors += f"Result Position: {[competitor.index(self.race_result)]}, {competitor}"

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