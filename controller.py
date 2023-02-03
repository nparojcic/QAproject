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
            insertMovie()
        elif selection == 2:
            updateMovieTitleId()
        elif selection == 3:
            deleteMovie()
        elif selection == 4:
            deleteTicketId()
        else:
            print("Incorrect choice.. try again: ")
        
        choice = input("Do you want to query more data? Y / N")
        if choice.upper() == 'N':
            print("Program Terminated")
            programRunning = False
    



def deleteOrderId():
    id = input("What is the ID of the order you want to delete from the system?: ")
    query = f"DELETE FROM orders where order_id = {id}"
    return dataQuery(query)

def deleteOrder():
    id = input("What is the ID of the movie you want to delete from the system?: ")
    query = f"DELETE FROM movies where film_id = {id}"
    return dataQuery(query)

def updateMoviTitleId():
    id = input("What is the ID of the film? ")
    title = input("What would you like to update it to? ")
    query = f"UPDATE movies SET movie_title = '{title}' WHERE film_id = {id}"
    return dataQuery(query)

def insertMovie():
    movie_title = input("Please enter movie title: ")
    genre = input("Please enter genre: ")
    third_dimension_film = input("Is it 3D? ")
    movie_query = f"INSERT INTO movies (movie_title, genre, third_dimension_film) VALUES ('{movie_title}', '{genre}', {third_dimension_film});"
    cursor.execute(movie_query)
    return True

def insertTicket(film_id):
    ticket_query = f"INSERT INTO tickets (film_id, number_tickets, ticket_name) VALUES ({film_id}, 5, 'Wesley Snipes');"
    cursor.execute(ticket_query)
    return True


def runApplication():
    print("""Welcome to Showcase Cinema, what would you like to do? \n

1. Add a movie
2. Update movie title
3. Delete movie
4. Delete ticket
5. Read movie by ID
6. Read ticket by ID
7. Update movie ID\n
""")

    






print(service.getAll())