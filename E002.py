# Exercise: E002
# •	Create a new class named "Customer" with below members. "name","email","phone",
# "street","city","state","country","company","type".
# •	"type" must be from "company,contact,billing,shipping".
# •	"Company" must be a Customer object which is the parent object.
# •	Apply Multiple possible validation for phone number and email
# •	Does not allowed number in name,city,state and country


# •	Create a new class named "Order" with members "number","date", "company", "billing", "shipping", "total_amount","order_lines".
# •	"company", "billing", "shipping" are objects of Customer.
# •	"date" must be today or the future. Does not allow past date.
# •	"total_amount" auto calculated based on different products inside order.
# •	"order_lines" is list of objects of "OrderLine"


# •	create a new class named "OrderLine" with members "order", "product", "quantity", "price", "subtotal".
# •	"order" is the object of Order.
# •	"subtotal" is auto calculated based on quantity and price.


# •	Display Order and Customer Information
# •	Sort orders based on "date".
# •	User can filter the current month orders
# •	Search Orders from its number.
# •	List/Display all orders of a specific product. 
import re,sys,datetime
class customer:
    def __init__(self,name,email,phone,street,city,state,country,company,type):
        
        if re.match(r"^[a-zA-Z]+$", name):
           self.name = name    
        else:
            print("Entry is not valid!",name)
        if re.match(r"^[a-zA-Z]+$", city):
           self.city = city    
        else:
            print("Entry is not valid!",city)
        if re.match(r"^[a-zA-Z]+$", state):
           self.state = state    
        else:
            print("Entry is not valid!",state)
        if re.match(r"^[a-zA-Z]+$", country):
           self.country = country    
        else:
            print("Entry is not valid!",country)
            
        if re.match(r"(0|9)?[6-9]\d{9}", phone):
           self.phone = int(phone)    
        else:
            print("Entry is not valid!",phone)
            sys.exit()
        
        if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',email):
            self.email = email 
        else:
            print("Entry is not valid!",email)
            
        self.street = street
        
        self.company = company
        if type in ["company","contact","billing","shipping"]:
            self.type = type
        else:
            print("Entry is not valid!",type)
    
    def display(self):
        print(f"name : {self.name} , phone : {self.phone} ,email : {self.email},street :{self.street},state : {self.state},country :{self.country},company :{self.company},type :{self.type}")


class Order:
    def __init__(self,number,date,company,billing,shipping,order_lines):
        self.number = number
        if date > datetime.date.today():
            self.date = date
        else:
            print("Date must be in future or today")
        self.company=company
        self.billing=billing
        self.shipping=shipping
        self.order_lines=order_lines
        self.total_amount=self.cal_total_amount()
    
    def cal_total_amount(self):
        total_amount=0
        for i in self.order_lines:
            total_amount+=i.subtotal
            # print(i.subtotal)
        return total_amount
        
    def show(self):
        print(f"Order Number : {self.number} \nDate : {self.date} \ncompany name : {self.company.company}\
            \nshipping address : {self.shipping.street},{self.shipping.city},{self.shipping.state},{self.shipping.country}\
                \nBilling address : {self.billing.street},{self.billing.city},{self.billing.state},{self.billing.country} \ntotal amount:{self.total_amount}")
    @staticmethod
    def sort_by_date(order_list):
        print("\n===============displaying order (order by date)===============")
        a=len(order_list)
        for i in range(0,a):
            for j in range(i+1,a):
                if order_list[i].date > order_list[j].date:
                    temp=order_list[i]
                    order_list[i]=order_list[j]
                    order_list[j]=temp
        for i in order_list:
            print()
            i.show()
    
    @staticmethod
    def filter_current_mionth_order(order_list):
        print("\n===============displaying order of current month===============")
        
        for i in order_list:
            if i.date.month== datetime.date.today().month:
                print()
                i.show()
    @staticmethod
    def display_order_by_products(order_lines):
        print("\n===============displaying order by specific product===============")
        for i in order_lines:
            print("==============",i.product,"==============")
            for j in i.order:
                print()
                print(f"order number :{j.number}\ndate :{j.date}\nquntity :{i.quantity}\nprice :{i.price}")
    @staticmethod
    def search_product(order_list):
        no=input("please enter your order number :")
        for i in order_list:
            for j in i.order_lines:
                if i.number == no:
                    print(f"order number :{i.number}\ndate :{i.date}\nquntity :{j.quantity}\nprice :{j.price}")

class OrderLine:
    def __init__(self,order,product,quantity,price):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.price * self.quantity
        


company=customer('None','company@gmail.com','9264585842','saiyaji','rajkot','Gujrat','India','Main company','company')
billing=customer('ankur','akakrecha@gmail.com','8849799712','manekpara','amreli','Gujrat','India',company,'shipping')
shipping=customer('ritul','ritul@gmail.com','9925265356','jyotinagar','rajkot','Gujrat','India',company,'billing')

company_list=[company,billing,shipping]

# product
ol1=OrderLine(None,'product1',2,500)
ol2=OrderLine(None,'product2',5,400)
ol3=OrderLine(None,'product3',1,400)
ol4=OrderLine(None,'product4',2,350)
ol5=OrderLine(None,'product5',4,200)

order_lines=[ol1,ol2,ol3,ol4,ol5]


o1=Order('O01',datetime.date(2024,1,24),company,billing,shipping,[ol1,ol2])
o2=Order('O02',datetime.date(2024,3,21),company,billing,shipping,[ol2])
o3=Order('O03',datetime.date(2024,1,19),company,billing,shipping,[ol3])
o4=Order('O04',datetime.date(2024,6,12),company,billing,shipping,[ol4])
o5=Order('O05',datetime.date(2024,8,28),company,billing,shipping,[ol5])

order_list=[o1,o2,o3,o4,o5]
ol1.order=[o1]
ol2.order=[o1,o2]
ol3.order=[o3]
ol4.order=[o4]
ol5.order=[o5]

# display order and customer detail
for i in order_list:
    print()
    i.show()
#sortin order by date
Order.sort_by_date(order_list)
#print order of current month
Order.filter_current_mionth_order(order_list)

#print order by specific order
Order.display_order_by_products(order_lines)
#serchin order by order number
Order.search_product(order_list)
