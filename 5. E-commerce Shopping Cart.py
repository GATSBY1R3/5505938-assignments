from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cart
                 (id INTEGER PRIMARY KEY, product_name TEXT, quantity INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_name = request.json['product_name']
    quantity = request.json['quantity']
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute("INSERT INTO cart (product_name, quantity) VALUES (?, ?)", (product_name, quantity))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product added to cart successfully'})

@app.route('/view_cart', methods=['GET'])
def view_cart():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cart")
    items = c.fetchall()
    conn.close()
    return jsonify({'cart': items})

@app.route('/clear_cart', methods=['GET'])
def clear_cart():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute("DELETE FROM cart")
    conn.commit()
    conn.close()
    return jsonify({'message': 'Cart cleared successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
