from flask import Flask, jsonify
from books import books

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
