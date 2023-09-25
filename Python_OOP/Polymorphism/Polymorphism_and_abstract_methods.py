# Polymorphism is the ability to work with completely 
# different objects (Python language) in a single way.

class Goods:
    def __init__(self, name, weight, price):
        print("init MixinLog")
        self.name = name
        self.weight = weight
        self.price = price
 
    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class NoteBook(Goods):
    pass

n = NoteBook("Acer", 1.5, 30000)

n.print_info()

class MixinLog:
    ID = 0
 
    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID
 
    def save_sell_log(self):
        print(f"{self.id}: the product was sold at 00:00 hours")

class NoteBook(Goods, MixinLog):
    pass

n = NoteBook("Lonovo", 1.3, 25000)

n.save_sell_log()
# AttributeError: 'NoteBook' object has no attribute 'id'

# And we see a mistake. Obviously, it is related to the 
# fact that the initializer was not called for the second 
# class of MixinLog. Why did this happen? As we already 
# know, when creating objects, the initializer is first 
# searched for in the child class, but since it is not 
# there, then in the first basic Goods. It is there, it 
# is executed, and this completes the initialization of 
# our NoteBook object. However, we also need to call the 
# initializer and the second base class MixinLog. In this 
# case, you can do this using the intermediary object 
# super(), which delegates the call to the __init__ method 
# of the MixinLog class: