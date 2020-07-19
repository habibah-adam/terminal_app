import pizza






def add_customer(customer_mobile):
        if customer_mobile in pizza.customers.keys():
            print(f" old customer:\n {pizza.customers[customer_mobile]}")
            serve_customer(customer_mobile)
        else:
            print("you are a new customer!!!")
            name = input("Enter your name: ")
            address = input("Your address: ")
            pizza.customers[customer_mobile] = {}
            pizza.customers[customer_mobile]["name"] = name
            pizza.customers[customer_mobile]["address"] = address
            pizza.customers[customer_mobile]["credit"] = 0

def serve_customer(customer_mobile):
    if customer_mobile in pizza.customers.keys():
        print(f"{pizza.customers[customer_mobile]['name']} put your order now and you have ${pizza.customers[customer_mobile]['credit']} credit.")
        customer_choice(customer_mobile)
    else:
        print("No such customer.")

def show_report():
    sorted_orders = {k: v for k, v in sorted(pizza.orders.items(), key=lambda item: item[1], reverse = True)}
    for i in sorted_orders.keys():
        print(f"{sorted_orders[i]} {i} sold today.")

def customer_choice(customer_mobile):
    
    pizza.customers_order[customer_mobile] = []
    while True:
        choice = input("Customer choice (c/f/o/x): ")
        if choice not in ["c", "f", "o", "x"]:
            print("c = create pizza")
            print("f = show first reference")
            print("o = submit order\n")
            print("x = exit\n")
        if choice == "c":
            pizza.create_pizza(customer_mobile)
            
        if choice == "f":
            pass

        if choice == "o":
            pizza.order_placed(customer_mobile)
            break

        if choice == "x":
            print("Order cancelled.")
            break

