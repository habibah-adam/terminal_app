print("\t*************************************")
print("\t****  Welcome to Pizza Express!  ****")
print("\t*************************************")

customers = {"433925405": ["Lucy", "34 ocean road, vic"],
              "466660096": ["john", "3 holland st, nsw"]}
dough = {"thin": 4.00, "thick" : 5.00}
sauce = {"tomato": 1.50, "barbeque": 1.50}
toppings = {"olive": 1.00, "spinach": 1.00, "pepperoni": 3.00, "mushroom": 2.00, "pineapple": 1.50}
customers_list = []
def add_customer(customer_mobile):
    
    
        if customer_mobile in customers.keys():
            print(f" old customer:\n {customers[customer_mobile]}")
        else:
            print("you are a new customer!!!")
            name = input("Enter your name: ")
            address = input("Your address: ")
            customers[customer_mobile] = []
            customers[customer_mobile][0] = name
            customers[customer_mobile][1] = address

def view_customer(customer_mobile):
    if customer_mobile != "":
        print(f"{customer_mobile}: {customers[customer_mobile]}")
    else:
        for key in customers.keys():
            print(f"{key}: {customers[key]}")
def create_pizza():
    pizza = {}
    pizza["total"] = 0
    dough_option = input("Choose dough (thin or thick): ")
    pizza["dough"] = dough_option.lower()
    pizza["total"] += dough[dough_option.lower()]
    sauce_option = input("Choose sauce (tomato or barbeque): ")
    pizza["sauce"] = sauce_option.lower()
    pizza["total"] += sauce[sauce_option.lower()]
    pizza["toppings"] = []
    while len(pizza["toppings"]) < 3:
        toppings_option = input("Choose  toppings (olive, spinach, pineapple, mushroom, pepperoni): ")
        if toppings_option.lower() in toppings.keys():
            pizza["toppings"].append(toppings_option.lower())
            pizza["total"] += toppings[toppings_option.lower()]
        else:
            print("No such ingredients.")
        
    print(f"you ordered {pizza['dough']} crust pizza with {pizza['sauce']} sauce and with {pizza['toppings'][0]}, {pizza['toppings'][1]}, {pizza['toppings'][2]}. total: ${pizza['total']}")
    



def customer_choice():
    order_list = []
    while True:
        customer_choice = input("Customer choice (c/f/o): ")
        if customer_choice not in ["c", "f", "o"]:
            print("c = add create customer")
            print("f = show first reference")
            print("o = submit order\n")
        if customer_choice == "c":
            create_pizza()
        if customer_choice == "f":
            pass 
        if customer_choice == "o":
            pass 

        
def serve_customer(customer_mobile):
    if customer_mobile in customers.keys():
        print(f"{customers[customer_mobile][0]} put your order now.")
        customer_choice()
    else:
        print("No such customer.")



            
while True:             
    user_input = input("Choice (a/v/s/r/x): ")
    if user_input not in ["a", "v", "s", "r", "x"]:
        print("a = add customer")
        print("v = view customer")
        print("s = serve customer")
        print("r = show report")
        print("x = exit\n")
    if user_input == "a":
        customer_mobile = input("Please enter a mobile number: ")
        add_customer(customer_mobile)
    if user_input == "v":
        customer_mobile = input("Please enter a mobile number: ")
        view_customer(customer_mobile)
    if user_input == "s":
        customer_mobile = input("Please enter a mobile number: ")
        serve_customer(customer_mobile)
        



        
