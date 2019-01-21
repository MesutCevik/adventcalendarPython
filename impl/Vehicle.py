from enum import Enum


class EngineType(Enum):
    electric = 1
    diesel = 2
    gasoline = 3


class Vehicle:

    # Wo müssen type hints plaziert werden?
    firstName: str

    # CONSTRUCTOR with INSTANCE VARIABLES
    def __init__(self, manufacturer, modelName, horsepower, engineType):
        self.manufacturer = manufacturer
        self.modelName = modelName
        self.horsepower = horsepower
        self.engineType = engineType


    # GETTER-METHODS
    def get_manufacturer(self):
        return self.manufacturer

    def get_modelName(self):
        return self.modelName

    def get_horsepower(self):
        return self.horsepower

    def get_engineType(self):
        return self.engineType

    # @Override-METHOD
    def __str__(self):
        return self.get_manufacturer() + " " + self.get_modelName() + ", " + self.get_engineType() + ", " + str(self.get_horsepower()) + "hsp."

if __name__ == '__main__':
    dodgeCharger = Vehicle("Dodge", "Charger", 478, "gasoline")
    print(dodgeCharger.get_manufacturer())
    print(dodgeCharger.get_modelName())
    print(dodgeCharger.get_horsepower())
    print(dodgeCharger.get_engineType())

    print("Dieses Fahrzueg ist ein: " + dodgeCharger.manufacturer + " " + dodgeCharger.modelName + ".")

    print(dodgeCharger)


"""
### Exercise 11 - Racing game base classes

Implement basic class lineup.

 1. Define Class `Driver` with following methods:
    * _Constructor_ => All needed attributes
    * _getName()_ => returns Lastname, Firstname as String
    * _getStartingNumber()_ => returns the starting number as an int
    * _toString()_ => generates a String like '(1) Joe Cewl'
 2. Define Class `Vehicle` with following  methods:
    * _Constructor_ => All needed attributes
    * _getManufacturer()_ - returns the manufacturer like 'Skoda' as String
    * _getName()_ - returns the vehicle name like 'Fabia' as String
    * _getHorsepower()_ - returns the engines horsepower as int
    * _getEngineType_ - returns one of `[electric, diesel, gasoline]` as an Enum
    * _toString()_ - returns the vehicle as String like 'Skoda Fabia, gasoline, 25hps'
 3. Add useful unit tests
 4. Visualize created classes with plantuml as class diagram, inclusive associations.
"""