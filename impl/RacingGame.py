from typing import List

from impl.Competitor import Competitor
from impl.CompetitorsGenerator import CompetitorsGenerator
from impl.CompetitorsList import CompetitorsList
from impl.Motorcycle import Motorcycle, MotorcycleType
from impl.Race import Race
from impl.Trike import TrikeType, Trike
from impl.Vehicle import Vehicle, EngineType


class RacingGame:
    amount_of_races: int
    current_race: int = 0
    competitors_list: CompetitorsList
    current_line_up: List['Competitor']  # Liste mit Listen der race_results = current_line_up
    seasonstart_line_up: List['Competitor']  # Liste zum Saisonbeginn

    def __init__(self, amount_of_races: int):
        self.amount_of_races = amount_of_races

        cg = CompetitorsGenerator()  # Call the CompetitorsGenerator()-method and assing the generated object to cg.
        self.competitors_list = CompetitorsList()  # Call the CompetitorsList()-method and assing the generated object to my_list.
        self.competitors_list.add_competitor(cg.get_random_competitor())  # 1st competitor
        self.competitors_list.add_competitor(cg.get_random_competitor())  # 2
        self.competitors_list.add_competitor(cg.get_random_competitor())  # 3
        self.competitors_list.add_competitor(cg.get_random_competitor())  # 4
        self.competitors_list.add_competitor(cg.get_random_competitor())  # 5
        self.current_line_up = self.competitors_list.competitors
        self.seasonstart_line_up = list(self.current_line_up)

        print(f"Race Result: {cg.get_random_competitor()}")



    def run(self) -> None:
        r = Race(self.current_line_up)
        r.generate_starting_lineup()
        r.race()
        print(f"Starting: {str(r.starting_lineup)}")
        print(f"Result  : {str(r.race_result)}")

        self.current_line_up = list(r.race_result)

    def get_standing(self, current_race):  # Methode zum abrufen des aktuellen Stands. Brauche List of lists!!!
        if current_race == 0:
            return f"Standing at race 0: {r.seasonstart_line_up}"
        elif current_race == self.amount_of_races:
            return f"Final standing at season end: {r.current_line_up}"  # NEU!!!
        else:
            return f"Standing at race {current_race}: {r.current_line_up}"  # NEU!!!

    def run_season(self):
        for current_race in range(1, self.amount_of_races + 1):
            print(f"{current_race }/{self.amount_of_races} starting")
            self.run()



if __name__ == '__main__':
    r = RacingGame(8)
    # r.run()
    r.run_season()
