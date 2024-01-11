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
    def __init__(self,p_name,p_code,category,price):
        self.p_name = p_name
        self.p_code = p_code
        self.category = category
        self.price = price
        
    def print_product(self):
        print("Product name: " , self.p_name)
        print("Product code: ", self.p_code)
        print("Category: ", self.category)
        print("Price: ", self.price)
    
    @classmethod    
    def product_search(self,lst):
        flag=True
        c=0
        find_product=input("enter a code to search for products :")
        for i in lst:
            if i.p_code == find_product:
                flag=True
                break
            else:
                flag=False
            c=c+1
        if flag==True:
            print("product name :",lst[c].p_name)
            print("product code :",lst[c].p_code)
            print("product category :",lst[c].category)
            print("product price :",lst[c].price)
        else:
            print("product not found")
        
    @classmethod
    def price_low_to_high(self,lst):
        for i in range(0,len(lst)):
            for j in range(i+1,len(lst)):
                if lst[i].price > lst[j].price:
                    temp=lst[i].price
                    lst[i].price=lst[j].price
                    lst[j].price=temp
        for i in lst:
            i.print_product()
            # print(lst[i].price)
    
    @classmethod
    def price_high_to_low(self,lst):
        for i in range(0,len(lst)):
            for j in range(i+1,len(lst)):
                if lst[i].price < lst[j].price:
                    temp=lst[i].price
                    lst[i].price=lst[j].price
                    lst[j].price=temp
        for i in lst:
            i.print_product()
        else:
            print()
            # print(lst[i].price)


# create object of category and print details
print("\n==============Category==============\n")
c_count=0
t_count=0
b_count=0
c1=category('car','c001',c_count)
c2=category('truck','t001',t_count)
c3=category('bike','b001',b_count)
cat_list=[c1,c2,c3]
for i in cat_list:
    i.print_category_details()
else:
    print()

# create objects of products     
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
    
product_list=[p1, p2, p3, p4, p5, p6,p7, p8, p9, p10,p11]

# count the product of perticuler category
for i in product_list:
    if i.category == 'car':
        c_count+=1
    elif i.category == 'truck':
        t_count+=1
    elif i.category == 'bike':
        b_count+=1

#print products details
   
for i in product_list:
    i.print_product()
else:
    print()
    
# search product thrue their product code
product.product_search(product_list)

# low to high order base of price
print("========== low to high price =============")
product.price_low_to_high(product_list)

# high to low order base of price
print("==========  high price to low =============")
product.price_high_to_low(product_list)