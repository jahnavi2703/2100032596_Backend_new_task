# routes.py

from flask import render_template
from app import app
from .models import Customer, Product, Order, OrderItem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers')
def customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/orders')
def orders():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

@app.route('/order_items')
def order_items():
    order_items = OrderItem.query.all()
    return render_template('order_items.html', order_items=order_items)

