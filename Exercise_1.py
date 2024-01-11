#   
# •	Create one class named "category" with members "name", "code", "no_of_products"
# •	Create one class named "product" with members "name", "code", "category", "Price"
# •	Create three objects of a category.
# •	Create 10 different products. The code must be unique.
# •	Print category info with its no_of_products
# •	Sort and Print products based on price ( Price High to Low and Low to High) with all details.
# •	Search product using its code.

class category:
    def __init__(self,name,c_code,no_of_products):
        self.name = name
        self.c_code = c_code
        self.no_of_products = no_of_products
        
    def print_category_details(self):
        print("name of category :", self.name)
        print("code :", self.c_code)
        print("no_of_products :", self.no_of_products)

class product():
    counter=0
    def __init__(self,p_name,p_code,category,price):
        self.p_name = p_name
        self.p_code = p_code
        self.category = category
        self.price = price
        product.counter=product.counter+1
    
    def print_product(self):
        print("Product name: " , self.p_name)
        print("Product code: ", self.p_code)
        print("Category: ", self.category)
        print("Price: ", self.price)


print("Products\n")
p1=product('ashok layland','a01','truck',1200000)        
p2=product('bmw','bm01','car',200000)
p3=product('swift','s01','car',120000)
p4=product('splender','sp01','bike',50000)
p5=product('baleno','b01','car',130000)
p6=product('creta','c01','car',140000)
p7=product('chota hathi','ch01','truck',220000)
p8=product('shine','sp01','bike',90000)
p9=product('g-wagon','g01','car',920000)
p10=product('safari','sf1','car',800000)
p11=product('i10','i01','car',240000)

# print(product.counter)

# product_list=[]

# for i in range(1,product.counter+1):
#     product_list.append("p{0}".format(i))
# print(product_list)
    
product_list=[p1, p2, p3, p4, p5, p6,p7, p8, p9, p10,p11]

for i in product_list:
    i.print_product()
else:
    print()
c_count=0
t_count=0
b_count=0
for i in product_list:
    if i.category == 'car':
        c_count+=1
    elif i.category == 'truck':
        t_count+=1
    elif i.category == 'bike':
        b_count+=1
print("\nCategory\n")
c1=category('car','c001',c_count)
c2=category('truck','t001',t_count)
c3=category('bike','b001',b_count)
cat_list=[c1,c2,c3]
for i in cat_list:
    i.print_category_details()
else:
    print()

def product_search():
    flag=True
    c=0
    find_product=input("enter a code to search for products :")
    for i in product_list:
        if i.p_code == find_product:
            flag=True
            break
        else:
            flag=False
        c=c+1
    if flag==True:
        print("product name :",product_list[c].p_name)
        print("product code :",product_list[c].p_code)
        print("product category :",product_list[c].category)
        print("product price :",product_list[c].price)
    else:
        print("product not found")
product_search()

def price_low_to_high():
    for i in range(0,len(product_list)):
        for j in range(i+1,len(product_list)):
            if product_list[i].price > product_list[j].price:
                temp=product_list[i].price
                product_list[i].price=product_list[j].price
                product_list[j].price=temp
    for i in product_list:
        i.print_product()
        # print(product_list[i].price)

def price_high_to_low():
    for i in range(0,len(product_list)):
        for j in range(i+1,len(product_list)):
            if product_list[i].price < product_list[j].price:
                temp=product_list[i].price
                product_list[i].price=product_list[j].price
                product_list[j].price=temp
    for i in product_list:
        i.print_product()
    else:
        print()
        # print(product_list[i].price)
print("\nlow to high price order\n")
price_low_to_high()
print("\nhigh to low price order\n")   
price_high_to_low()