class Car():
    def __init__(self, name, origin):
        self.name=name
        self.origin=origin
    '''def instance is just for any activity formed by 
       attributes or properties and representing that activity by attritbutes return print '''
    def drive(self):
        return (f"name is {self.name} and origin is {self.origin} ok" )
        
        

c1=Car("mercedes", "usa") 
print(c1.drive())
print(c1.name)        



