#no need to def parent cl;ass by init just give motto of full family eg. area
#just make return of parent class then
#make child class with CLASS CHILD1(PARENT) THERN DEFINE EITHER MOTTO OR INIT (INIT IF HAVE ATTRIBUTES RATHER THAN SELF )
class Animal():                                                            
    def speak(self):
        return f"animal makes sound"
    
class Dog(Animal):                                                            
    def speak(self):
        return f"bhau"
    
class Cat(Animal):                                                            
    def speak(self):
        return f"mew" 

doggy=Dog()
kitty=Cat()  
print(doggy.speak())
print(kitty.speak())        

#making attributes in child

class Shape():                                                            
    def area(self):
        return f"finds area of shapes"
    
class Rectangle(Shape):                                                            
    def __init__(self, lenght, breadth):
        self.length=lenght
        self.breadth=breadth
    
    def area(self):
      return self.length * self.breadth

 
    
class Circle(Shape):                                                            
    def __init__(self, radius):
     self.radius=radius

    def area(self):
      return self.radius * 2 * 3.14
    
objectarec=Rectangle(3,4)
objectcircle=Circle(3)  
print(objectarec.area())
print(objectcircle.area())      


