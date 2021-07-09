import sqlite3


def get_db():
    conn = sqlite3.connect('dreamshop_dev.db')
    return conn


def insert_product(name, short_description, brand, size, color, suggested_retail_price, image,
                   amount_in_stock, reorder_point, max_stock, out_of_stock_reason, restock_date):
    db = get_db()
    cursor = db.cursor()
    statement_1 = "INSERT INTO products(name, short_description, brand, size, color, suggested_retail_price, image) " \
                  "VALUES (?, ?, ?, ?, ?, ?, ?);"
    statement_2 = "INSERT INTO inventory(amount_in_stock, reorder_point, max_stock, out_of_stock_reason, restock_date) " \
                  "VALUES (?, ?, ?, ?, ?);"
    cursor.execute(statement_1, [name, short_description, brand, size, color, suggested_retail_price, image])
    cursor.execute(statement_2, [amount_in_stock, reorder_point, max_stock, out_of_stock_reason, restock_date])

    db.commit()
    return True


def update_product(product_id, name, short_description, brand, size, color, suggested_retail_price, image,
                   amount_in_stock, reorder_point, max_stock, out_of_stock_reason, restock_date,):
    db = get_db()
    cursor = db.cursor()
    statement_1 = "UPDATE products "\
                  "SET name = ?, "\
                  "short_description = ?, "\
                  "brand = ? , "\
                  "size = ?, "\
                  "color = ?, "\
                  "suggested_retail_price = ?, "\
                  "image = ? "\
                  "WHERE id = ?;"
    statement_2 = "UPDATE inventory " \
                  "SET amount_in_stock = ?," \
                  "reorder_point = ?, " \
                  "max_stock = ?, " \
                  "out_of_stock_reason = ?, " \
                  "restock_date = ? " \
                  "WHERE product_id = ?;"
    cursor.execute(statement_1, [name, short_description, brand, size, color, suggested_retail_price, image, product_id])
    cursor.execute(statement_2, [amount_in_stock, reorder_point, max_stock, out_of_stock_reason, restock_date, product_id])
    db.commit()
    return True


def delete_product(product_id):
    db = get_db()
    cursor = db.cursor()
    statement_1 = "DELETE FROM products WHERE products.id = ?;"
    statement_2 = "DELETE FROM inventory WHERE inventory.product_id = ?;"
    cursor.execute(statement_1, [product_id])
    cursor.execute(statement_2, [product_id])
    db.commit()
    return True


def get_product_by_id(product_id):
    db = get_db()
    cursor = db.cursor()
    product_id
    statement = "SELECT products.id, products.name, products.short_description, products.brand, products.size, " \
                "products.color, products.suggested_retail_price, products.image, " \
                "inventory.amount_in_stock, inventory.out_of_stock_reason " \
                "FROM products, inventory " \
                "WHERE products.id = inventory.product_id and products.id = ?;"
    cursor.execute(statement, [product_id])
    return cursor.fetchone()


def get_products():
    db = get_db()
    cursor = db.cursor()
    # query = "SELECT id, name, short_description, brand, size, color, suggested_retail_price, image FROM products"
    query = "SELECT products.id, " \
            "products.name, " \
            "products.short_description, " \
            "products.brand, " \
            "products.size, " \
            "products.color, " \
            "products.suggested_retail_price, " \
            "products.image, " \
            "inventory.amount_in_stock, " \
            "inventory.out_of_stock_reason " \
            "FROM products, inventory WHERE products.id = inventory.product_id;"
    cursor.execute(query)
    return cursor.fetchall()
