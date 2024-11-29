from flask import Flask, jsonify, request
app = Flask(__name__)

products = []

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({"error": "Bad Request", "message": "Invalid JSON"}), 400
    product = {
        "name": data['name'],
        "description": data['description'],
        "price": data['price']
    }
    products.append(product)
    return jsonify(product), 201

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id < 0 or product_id >= len(products):
        return jsonify({"error": "Not Found", "message": "Product not found"}), 404
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({"error": "Bad Request", "message": "Invalid JSON"}), 400
    products[product_id] = {
        "name": data['name'],
        "description": data['description'],
        "price": data['price']
    }
    return jsonify(products[product_id])

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id < 0 or product_id >= len(products):
        return jsonify({"error": "Not Found", "message": "Product not found"}), 404
    products.pop(product_id)
    return jsonify({"message": "Product deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    data = {"message": "Hello, World!"}
    return jsonify(data)

@app.route('/api', methods=['POST'])
def post_data():
    data = request.get_json()
    response = {"received": data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
    # Add error handling for invalid JSON in POST request
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request", "message": "Invalid JSON"}), 400

    # Add a route to handle PUT requests
    @app.route('/api', methods=['PUT'])
    def put_data():
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Invalid JSON"}), 400
        response = {"updated": data}
        return jsonify(response)

    # Add a route to handle DELETE requests
    @app.route('/api', methods=['DELETE'])
    def delete_data():
        return jsonify({"message": "Resource deleted"}), 200
    
    
