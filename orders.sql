CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    drink VARCHAR(20),
    customer VARCHAR(30),
    size CHAR(6),
    quantity INTEGER 
);
