class Bank:
    def __init__(self, name, balance=0):
        self.name=name
        self.balance=balance
    '''def instance is just for any activity formed by 
       attributes or properties and representing that activity by attritbutes return print 
       + activity or instance also have attributes or property
       so make those property related to old attributes'''
    def deposite(self, amount):
        self.balance= self.balance + amount
        return (f"{amount} deposites in account of {self.name}" )
    
    def withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient balance for withdrawal from account of {self.name}"
        else:
            self.balance -= amount
            return f"{amount} withdrawn from account of {self.name}"
        
    def get_balance (self):
             return self.balance
        
        

account1 = Bank("priyanshu boran", 1000)
print(account1.name)  # Output: priyanshu boran
print(account1.get_balance())
account1.get_balance()       

