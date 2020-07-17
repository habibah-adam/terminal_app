#!/usr/sbin/python
import datetime
import random


print("\t*************************************")
print("\t****  Welcome to Pizza Express!  ****")
print("\t*************************************")

customers = {
            "433925405": {
                        "name": "Lucy",
                        "address": "34 ocean road, sutherland", 
                        "credit": 6.00,
                        
                         },
            "466660096": {
                        "name": "John",
                        "address": "31 holland cr, casula", 
                        "credit": 7.00,
                        
                         }
            }

dough = {
        "thin": 4.00, 
        "thick" : 5.00
        }

sauce = {
        "tomato": 1.50,
        "barbeque": 1.50
        }

toppings = {
            "olive": 1.00, 
            "spinach": 1.00, 
            "pepperoni": 3.00,
            "mushroom": 2.00, 
            "pineapple": 1.50
            }

customers_order = {}
orders = {}



# def view_customer(customer_mobile):
#     if customer_mobile != "":
#         print(f"{customer_mobile}: {customers[customer_mobile]}")
#     else:
#         for key in customers.keys():
#             print(f"{key}: {customers[key]}")

def create_pizza(customer_mobile):
    pizza = {}
    pizza["price"] = 0
    
    dough_option = input("Choose dough (thin or thick): ")
    pizza["dough"] = dough_option.lower()
    pizza["price"] += dough[dough_option.lower()]
    sauce_option = input("Choose sauce (tomato or barbeque): ")
    pizza["sauce"] = sauce_option.lower()
    pizza["price"] += sauce[sauce_option.lower()]
    pizza["toppings"] = []
    while len(pizza["toppings"]) < 3:
        toppings_option = input("Choose  toppings (olive, spinach, pineapple, mushroom, pepperoni): ")
        if toppings_option.lower() in toppings.keys():
            pizza["toppings"].append(toppings_option.lower())
            pizza["price"] += toppings[toppings_option.lower()]
        else:
            print("No such ingredients.")
    customers_order[customer_mobile].append(pizza)
    try:
        orders[f"{pizza['dough']}-{pizza['sauce']}-{pizza['toppings'][0]}-{pizza['toppings'][1]}-{pizza['toppings'][2]}"] += 1
    except:
        orders[f"{pizza['dough']}-{pizza['sauce']}-{pizza['toppings'][0]}-{pizza['toppings'][1]}-{pizza['toppings'][2]}"] = 1

    print(f"you ordered {pizza['dough']} crust pizza with {pizza['sauce']} sauce and with {pizza['toppings'][0]}, {pizza['toppings'][1]}, {pizza['toppings'][2]}. price: ${pizza['price']}")
    
def delievery_time():
    order_time = datetime.datetime.now()
    delievery_time = order_time + datetime.timedelta(minutes = random.randint(15,25))
    hour = delievery_time.hour
    minute = delievery_time.minute
    return f"{hour}:{minute}"
   
def order_placed(customer_mobile):
    total = 0
    order_list = []
    credit = customers[customer_mobile]['credit']
    print("Order summary:\n")
    for item in customers_order[customer_mobile]:
        total += item["price"]
        
        print(f"{item['dough']} crust pizza with {item['sauce']} sauce and {item['toppings'][0]}, {item['toppings'][1]}, {item['toppings'][2]}. price: ${item['price']}")
    print(f"Sub-Total: ${total} (Available Credit ${credit})")
    print(f"Total: ${total - credit}")
    print(f"Your order will be delievered at {delievery_time()} to address: {customers[customer_mobile]['address']}.")
    customers[customer_mobile]['credit'] += 0.1 * total
    
    


def customer_choice(customer_mobile):
    global customers_order
    customers_order[customer_mobile] = []
    while True:
        choice = input("Customer choice (c/f/o/x): ")
        if choice not in ["c", "f", "o", "x"]:
            print("c = add create customer")
            print("f = show first reference")
            print("o = submit order\n")
        if choice == "c":
            create_pizza(customer_mobile)
            # customers_order[customer_mobile].append(create_pizza())
        if choice == "f":
            pass 
        if choice == "o":
            order_placed(customer_mobile)
            break
        if choice == "x":
            
            break
             

        
def serve_customer(customer_mobile):
    if customer_mobile in customers.keys():
        print(f"{customers[customer_mobile]['name']} put your order now and you have ${customers[customer_mobile]['credit']} credit.")
        customer_choice(customer_mobile)
    else:
        print("No such customer.")

def show_report():
    sorted_orders = {k: v for k, v in sorted(orders.items(), key=lambda item: item[1])}
    print(sorted_orders)
    
    
           
        

def add_customer(customer_mobile):
        if customer_mobile in customers.keys():
            print(f" old customer:\n {customers[customer_mobile]}")
            serve_customer(customer_mobile)
        else:
            print("you are a new customer!!!")
            name = input("Enter your name: ")
            address = input("Your address: ")
            customers[customer_mobile] = {}
            customers[customer_mobile]["name"] = name
            customers[customer_mobile]["address"] = address
            customers[customer_mobile]["credit"] = 0


while True:             
    user_input = input("Choice (a/s/r/x): ")
    if user_input not in ["a", "s", "r", "x"]:
        print("a = add customer")
        
        print("s = serve customer")
        print("r = show report")
        print("x = exit\n")
    if user_input == "a":
        customer_mobile = input("Please enter a mobile number: ")
        add_customer(customer_mobile)
    
    if user_input == "s":
        customer_mobile = input("Please enter a mobile number: ")
        serve_customer(customer_mobile)
    if user_input == "r":
        show_report()
        
    if user_input == "x":
        print("Bye!")
        break
        






        
