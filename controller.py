# The controller acts as the API for the app, in this case it will exist as a terminal based app
# using inputs and if statements to specify what the app should do

# It will run commands from the service file, which in turn uses the DB file to 
# query and create data and will return the data back to the user

from service import *

def menu():
    print(
        """
        Welcome to the QA Cafe, what would you like to do? 
        1. Create an order
        2. Read an order
        3. Read all orders
        4. Update an order
        5. Delete an order
        6. Delete all orders
        """
    )

    programRunning = True

    while programRunning:
        selection = int(input("Enter choice: "))
        if selection == 1:
            create_order(drink_name, customer, size, quantity)
        elif selection == 2:
            read_by_id(id)
        elif selection == 3:
            readAllOrders()
        elif selection == 4:
            updateOrder()
        elif selection == 5:
            deleteOrder()
        elif selection == 6:
            deleteAllOrders()
        else:
            print("Incorrect choice.. try again: ")
        
        choice = input("Do you want to query more data? Y / N")
        if choice.upper() == 'N':
            print("Program Terminated")
            programRunning = False

menu()