from impl import Competitor
from impl.Motorcycle import Motorcycle, MotorcycleType
from impl.Trike import TrikeType, Trike
from impl.Vehicle import Vehicle, EngineType


class RacingGame:
    def run(self):
        dodge_charger = Vehicle("Dodge", "Charger", 478, EngineType.gasoline)
        print(dodge_charger)

        harley_davidson = Motorcycle("Harley Davidson", "EasyRider", 98, EngineType.diesel, MotorcycleType.Dirtbike)
        print(f"Harley: {harley_davidson}")

        trike = Trike("Harley Davidson", "EasyRider", 98, EngineType.diesel, TrikeType.Three_Seater)
        print(f"Trike: {trike}")

        ronald_reagan = Competitor()



if __name__ == '__main__':
    r = RacingGame()
    r.run()
