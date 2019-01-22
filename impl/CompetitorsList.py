from impl import Competitor


class CompetitorsList:
    competitor: Competitor
    competitors: str = list()
    competitors_in_string: str = list()

    def __init__(self, competitor, competitors):
        self.competitor = competitor
        self.competitors = competitors

    def add_competitor(self, competitor: Competitor):
        self.competitors.__add__(competitor)

    def get_competitors(self):
        return self.competitors

    def __str__(self, competitors_in_string=None) -> str:
        for self.competitor in self.competitors:
            self.competitors_in_string.__add__(f"Competitor: {self.competitor}; ")
        return competitors_in_string


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