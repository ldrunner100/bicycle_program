class bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        

class bike_shop(object):
    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory 
        self.stock = {}
        self.margin = margin / 100
        self.profit = 0.00
        
    def create_inventory(self):
        for bike in self.inventory:
            self.stock[bike] = 10
    
    def sales(self, name):
        self.stock[name] -= 1
        self.profit += name.cost * self.margin
        
class customers(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.garage = []
    def buy(self, name):
        if name.cost <= self.budget:
            self.budget -= name.cost
            self.garage.append(name.model)
            Mikes_Bikes.sell(name)
            print (str(self.name) + ' bought ' + str(name.model) + ' bike for ' + str(name.cost) + ' dollars')
            print (str(self.name) + ' has ' + str(self.budget) + ' dollars left in their fund.')
        else:
            print(self.name + ' cannot afford that bike')