#!/usr/bin/env python3
import base64
import logging

from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

import product_controller

# Initialise SQLAlchemy to be used in the models
db = SQLAlchemy()

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


# Backend code

# One of the two read endpoints
@app.route('/products', methods=["GET"])
def get_products():
    products = product_controller.get_products()
    products_list = []
    for element in products:
        element = list(element)
        try:
            image = base64.b64encode(element[7])
            decoded_image = image.decode()
            element.pop(7)
            element.insert(7, decoded_image)
        except Exception:
            pass
        products_list.append(element)
    return jsonify(products_list)


# The create endpoint to add one new product at a time
@app.route("/product", methods=["POST"])
def insert_product():
    # product_details = request.get_data()
    product_details = request.form.to_dict(flat=False)
    name = product_details["name"][0]
    short_description = product_details["short_description"][0]
    brand = product_details["brand"][0]
    size = product_details["size"][0]
    color = product_details["color"][0]
    suggested_retail_price = product_details["suggested_retail_price"][0]
    image = product_details["image"][0]
    try:
        image = base64.b64encode(image)
        image = image.decode()
    except TypeError:
        image = image
    amount_in_stock = product_details["amount_in_stock"][0]
    reorder_point = product_details["reorder_point"][0]
    max_stock = product_details["max_stock"][0]
    out_of_stock_reason = product_details["out_of_stock_reason"][0]
    restock_date = product_details["restock_date"][0]
    result = product_controller.insert_product(name,
                                               short_description,
                                               brand,
                                               size,
                                               color,
                                               suggested_retail_price,
                                               image,
                                               amount_in_stock,
                                               reorder_point,
                                               max_stock,
                                               out_of_stock_reason,
                                               restock_date)
    return jsonify(result)


# The update endpoint for individual products
@app.route("/product", methods=["PUT"])
def update_product():
    product_details = request.form.to_dict(flat=False)
    product_id = product_details["product_id"][0]
    name = product_details["name"][0]
    short_description = product_details["short_description"][0]
    brand = product_details["brand"][0]
    size = product_details["size"][0]
    color = product_details["color"][0]
    suggested_retail_price = product_details["suggested_retail_price"][0]
    image = product_details["image"][0]
    try:
        image = base64.b64encode(image)
        image = image.decode()
    except TypeError:
        image = image
    amount_in_stock = product_details["amount_in_stock"][0]
    reorder_point = product_details["reorder_point"][0]
    max_stock = product_details["max_stock"][0]
    out_of_stock_reason = product_details["out_of_stock_reason"][0]
    restock_date = product_details["restock_date"][0]
    result = product_controller.update_product(product_id,
                                               name,
                                               short_description,
                                               brand,
                                               size,
                                               color,
                                               suggested_retail_price,
                                               image,
                                               amount_in_stock,
                                               reorder_point,
                                               max_stock,
                                               out_of_stock_reason,
                                               restock_date)
    return jsonify(result)


# The delete endpoint for products
@app.route("/product/<product_id>", methods=["DELETE"])
def delete_game(product_id):
    result = product_controller.delete_product(product_id)
    return jsonify(result)


# The second of the read endpoints for individual products
@app.route("/product/<product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = product_controller.get_product_by_id(product_id)
    product = list(product)

    try:
        image = base64.b64encode(product[7])
        decoded_image = image.decode()
    except TypeError:
        decoded_image = product[7]

    product.pop(7)
    product.insert(7, decoded_image)
    return jsonify(product)


# Frontend code
@app.route('/')
def index():
    products = product_controller.get_products()
    products_list = []
    for element in products:
        element = list(element)
        try:
            image = base64.b64encode(element[7])
            decoded_image = image.decode()
        except TypeError:
            decoded_image = element[7]
        element.pop(7)
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
