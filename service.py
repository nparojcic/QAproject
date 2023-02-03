from db import *

def read_by_id(id):
    order_data = db.query(id)
    order = order(order_data) 
    
def create_order(drink_name, customer, size, quantity):
    # order = Order(drink_name, customer, size, quantity)
    customer = input("Customer name: ")
    drink_name = input("Drink name: ")
    size = input("Size: ")
    order_query = f"INSERT INTO orders (drink, customer, size, quantity) VALUES ('{drink}', '{customer}', {size}, '{quantity}');"
    cursor.execute(order_query)
    return True

def readAllOrders():
    query = "SELECT * FROM orders"
    return selectQuery(query)

def deleteOrder():
    id = input("What is the ID of the order you want to delete from the system?: ")
    query = f"DELETE FROM orders where order_id = {id}"
    return dataQuery(query)

def deleteAllOrders():
    while True:
        choice = input("Delete all orders? (yes / no")
        if choice.lower() == "yes":
            doubleCheck = input("Are you sure? ")
            if doubleCheck.lower() == "yes":
                query = f"DELETE * FROM orders"
                return dataQuery(query)
            elif doubleCheck.lower() == "no":
                return False
        elif choice.lower() == "no":
            return False
        else: 
            print("Invalid choice (yes or no): ")

    

def updateOrder():
    id = input("What is the ID of the order? ")
    title = input("What would you like to update it to? ")
    query = f"UPDATE orders SET orderId = '{order_id}' WHERE order_id = {id}"
    return dataQuery(query)


