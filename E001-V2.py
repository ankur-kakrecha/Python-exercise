# Exercise: E001-V2

# •  Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.
# •  Add a new member function to generate “display_name”.
# •  “display_name” has the text value as below.
#            1.	Vehicle category without parent then “Vehicle” 
#            2.	Car category with “Vehicle” as a parent then “Vehicle > Car”
#            3.	Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”
# •  Create 5 category objects with parent and child relation.
# •  Create 3 product objects in each category.
# •  Display the Category with its Code, Display Name, and all product details inside that category.
# •  Display product list by category (group by category, order by category name).

class category:
    def __init__(self,c_name,c_code,parent=None):
        self.c_name = c_name
        self.c_code = c_code
        self.parent = parent
        self.no_of_product = 0
        self.products=[]
    def generate_display_names(self):
        display_name = self.c_name
        if self.parent:
            display_name=self.parent.generate_display_names() + ">" + display_name
        return display_name
    # def show_category(self):
    #     print("category name : {0} , category code : {1} , display name : {2} ,number of product {3} , parent : {4}".format(self.c_name, \
    #         self.c_code, self.generate_display_names(), self.no_of_product,self.parent_name))
    def __str__(self):
        if self.parent:
            return f" category name = {self.c_name} , diaplay name = {self.generate_display_names()}, number of product ={self.no_of_product}, parent name= {self.parent.c_name}"
        else:
            return f" category name = {self.c_name} , diaplay name = {self.generate_display_names()}, number of product ={self.no_of_product}, parent name= None"
            

class Product:
    def __init__(self,p_name,p_code,category,price):
        self.p_name = p_name
        self.p_code = p_code
        self.category = category
        self.price = price
        category.no_of_product+=1
    def show_product(self):
        print("product name :{0}, code :{1},category name: {2}, price : {3}".format(self.p_name,self.p_code,self.category.c_name,self.price))
    @classmethod
    def sort(self,clist):
        n=len(clist)
        for i in range(0,n):
            for j in range(i+1,n):
                if clist[i].c_name > clist[j].c_name:
                    temp=clist[i].c_name
                    clist[i].c_name=clist[j].c_name
                    clist[j].c_name=temp
        for j in clist:
            print("=========",j.c_name,"=========")
            for i in j.products:
                print("product name :{0} , product code : {1} , product price : {2} ,category name : {3}".format(i.p_name,i.p_code,i.price,i.category.c_name))
                
                
vehicle=category("vehicle","v01")
car=category("car","c01",vehicle)
truck=category("truck","t01",vehicle)
petrol=category("petrol","p01",car)

vehicle.products.append(Product('vehicle1','v001',vehicle,120000))
vehicle.products.append(Product('vehicle2','v002',vehicle,110000))
vehicle.products.append(Product('vehicle3','v003',vehicle,100000))

car.products.append(Product('bmw','b001',car,9000000))
car.products.append(Product('mustung','m001',car,8000000))
car.products.append(Product('fortuner','f001',car,4500000))

truck.products.append(Product('ashok layland','as01',truck,1900000))
truck.products.append(Product('icer','i01',truck,1000000))
truck.products.append(Product('chota hathi','ch01',truck,900000))

petrol.products.append(Product('normal petrol','pt1',petrol,100))
petrol.products.append(Product('power petrol','pt2',petrol,110))
petrol.products.append(Product('bio petrol','pt3',petrol,120))

category_list=[vehicle,car,truck,petrol]
# Product_list=[c1,c2,c3,t1,t2,t3,p1,p2,p3]
for i in category_list:
    print("==============Category details==============\n")
    # i.show_category()
    print(i)
    # print(i.c_name,i.no_of_product,i.c_code,)
    print("product of",i.c_name,":\n")
    for j in i.products:
        j.show_product()     
    print()
print("============sorting============")
Product.sort(category_list)
