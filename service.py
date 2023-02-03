# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data


def read_by_id(id):
    order_data = db.query(id)
    order = order(order_data) 
    
def create_order(drink_name, customer, size, quantity):
    order_id = 0
    order = Order(drink_name, customer, size, quantity)
    order_id = 
    genre = input("Please enter genre: ")
    third_dimension_film = input("Is it 3D? ")
    movie_query = f"INSERT INTO orders (drink_name, customer, size, quantity) VALUES ('{drink_name}', '{customer}', {size}, '{quantity}');"
    cursor.execute(movie_query)
    order_id += 1
    return True
    

def deleteOrderId():
    id = input("What is the ID of the order you want to delete from the system?: ")
    query = f"DELETE FROM orders where order_id = {id}"
    return dataQuery(query)

def deleteOrder():
    id = input("What is the ID of the movie you want to delete from the system?: ")
    query = f"DELETE FROM movies where film_id = {id}"
    return dataQuery(query)

def updateOrder():
    id = input("What is the ID of the order? ")
    title = input("What would you like to update it to? ")
    query = f"UPDATE orders SET orderId = '{title}' WHERE film_id = {id}"
    return dataQuery(query)

def insertMovie():
    

def insertTicket(film_id):
    ticket_query = f"INSERT INTO tickets (film_id, number_tickets, ticket_name) VALUES ({film_id}, 5, 'Wesley Snipes');"
    cursor.execute(ticket_query)
    return True

