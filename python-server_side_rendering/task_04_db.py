from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source', 'json')
    product_id = request.args.get('id', type=int)
    
    products_list = []
    
    if source == 'json':
        with open('products.json', 'r') as file:
            products_list = json.load(file)
    elif source == 'csv':
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            products_list = list(reader)
    elif source == 'sql':
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        
        for row in cursor.fetchall():
            products_list.append({
                'id': row[0],
                'name': row[1],
                'category': row[2], 
                'price': row[3]
            })
        conn.close()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        products_list = [p for p in products_list if p.get('id') == product_id]
        if not products_list:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
