from bikes import bicycle
from bikes import bike_shop
from bikes import customers

inventory = []
customers = []
xray = inventory.append(bicycle("xray", 10, 300))
sloop = inventory.append(bicycle("sloop", 8, 400))
flame = inventory.append(bicycle("flame", 6, 500))
rocket = inventory.append(bicycle("rocket", 5, 700))
superman = inventory.append(bicycle("superman", 4.5, 1000))
basic = inventory.append(bicycle("basic", 11, 250))    
jack = customer.append(customers("jack", 500))
bob = customer.append(customers("bob", 200))
joe = customer.append(customers("joe", 1000))
bill = customer.append(customers("bill", 250))
   
   
Mikes_Bikes = bike_shop([xray, sloop, flame, rocket, superman], 20.00)
Mikes_Bikes.create_inventory()
for bike in Mikes_Bikes.stock:
    print ('Mikes_Bikes has ' + str(Mikes_Bikes.stock[bike]) + ' ' + str(bike.model) + 'bikes')
    
for customer in customers:
    print customer.name + ' has ' + str(customer.budget) + ' to spend.'
    print customer.name + ' can buy these bikes:'
    for key in Mikes_Bikes.stock:
        if key.cost * (1 + Mikes_Bikes.margin) <= customers.budget:
            print (key.model + ' costs ' + str(key.cost * (1 + Mikes_Bikes.margin)))
                
jack.buy(sloop)
joe.buy(superman)
bill.buy(basic)

print('Jack has the following bike in his garage: ' + str(jack.garage)
print('Joe has the following bike in his garage: ' + str(joe.garage)
print('Bill has the following bike in his garage: ' + str(bill.garage)

print('Mikes_Bikes has made ' + str(Mikes_Bikes.profit) + ' dollars profit, it has the following left in inventory:'
for key in Mikes_Bikes.stock:
    print(str(Mikes_Bikes.stock[key]) + ' ' + str(key.model) + ' bikes.'