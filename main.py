print("\t*************************************")
print("\t****  Welcome to Pizza Express!  ****")
print("\t*************************************")

customers = {"433925405": {"name": "Lucy", "address": "34 ocean road, vic"},
              "466660096": {"name": "john", "address": "3 holland st, nsw"}}
daugh = {"thin": "$4.00", "thick" = "$5.00"}
sause = {"tomato": "$1.50", "barbeque": "$1.50"}
toppings = {"olives": "$1.00", "spinach": "$1.00", "pepperoni": "$3.00", "mushroom": "$2.00", "pineapple": "$1.50"}
customers_list = []
def add_customer(customer_mobile):
    
    
        if customer_mobile in customers.keys():
            print(f" old customer:\n {customers[customer_mobile]}")
        else:
            print("you are a new customer!!!")
            name = input("Enter your name: ")
            address = input("Your address: ")
            customers[customer_mobile] = {}
            customers[customer_mobile]["name"] = name
            customers[customer_mobile]["address"] = address

def view_customer(customer_mobile):
    if customer_mobile != "":
        print(f"{customer_mobile}: {customers[customer_mobile]}")
    else:
        for key in customers.keys():
            print(f"{key}: {customers[key]}")
def create_pizza():
    pizza = {}
    dough_option = input("Choose dough (thin or thick): ")
    pizza["dough"] = dough_option
    
    sauce_option = input("Choose sauce (tomato or barbeque): ")
    pizza["sauce"] = sauce_option
    toppings_option = input("Choose toppings (olive, spinach, pineapple, mushroom, pepperoni): ")



def customer_choice():
    order_list = []
    while True:
        customer_choice = input("Customer choice (c/f/o): ")
        if customer_choice == "c":
            create_pizza()
        if customer_choice == "f":
            pass favourite_pizza
        if customer_choice == "o":
            pass order_placed()

        
def serve_customer(customer_mobile):
    if customer_mobile in customers.keys():
        print(f"{customers[customer_mobile]['name']} put your order now.")
        customer_choice()
    else:
        print("No such customer.")



            
while True:             
    user_input = input("Choice (a/v/s/r/x): ")
    if user_input == "a":
        customer_mobile = input("Please enter a mobile number: ")
        add_customer(customer_mobile)
    if user_input == "v":
        customer_mobile = input("Please enter a mobile number: ")
        view_customer(customer_mobile)
    if user_input == "s":
        customer_mobile = input("Please enter a mobile number: ")
        serve_customer(customer_mobile)
        



        
