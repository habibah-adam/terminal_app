print("\t*************************************")
print("\t****  Welcome to Pizza Express!  ****")
print("\t*************************************")

customers = {"433925405": {"name": "Lucy", "address": "34 ocean road, vic"},
              "466660096": {"name": "john", "address": "3 holland st, nsw"}}
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
def view_customer(customer_mobile = "None"):
    if customer_mobile in customers.keys():
        print(f"{customer_mobile}: {customers[customer_mobile]}")
    else:
        for key in customers.keys():

            print(f"{key}: {customers[key]}")



            
while True:             
    user_input = input("Choice (a/v/s/r/x): ")
    if user_input == "a":
        customer_mobile = input("Please enter a mobile number: ")
        add_customer(customer_mobile)
    elif user_input == "v":
        customer_mobile = input("Please enter a mobile number: ")
        view_customer()
print(customers)


        
