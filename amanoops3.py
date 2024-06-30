class Calculator():
    def __init__(self, a):
        self.a=a
       
    def Cube(self):
        return self.a * self.a * self.a
    def Square(self):
        return self.a * self.a 
    def SquareRoot(self):
        return self.a **(1/2)
    
    #print      object.attribute and object.activity() while calling
calculate= Calculator(5)
print(calculate.Square())
print(calculate.a)





class Calculator():
    def __init__(self, a=4):
        self.a=a
       
    def Cube(self):
        return self.a * self.a * self.a
    def Square(self):
        return self.a * self.a 
    def SquareRoot(self):
        return self.a **(1/2)
    
    #print      object.attribute and object.activity() while calling
calculate= Calculator()
   # after providing vale of attribute in class , providing vale value after making and using object .
   #now result or output according to ppriority i.e object 
calculate.a=25 
print(calculate.Square())
print(calculate.a)







class Calculator():
    def __init__(self, a):
        self.a=a
       
    def Cube(self):
        return self.a * self.a * self.a
    def Square(self):
        return self.a * self.a 
    def SquareRoot(self):
        return self.a **(1/2)
   # use of static method without using self 
    @staticmethod
    def usingstaticmethod():
        print ("hello")
    
    #print      object.attribute and object.activity() while calling
calculate= Calculator(5)
print(calculate.Square())
print(calculate.a)
calculate.usingstaticmethod()







    
