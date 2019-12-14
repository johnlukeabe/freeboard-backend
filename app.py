# Common Classes
import json
from flask import Flask

# Private Classes

app = Flask(__name__)

@app.route('/')
def hello():
    return "main"

@app.route('/index')
def index():
    return "index"

if __name__ == '__main__':
    # Load configuration
    with open('config.json', 'r') as f:
        data = f.read()
    config = json.loads(data)

    app.run(host=config['host'], port=config['port'])
