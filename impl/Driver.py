class Driver:
    starting_number: int = 0
    first_name: str = ""
    last_name: str = ""


    def __init__(self, first_name: str, last_name: str, starting_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.starting_number = starting_number

    def __str__(self) -> str:
        return f"({self.starting_number}) {self.name}"

    def __eq__(self, other) -> bool:
        return self.starting_number == other.starting_number \
               and self.first_name == other.first_name \
               and self.last_name == other.last_name

    @property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"


if __name__ == '__main__':
    michail_gorbatschow = Driver("Michail", "Gorbatschow", 0)


    print(f"1: {michail_gorbatschow.name}")

    michail_gorbatschow.first_name = "Peter"

    print(f"2: {michail_gorbatschow.name}")

    # michail_gorbatschow.


    # print(michail_gorbatschow)

    print(f"Jetzt gebe ich den Namen dieses Driver-Objekts ist: {michail_gorbatschow.first_name} {michail_gorbatschow.last_name}")


"""

@property
  
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
