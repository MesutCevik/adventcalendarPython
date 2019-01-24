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
    competitors_list: CompetitorsList
    current_line_up: List['Competitor']  # Liste mit Listen der race_results = current_line_up
    seasonstart_line_up: List['Competitor']  # Liste zum Saisonbeginn

    def __init__(self, amount_of_races: int):
        self.amount_of_races = amount_of_races

        cg = CompetitorsGenerator()  # Call the CompetitorsGenerator()-method and assign the generated object to "cg".
        self.competitors_list = CompetitorsList()  # Call the CompetitorsList()-method and assign the generated object to "my_list".
        self.competitors_list.add_competitor(cg.get_random_competitor())  # 1st competitor
        self.competitors_list.add_competitor(cg.get_random_competitor())  # 2
        self.competitors_list.add_competitor(cg.get_random_competitor())  # 3
        self.competitors_list.add_competitor(cg.get_random_competitor())  # 4
        self.competitors_list.add_competitor(cg.get_random_competitor())  # 5
        self.current_line_up = self.competitors_list.competitors
        self.seasonstart_line_up = list(self.current_line_up)

        print(f"Race Result: {cg.get_random_competitor()}")

    def run_season(self):
        for race_number in range(1, self.amount_of_races + 1):
            print(f"{race_number }/{self.amount_of_races} starting")
            self.run(race_number)

    def run(self, race_number: int) -> None:

        current_race = Race(self.current_line_up, race_number, self.amount_of_races)
        current_race.generate_starting_lineup()
        print(f"Starting: {str(current_race.starting_lineup)}")
        current_race.race()
        print(f"Result  : {str(current_race.race_result)}")

        differences = self.calculate_differences_between_two_races(race_number, self.current_line_up, current_race.race_result)
        print(f"Differences  : {differences}")

        current_standing = self.get_standing_for(current_race)
        print(f"Result  : {current_standing}")

        self.current_line_up = list(current_race.race_result)

    def calculate_differences_between_two_races(self, race_number: int, previous_race: List['Competitor'], current_race: List['Competitor']) -> str:
        """
        toString() => the standing as String like '[Place] [Placement shift] [Competitor]'
        for the shift up ↑
        for shift down ↓
        for a remained placement →
        :return:
        """
        if race_number == 1:
            return "no previous race yet"

        result = ""
        for place in range(0, len(current_race)):
            competitor = current_race[place]

            for previous_place in range(0, len(previous_race)):
                prev_competitor = previous_race[previous_place]

                if competitor != prev_competitor:
                    continue

                result += f"[{place}] "
                if place == previous_place:
                    result += "→"
                elif place < previous_place:
                    result += "↑"
                else:
                    result += "↓"

                result += f" {competitor.driver.first_name} {competitor.driver.last_name} "
                break

        return result






    def get_standing_for(self, current_race: Race) -> str:  # Methode zum abrufen des aktuellen Stands. Brauche List of lists!!!
        if current_race.race_number == 1:
            return f"Standing at race 0: {r.seasonstart_line_up}"
        elif current_race.race_number == current_race.amount_of_races:
            return f"Final standing at season end: {r.current_line_up}"  # NEU!!!
        else:
            return f"Standing at race {current_race.race_number}: {current_race}"  # NEU!!!





if __name__ == '__main__':
    r = RacingGame(8)
    # r.run()
    r.run_season()


"""
### Exercise 16 - Racing game season
  
  Implement and a race season. In one season 1..n races can happen. Compute the final result.
  
  2. Add and implement following methods to class `RacingGame`
      * enhance the constructor with the amounts of races. <done>
      * _runSeason()_ => run's the amount of races that are happening this season. <done>
      * _getStanding()_ => holds the competitors in their actual standing as a List, order this list by: <Dabelleeee>
        * without a race by _drivers last name_, _drivers first name_, _vehicles manufacturer_
        * after a race has happened by the competitors points
        * Store the placements shift after a race, means if a competitors went places up, down or remained.
      * _toString()_ => the standing as String like '[Place] [Placement shift] [Competitor]'
        * for the shift up &#8593;
        * for shift down &#8595;
        * for a remained placement &#8594;
  3. Add useful unit tests
  4. Visualize created classes with plantuml as class diagram, inclusive associations."""