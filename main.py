import datetime

print("\t*************************************")
print("\t****  Welcome to Pizza Express!  ****")
print("\t*************************************")

customers = {"433925405": ["Lucy", "34 ocean road, sutherland"],
              "466660096": ["john", "3 holland st, casula"]}
dough = {"thin": 4.00, "thick" : 5.00}
sauce = {"tomato": 1.50, "barbeque": 1.50}
toppings = {"olive": 1.00, "spinach": 1.00, "pepperoni": 3.00, "mushroom": 2.00, "pineapple": 1.50}
customers_order = {}
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
def create_pizza(customer_mobile):
    pizza = {}
    pizza["price"] = 0
    pizza["order"] = {}
    dough_option = input("Choose dough (thin or thick): ")
    pizza["order"]["dough"] = dough_option.lower()
    pizza["price"] += dough[dough_option.lower()]
    sauce_option = input("Choose sauce (tomato or barbeque): ")
    pizza["order"]["sauce"] = sauce_option.lower()
    pizza["price"] += sauce[sauce_option.lower()]
    pizza["order"]["toppings"] = []
    while len(pizza["order"]["toppings"]) < 3:
        toppings_option = input("Choose  toppings (olive, spinach, pineapple, mushroom, pepperoni): ")
        if toppings_option.lower() in toppings.keys():
            pizza["order"]["toppings"].append(toppings_option.lower())
            pizza["price"] += toppings[toppings_option.lower()]
        else:
            print("No such ingredients.")
    customers_order[customer_mobile].append(pizza)   
    print(f"you ordered {pizza['order']['dough']} crust pizza with {pizza['order']['sauce']} sauce and with {pizza['order']['toppings'][0]}, {pizza['order']['toppings'][1]}, {pizza['order']['toppings'][2]}. price: ${pizza['price']}")
    
def delievery_time(wait_period):
    order_time = datetime.datetime.now()
    delievery_time = order_time + datetime.timedelta(minutes = wait_period)
    hour = delievery_time.hour
    minute = delievery_time.minute
    return f"{hour}:{minute}"
   
def order_placed(customer_mobile):
    total = 0
    order_list = []
    print("Order summary:\n")
    for item in customers_order[customer_mobile]:
        total += item["price"]
        print(f"{item['order']['dough']} crust with {item['order']['sauce']} sauce and {item['order']['toppings'][0]}, {item['order']['toppings'][1]}, {item['order']['toppings'][2]}. price: ${item['price']}")
    print(f"Total: ${total}")
    print(f"Your order will be delievered at {delievery_time(20)} to address: {customers[customer_mobile][1]}.")


def customer_choice(customer_choice):
    customers_order[customer_mobile] = []
    while True:
        customer_choice = input("Customer choice (c/f/o): ")
        if customer_choice not in ["c", "f", "o"]:
            print("c = add create customer")
            print("f = show first reference")
            print("o = submit order\n")
        if customer_choice == "c":
            create_pizza(customer_mobile)
            # customers_order[customer_mobile].append(create_pizza())
        if customer_choice == "f":
            pass 
        if customer_choice == "o":
            order_placed(customer_mobile)
             

        
def serve_customer(customer_mobile):
    if customer_mobile in customers.keys():
        print(f"{customers[customer_mobile][0]} put your order now.")
        customer_choice(customer_choice)
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
        






        
