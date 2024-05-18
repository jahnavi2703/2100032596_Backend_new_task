from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

# Sample data for products, customers, orders, and order items
products = [
    {"ProductID": 1, "ProductName": "Laptop", "Price": 1000},
    {"ProductID": 2, "ProductName": "Smartphone", "Price": 600},
    {"ProductID": 3, "ProductName": "Headphones", "Price": 100}
]

customers = [
    {"CustomerID": 1, "FirstName": "John", "LastName": "Doe", "Email": "john.doe@example.com", "DateOfBirth": "1985-01-15"},
    {"CustomerID": 2, "FirstName": "Jane", "LastName": "Smith", "Email": "jane.smith@example.com", "DateOfBirth": "1990-06-20"}
]

orders = [
    {"OrderID": 1, "CustomerID": 1, "OrderDate": "2023-01-10"},
    {"OrderID": 2, "CustomerID": 2, "OrderDate": "2023-01-12"}
]

order_items = [
    {"OrderItemID": 1, "OrderID": 1, "ProductID": 1, "Quantity": 1},
    {"OrderItemID": 2, "OrderID": 1, "ProductID": 3, "Quantity": 2},
    {"OrderItemID": 3, "OrderID": 2, "ProductID": 2, "Quantity": 1},
    {"OrderItemID": 4, "OrderID": 2, "ProductID": 3, "Quantity": 1}
]

# Routes to serve data for products, customers, orders, and order items
@app.route('/')
@app.route('/index')
def index():
    welcome_message = "Welcome to my project!"
    return render_template('index.html', welcome_message=welcome_message,
                           products=products, customers=customers,
                           orders=orders, order_items=order_items)

@app.route('/products')
def show_products():
    return render_template('products.html', products=products)

@app.route('/customers')
def show_customers():
    return render_template('customers.html', customers=customers)

@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

@app.route('/order_items')
def show_order_items():
    return render_template('order_items.html', order_items=order_items)

@app.route('/redirect_to_index')
def redirect_to_index():
    return redirect(url_for('index'))

@app.route('/query')
def query():
    # Assuming you have retrieved data for each query

    # Query 1: List all customers
    query1_data = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'},
        {'id': 3, 'name': 'Alice Johnson', 'email': 'alice@example.com'}
    ]

    # Query 2: Find all orders placed in January 2023
    query2_data = [
        {'id': 1, 'customer_id': 1, 'order_date': '2023-01-01'},
        {'id': 2, 'customer_id': 2, 'order_date': '2023-01-05'},
        {'id': 3, 'customer_id': 1, 'order_date': '2023-01-10'}
    ]

    # Query 3: Get the details of each order, including the customer name and email
    query3_data = [
        {'id': 1, 'customer_name': 'John Doe', 'customer_email': 'john@example.com', 'order_date': '2023-01-01'},
        {'id': 2, 'customer_name': 'Jane Smith', 'customer_email': 'jane@example.com', 'order_date': '2023-01-05'},
        {'id': 3, 'customer_name': 'Alice Johnson', 'customer_email': 'alice@example.com', 'order_date': '2023-01-10'}
    ]

    # Query 4: List the products purchased in a specific order
    query4_data = [
        {'order_id': 1, 'product_id': 101, 'product_name': 'Product A', 'quantity': 2},
        {'order_id': 1, 'product_id': 102, 'product_name': 'Product B', 'quantity': 1},
        {'order_id': 2, 'product_id': 103, 'product_name': 'Product C', 'quantity': 3}
    ]

    # Query 5: Calculate the total amount spent by each customer
    query5_data = [
        {'id': 1, 'total_amount': 500},
        {'id': 2, 'total_amount': 750},
        {'id': 3, 'total_amount': 300}
    ]

    # Query 6: Find the most popular product
    query6_data = "Product X"

    # Query 7: Get the total number of orders and the total sales amount for each month in 2023
    query7_data = [
        {'month': 'January', 'total_orders': 20, 'total_sales': 1500},
        {'month': 'February', 'total_orders': 15, 'total_sales': 1200},
        {'month': 'March', 'total_orders': 25, 'total_sales': 1800}
    ]

    # Query 8: Find customers who have spent more than $1000
    query8_data = [
        {'id': 2, 'total_amount': 1200},
        {'id': 5, 'total_amount': 1100}
    ]

    return render_template('query.html', query1_data=query1_data, query2_data=query2_data, query3_data=query3_data,
                           query4_data=query4_data, query5_data=query5_data, query6_data=query6_data,
                           query7_data=query7_data, query8_data=query8_data)

if __name__ == '__main__':
    app.run(debug=True)