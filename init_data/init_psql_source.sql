-- Create user table:
CREATE SEQUENCE user_id_seq START WITH 1 INCREMENT BY 1;
CREATE TABLE IF NOT EXISTS users (
    user_id int default nextval('user_id_seq'::regclass) PRIMARY KEY ,
    name varchar(255),
    email varchar(255),
    mobile varchar(255),
    created_at timestamp DEFAULT now(),
    updated_at timestamp
)
;
-- Ingest Data:

-- Create transaction table:
CREATE SEQUENCE transaction_id_seq START WITH 1 INCREMENT BY 1;
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id int default nextval('transaction_id_seq'::regclass) PRIMARY KEY ,
    user_id int ,
    order_id int,
    paid_price int,
    status int,
    created_at timestamp DEFAULT now(),
    updated_at timestamp
)
;

-- Create order table:
CREATE SEQUENCE order_id_seq START WITH 1 INCREMENT BY 1;
CREATE TABLE IF NOT EXISTS orders (
    order_id int,
    item_id int,
    num int ,
    price int,
    created_at timestamp DEFAULT now(),
    updated_at timestamp
)
;

-- Create menu table:
CREATE SEQUENCE menu_id_seq START WITH 1 INCREMENT BY 1;
CREATE TABLE IF NOT EXISTS menus (
    item_id int default nextval('menu_id_seq'::regclass) PRIMARY KEY ,
    name varchar(255),
    price int,
    created_at timestamp DEFAULT now(),
    updated_at timestamp
)
;

