from impl.CompetitorsGenerator import CompetitorsGenerator
from impl.CompetitorsList import CompetitorsList
from impl.Motorcycle import Motorcycle, MotorcycleType
from impl.Race import Race
from impl.Trike import TrikeType, Trike
from impl.Vehicle import Vehicle, EngineType


class RacingGame:
    def run(self) -> None:
        dodge_charger = Vehicle("Dodge", "Charger", 478, EngineType.gasoline)
        print(dodge_charger)

        harley_davidson = Motorcycle("Harley Davidson", "EasyRider", 98, EngineType.diesel, MotorcycleType.Dirtbike)
        print(f"Harley: {harley_davidson}")

        dreirad_trike = Trike("Harley Davidson", "EasyRider", 98, EngineType.diesel, TrikeType.Three_Seater)
        print(f"Trike: {dreirad_trike}")

        cg = CompetitorsGenerator()
        c = cg.get_random_competitor()
        print(f"Competitor: {c}")

        my_list = CompetitorsList()
        my_list.add_competitor(cg.get_random_competitor())  # 1
        my_list.add_competitor(cg.get_random_competitor())  # 2
        my_list.add_competitor(cg.get_random_competitor())  # 3
        my_list.add_competitor(cg.get_random_competitor())  # 4
        my_list.add_competitor(cg.get_random_competitor())  # 5

        r = Race(my_list)
        r.generate_starting_lineup()
        r.race()
        print(f"Race Result: {r.race_result}")


if __name__ == '__main__':
    r = RacingGame()
    r.run()
