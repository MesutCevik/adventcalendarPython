class Driver:

    startingNumber = 0


    # CONSTRUCTOR with INSTANCE VARIABLES
    def __init__(self, firstName, lastName, startingNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.startingNumber = startingNumber


    # GETTER-METHODS
    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

    def get_startingNumber(self):
        return self.startingNumber


    # @Override-METHOD
    def __str__(self) -> str:
        result = "(" + str(self.get_startingNumber()) + ") " + self.get_firstName() + " " + self.get_lastName()
        return result



if __name__ == '__main__':
    michailGorbatschow = Driver("Michail", "Gorbatschow", 0)
    print(michailGorbatschow.get_firstName())
    print(michailGorbatschow.get_lastName())
    print(michailGorbatschow.get_startingNumber())
    print(michailGorbatschow)

    print(michailGorbatschow.firstName + " " + michailGorbatschow.lastName)


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