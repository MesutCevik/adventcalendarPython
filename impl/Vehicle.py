from enum import Enum


class EngineType(Enum):
    electric = 1
    diesel = 2
    gasoline = 3


class Vehicle:
    manufacturer: str
    model_name: str
    engine_type: EngineType
    horsepower: int

    def __init__(self, manufacturer, model_name, horsepower, engine_type: EngineType):
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.horsepower = horsepower
        self.engine_type = engine_type

    def __str__(self):
        return f"{self.manufacturer} {self.model_name}, {self.horsepower}hsp, {self.engine_type.name}."


if __name__ == '__main__':
    dodge_charger = Vehicle("Dodge", "Charger", 478, EngineType.diesel)

    print(dodge_charger.manufacturer)
    print(dodge_charger.model_name)
    print(dodge_charger.horsepower)
    print(dodge_charger.engine_type)
    print(dodge_charger.engine_type.name)

    print(f"Dieses Fahrzeug ist ein: {dodge_charger.manufacturer} {dodge_charger.model_name}.")

    print(dodge_charger)

"""
### Exercise 12 - Racing game with different vehicles

Implement different types of vehicle.
 
 1. Derive different types of vehicles from the base class `Vehicle`, like a _motorcycle_ or a _trike_.
 2. Add specific attributes to each of the new derived classes.
 4. Add get methods for the new attributes
 5. Enhance toString() method with the new attributes 
 3. Visualize created classes with plantuml as class diagram, inclusive associations.
 
"""

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
