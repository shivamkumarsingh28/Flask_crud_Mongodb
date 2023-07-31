from flask import Flask, request
from pymongo import MongoClient

# flask app object
app = Flask(__name__)

# root route
@app.route('/')
def saeeam():
    return 'Hello, SaeeAM'

# set up mongodb connection
client = MongoClient('mongodb://localhost:27017')
db = client['demo']
collection = db['data']


@app.route('/add_data', methods=['POST'])
def add_data():
    # Get data from request
    data = request.json
  
    # Insert data into MongoDB
    collection.insert_one(data)
  
    return 'Data added to MongoDB'

if __name__ == "__main__":
    app.run(debug=True)
