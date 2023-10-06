import psycopg2

def customer():
    sql_query = """CREATE TABLE customer(
    customer_id INT NOT NULL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(20),
    phone_no VARCHAR(20),
    address VARCHAR(20)
    )"""
    return sql_query

def vehicle():
    sql_query = """CREATE TABLE vehicle(
    vehicle_id INT NOT NULL PRIMARY KEY,
    make VARCHAR(10),
    model VARCHAR(20),
    year INT,
    vin INT,
    color VARCHAR(10),
    price INT,
    stock_quantity INT,
    engine_type VARCHAR(10),
    fuel_type VARCHAR(10)
    )"""
    return sql_query

def sales():
    sql_query = """CREATE TABLE sales(
    sales_id INT NOT NULL PRIMARY KEY,
    customer_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    CONSTRAINT fk_tata_sales1 FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
    CONSTRAINT fk_tata_sales2 FOREIGN KEY(vehicle_id) REFERENCES vehicle(vehicle_id),
    sales_date DATE,
    sales_price INT,
    payment_method VARCHAR(10)
    )"""
    return sql_query

def employee():
    sql_query = """CREATE TABLE employee(
    employee_id INT NOT NULL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(20),
    phone_no VARCHAR(20),
    address VARCHAR(20),
    job_title VARCHAR(15),
    department VARCHAR(20)
    )"""
    return sql_query

def supplier():
    sql_query = """CREATE TABLE supplier(
    supplier_id INT NOT NULL PRIMARY KEY,
    supplier_name VARCHAR(20),
    contact_name VARCHAR(20),
    email VARCHAR(20),
    phone_no VARCHAR(20),
    address VARCHAR(50)
    )"""
    return sql_query

def parts_inventory():
    sql_query = """CREATE TABLE parts_inventory(
    part_id INT NOT NULL PRIMARY KEY,
    part_name VARCHAR(20),
    supplier_id INT NOT NULL,
    CONSTRAINT fk_tata_inven1 FOREIGN KEY(supplier_id) REFERENCES supplier(supplier_id),
    in_stock_quantity INT,
    unit_price INT,
    reoerder_level INT
    )"""
    return sql_query

def employee_training():
    sql_query = """CREATE TABLE employee_training(
    training_id INT NOT NULL PRIMARY KEY,
    employee_id INT NOT NULL,
    CONSTRAINT fk_tata_train1 FOREIGN KEY(employee_id) REFERENCES employee(employee_id),
    training_name VARCHAR(20),
    training_date DATE
    )"""
    return sql_query

def main(usr,psswd):
    try:
        with psycopg2.connect(database='tatadb',
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432) as connection:

            with connection.cursor() as cursor:                
                cursor.execute(customer())
                cursor.execute(vehicle())
                cursor.execute(sales())
                cursor.execute(employee())
                cursor.execute(supplier())
                cursor.execute(parts_inventory())
                cursor.execute(employee_training())
                connection.commit()
                print("ALL TABLES CREATED")
    except psycopg2.Error as e:
        print("!!!!!!!!!!!!!CREATE TABLES UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

main("postgres","2202")