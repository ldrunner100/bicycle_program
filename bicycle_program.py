class bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def __repr__(self):
        return "{0} weight is {1} lbs. {0} costs ${2} to make" .format(self.model, self.weight, self.cost)
        

class bike_shop(object):
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory 
    
    def sales_price(self, bicycle):
        price = (bicycle.cost * 1.20)
        return price
        
class customers(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        
    def __repr__(self):
        return "this is {0}, he has ${1} to spend on a bike." .format(self.name, self.fund)
        
        
        
        
        
if __name__ == '__main__':
   
   inventory = []
   customer = []
   inventory.append(bicycle("xray", 10, 300))
   inventory.append(bicycle("sloop", 8, 400))
   inventory.append(bicycle("flame", 6, 500))
   inventory.append(bicycle("rocket", 5, 700))
   inventory.append(bicycle("superman", 4.5, 1000))
   inventory.append(bicycle("basic", 11, 250))    
   customer.append(customers("jack", 500))
   customer.append(customers("bob", 200))
   customer.append(customers("joe", 1000))
   customer.append(customers("bill", 250))
   #print(inventory, customer)
   
   print (bike_shop("wheels", inventory))
   
   
    
    
        

        
        
    
    