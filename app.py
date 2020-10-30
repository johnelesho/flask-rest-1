from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# db.create_all()
# Init ma
ma = Marshmallow(app)

# Product Class/Model

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
          self.name = name
          self.description = description
          self.price = price
          self.qty = qty


class ProductSchema(ma.Schema):
    fields = ('id', 'name', 'description', 'price', 'qty')
    

# Init Schemas
product_schema = ProductSchema()
products_schema = ProductSchema()


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World'})

@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json["description"]
    price = request.json["price"]
    qty = request.json["qty"]

    new_product = Product(name, description, price, qty)

    # db.session.add(new_product)
    # db.session.commit()
    
    return product_schema.jsonify(new_product)

# Run server

if  __name__ == "__main__":
    app.run(debug=True)

