from http.server import BaseHTTPRequestHandler, HTTPServer
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"message": "Hello, World!"}
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data)
            response = {"received": data}
            self.send_response(200)
        except json.JSONDecodeError:
            response = {"error": "Bad Request", "message": "Invalid JSON"}
            self.send_response(400)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        try:
            data = json.loads(put_data)
            response = {"updated": data}
            self.send_response(200)
        except json.JSONDecodeError:
            response = {"error": "Bad Request", "message": "Invalid JSON"}
            self.send_response(400)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_DELETE(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"message": "Resource deleted"}
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, jsonify, request

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"message": "Hello, World!"}
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        response = {"received": data}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
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

@app.route('/api', methods=['PUT'])
def put_data():
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Invalid JSON"}), 400
        response = {"updated": data}
        return jsonify(response)

@app.route('/api', methods=['DELETE'])
def delete_data():
        return jsonify({"message": "Resource deleted"}), 200

@app.errorhandler(400)
def bad_request(error):
        return jsonify({"error": "Bad Request", "message": "Invalid JSON"}), 400

    if __name__ == '__main__':
        app.run(debug=True)