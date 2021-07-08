import sqlite3


def get_db():
    conn = sqlite3.connect('dreamshop.db')
    return conn


def insert_product(name, short_description, brand, size, color, suggested_retail_price, image):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO products(name, short_description, brand, size, color, suggested_retail_price, image) " \
                "VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [name, short_description, brand, size, color, suggested_retail_price, image])
    db.commit()
    return True


def update_product(id, name, short_description, brand, size, color, suggested_retail_price, image):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE products " \
                "SET name = ?, " \
                "short_description = ?, " \
                "brand = ? , size = ?, " \
                "color = ?, " \
                "suggested_retail_price = ?, " \
                "image = ? " \
                "WHERE id = ?"
    cursor.execute(statement, [name, short_description, brand, size, color, suggested_retail_price, image, id])
    db.commit()
    return True


def delete_product(product_id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM products WHERE products.id = ?;" \
                "DELETE FROM inventory WHERE inventory.product_id = ?;"
    cursor.execute(statement, [product_id])
    db.commit()
    return True


def get_product_by_id(product_id):
    db = get_db()
    cursor = db.cursor()
    product_id
    # statement = "SELECT id, name, short_description, brand, size, color, suggested_retail_price, image
    # FROM products " \
    # "WHERE id = ?"
    statement = "SELECT products.name, products.short_description, products.brand, products.size, " \
                "products.color, products.suggested_retail_price, products.image, " \
                "inventory.amount_in_stock, inventory.out_of_stock_reason " \
                "FROM products, inventory " \
                "WHERE products.id = inventory.product_id and products.id = ?;"
    cursor.execute(statement, [product_id])
    return cursor.fetchone()


def get_products():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, short_description, brand, size, color, suggested_retail_price, image FROM products"
    cursor.execute(query)
    return cursor.fetchall()
