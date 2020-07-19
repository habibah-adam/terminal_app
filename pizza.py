import datetime
import random


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


def create_pizza(customer_mobile):
    pizza = {}
    pizza["price"] = 0
    while True:
        dough_option = input("Choose dough (thin or thick): ")
        if dough_option.lower() in ("thin", "thick"):
            break
    pizza["dough"] = dough_option.lower()
    pizza["price"] += dough[dough_option.lower()]
    while True:
        sauce_option = input("Choose sauce (tomato or barbeque): ")
        if sauce_option.lower() in ("tomato", "barbeque"):
            break
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
    print(f"Total: ${(total - credit):.2f}")
    print(f"Your order will be delievered at {delievery_time()} to address: {customers[customer_mobile]['address']}.")
    customers[customer_mobile]['credit'] = 0.1 * total
    print(f"You earned ${customers[customer_mobile]['credit']:.2f} credit!")
