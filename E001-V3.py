# Exercise: E001-V3 : 
# Create one class named “location” with members “name”, “code”.
# Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.
# Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”.
# --This method will return all “movement” objects which belong to the passed “product” as an argument.
# Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary and it contains “location” as key and actual stock of that product on that location as value.
# Create 4 different location objects.
# Create 5 different product objects.
# Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve. 
# Display movements of each product using the “movement_by_product” method.
# Display product details with its stock at various locations using “stock_at_locations”.
# Display product list by location ( group by location).

class Location:
    def __init__(self,name,code):
        self.name = name
        self.code = code
  
class product:
    def __init__(self,product_name,location,qty):
        self.product_name = product_name
        self.location = location
        self.qty = qty
        self.stock_at_location ={}
        self.stock_at_location.update({self.location.name:self.qty})
    def display(self):
        print("\nproduct details:",self.product_name)
        
         
class Movement:
    def __init__(self,from_location,to_location,product,quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
    
    def move(self):
        if self.product.stock_at_location.get(self.from_location.name) < self.quantity:
            raise ValueError("\ninsufficient stock of {0}".format(self.product.product_name))
        else:
            self.product.stock_at_location[self.from_location.name] -= self.quantity
            self.product.stock_at_location[self.to_location.name] =self.product.stock_at_location.get(self.to_location.name,0)+ self.quantity
              
    @staticmethod
    def movements_by_product(product):
        # print(product.product_name)
        for i in product:
            print("\n=========product name :",i.product_name,"=========")
            print("movement : ")
            
            for j in Movement_list:
                if i==j.product:
                    print(j.from_location.name,"->",j.to_location.name," : ",j.quantity)
    @staticmethod
    def group_by_location(L_list,p_list):
        for i  in L_list:
            print("\n========",i.name,"========")
            for j in p_list:
                for loc,qty in j.stock_at_location.items():
                    if loc == i.name:
                        j.display()
                        print("available qty :",qty)
    @staticmethod
    def stock_at_various_location(p_list):
        for i in p_list:
            print("==========",i.product_name,"==========")
            for key,val in i.stock_at_location.items():
                print(key ,":",val)
            print()

l1=Location('Rajkot','R1')
l2=Location('Ahemdabad','Am1')
l3=Location('Amreli','A1')
l4=Location('Junagadh','J1')

Location_list=[l1,l2,l3,l4]

p1=product('mobile',l1,50)
p2=product('air pods',l2,20)
p3=product('laptop',l3,30)
p4=product('freez',l4,15)           
product_list=[p1, p2, p3, p4]

m1=Movement(l1,l2,p1,3)    
m2=Movement(l2,l3,p2,5)
m3=Movement(l3,l4,p3,1)
m4=Movement(l4,l1,p4,7)
m5=Movement(l3,l1,p3,5)

Movement_list=[m1,m2,m3,m4,m5]

error = " "
Movement.movements_by_product(product_list)
try:
    for i in Movement_list:
        i.move()
except ValueError as e:
    error = e

product_list=[p1, p2, p3, p4]
print("\n product details with its stock at various locations\n ")
Movement.stock_at_various_location(product_list)

print("\n product details with group by locatio")  
Movement.group_by_location(Location_list,product_list)
print(error)