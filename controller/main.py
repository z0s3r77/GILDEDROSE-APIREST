from flask import Flask
from flask import make_response
app = Flask(__name__)

@app.route('/')
def index():
    response = make_response("<h1>Flask is running</h1>")
    return  response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
