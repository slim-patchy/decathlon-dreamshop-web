#!/usr/bin/env python3
import base64
import json
import logging

from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

import product_controller

# Initialise SQLAlchemy to be used in the models
db = SQLAlchemy()

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


# Backend code
@app.route('/products', methods=["GET"])
def get_products():
    products = product_controller.get_products()
    products_list = []
    for element in products:
        element = list(element)
        image = base64.b64encode(element[7])
        decoded_image = image.decode()
        element.pop(7)
        element.insert(7, decoded_image)
        products_list.append(element)
    return jsonify(products_list)


@app.route("/product", methods=["POST"])
def insert_product():
    product_details = request.get_json()
    name = product_details["name"]
    short_description = product_details["short_description"]
    brand = product_details["brand"]
    size = product_details["size"]
    color = product_details["color"]
    suggested_retail_price = product_details["suggested_retail_price"]
    image = product_details["image"]
    image = base64.b64encode(image)
    image = image.decode()
    image = json.dumps(image)
    result = product_controller.insert_product(name,
                                               short_description,
                                               brand,
                                               size,
                                               color,
                                               suggested_retail_price,
                                               image)
    return jsonify(result)


@app.route("/product", methods=["PUT"])
def update_product():
    product_details = request.get_json()
    product_id = product_details["id"]
    name = product_details["name"]
    short_description = product_details["short_description"]
    brand = product_details["brand"]
    size = product_details["size"]
    color = product_details["color"]
    suggested_retail_price = product_details["suggested_retail_price"]
    image = product_details["image"]
    image = base64.b64encode(image)
    image = image.decode()
    image = json.dumps(image)
    result = product_details.update_product(product_id,
                                            name,
                                            short_description,
                                            brand,
                                            size,
                                            color,
                                            suggested_retail_price,
                                            image)
    return jsonify(result)


@app.route("/product/<product_id>", methods=["DELETE"])
def delete_game(product_id):
    result = product_controller.delete_product(product_id)
    return jsonify(result)


@app.route("/product/<product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = product_controller.get_product_by_id(product_id)
    product = list(product)
    image = base64.b64encode(product[6])
    decoded_image = image.decode()
    product.pop(6)
    product.insert(6, decoded_image)
    return jsonify(product)


# Frontend code
@app.route('/')
def index():
    products = product_controller.get_products()
    products_list = []
    for element in products:
        element = list(element)
        image = base64.b64encode(element[7])
        decoded_image = image.decode()
        element.insert(7, decoded_image)
        element.append(decoded_image)
        products_list.append(element)
    return render_template('index.html', products=products_list)


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
