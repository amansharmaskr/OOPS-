
'''This puts restrictions on accessing variables and methods directly and
 can prevent the accidental modification of data.'''


class Car():
    def __init__(self, attribute1, attribute2, attribute3):
        self.__attribute1 = attribute1  # Private attribute
        self.__attribute2 = attribute2  # Private attribute
        self.attribute3 = attribute3     # Public attribute

def getinfo(car):                        
    return car.attribute3

# Create an instance of Car
car = Car("abc", "pqr", "xyz")

# Use getinfo function to retrieve attribute3
print(getinfo(car))  # Output: xyz





class Car():
    def __init__(self, attribute1, attribute2, attribute3):
        self.__attribute1 = attribute1  # Private attribute
        self.__attribute2 = attribute2  # Private attribute
        self.attribute3 = attribute3     # Public attribute

def getinfo(car):
    return car.attribute2

# Create an instance of Car
car = Car("abc", "pqr", "xyz")

# Use getinfo function to retrieve attribute3
print(getinfo(car))  # Output: error






#achieveing value of private attribute inside class

class Car():
    def __init__(self, attribute1, attribute2, attribute3):
        self.__attribute1 = attribute1  # Private attribute
        self.__attribute2 = attribute2  # Private attribute
        self.attribute3 = attribute3     # Public attribute

    def getinfo(self):
      return self.__attribute2

# Create an instance of Car
car = Car("abc", "pqr", "xyz")

# Use getinfo function to retrieve attribute3
print(car.getinfo())  # Output: pqr

class Car():
    def __init__(self, attribute1, attribute2, attribute3):
        self.__attribute1 = attribute1  # Private attribute, can be access through base class only
        self._attribute2 = attribute2  # Protected attribute , can be accessed through drive class also
        self.attribute3 = attribute3     # Public attribute, access in whatever way you like


class Vehicle(Car):
    def __init__(self, attribute1, attribute2, attribute3):
      super().__init__(attribute1, attribute2, attribute3)

    def activity(self):
      return self._attribute2

vehicle = Vehicle("abc", "pqr", "xyz")
print(vehicle.activity())
  # Output: pqr



#encapsulation using getter and setter

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age >= 0:  # Basic validation
            self.__age = age
        else:
            print("Age cannot be negative")

# Create an instance of Person
person = Person("Alice", 30)

# Accessing attributes using getter methods
print(f"Name: {person.get_name()}")  # Output: Name: Alice
print(f"Age: {person.get_age()}")    # Output: Age: 30

# Using setter methods to modify attributes
person.set_name("Bob")
person.set_age(25)

# Accessing modified attributes
print(f"Name: {person.get_name()}")  # Output: Name: Bob
print(f"Age: {person.get_age()}")    # Output: Age: 25

# Trying to set negative age (will print error message)
person.set_age(-5)

# Accessing age again to verify it hasn't changed
print(f"Age: {person.get_age()}")    # Output: Age: 25 (unchanged due to validation in setter)


