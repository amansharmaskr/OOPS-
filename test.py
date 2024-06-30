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
