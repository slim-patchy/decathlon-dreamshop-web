DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    short_description TEXT NOT NULL,
    brand TEXT NOT NULL,
    size TEXT NOT NULL,
    color TEXT NOT NULL,
    suggested_retail_price REAL NOT NULL,
    image BLOB
);

DROP TABLE IF EXISTS items;
CREATE TABLE items (
    product_id INTEGER,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    quantity_shipped INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

DROP TABLE IF EXISTS inventory;
CREATE TABLE inventory (
    product_id INTEGER,
    amount_in_stock INTEGER NOT NULL,
    reorder_point TEXT,
    max_stock INTEGER NOT NULL,
    out_of_stock_reason TEXT,
    restock_date TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL DEFAULT 'Hong Kong',
    country TEXT NOT NULL DEFAULT 'China',
    postal_code TEXT,
    credit_ratings TEXT,
    comments TEXT
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    customer_id INTEGER,
    date_ordered TEXT NOT NULL,
    date_shipped TEXT NOT NULL,
    total REAL NOT NULL,
    payment_type TEXT NOT NULL DEFAULT 'Cash',
    order_filled INTEGER DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);