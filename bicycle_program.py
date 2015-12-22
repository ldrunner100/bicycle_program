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
        
class customers(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        
    def __repr__(self):
        return "this is {0}, he has ${1} to spend on a bike." .format(self.name, self.fund)
        
        
        
        
        
if __name__ == '__main__':
   print bike_shop("mikes bikes", 6)
   print bicycle("xray", 10, 300)
   print bicycle("sloop", 8, 400)
   print bicycle("flame", 6, 500)
   print bicycle("rocket", 5, 700)
   print bicycle("superman", 4.5, 1000)
   print bicycle("basic", 11, 250)
   print customers("bob", 200)
   print customers("jack", 500)
   print customers("joe", 1000)
   print customers("bill", 250)
   
    
    
        

        
        
    
    