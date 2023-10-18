import psycopg2

def client():
    sql_query = """CREATE TABLE client(
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(40),
    company_name VARCHAR(40),
    email VARCHAR(40)
    );"""
    return sql_query


def department():
    sql_query = """CREATE TABLE department(
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(40)
    );"""
    return sql_query

def employee():
    sql_query = """CREATE TABLE employee(
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    email VARCHAR(40),
    phone_no VARCHAR(40),
    address VARCHAR(40),
    designation VARCHAR(15),
    salary INT,
    department_id INT NOT NULL,
    CONSTRAINT fk_tata_employee FOREIGN KEY(department_id) REFERENCES department(department_id)
    );"""
    return sql_query

def supplier():
    sql_query = """CREATE TABLE supplier(
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(40),
    company_name VARCHAR(40),
    email VARCHAR(40)
    );"""
    return sql_query

def model():
    sql_query = """CREATE TABLE model(
    model_id SERIAL PRIMARY KEY,
    model_name VARCHAR(40),
    design_year INT,
    engine_type VARCHAR(40),
    fuel_type VARCHAR(20),
    dimensions VARCHAR(20),
    zero_to_sixty INT,
    km_per_litres INT
    )"""
    return sql_query

def vehicle():
    sql_query = """CREATE TABLE vehicle(
    vehicle_id SERIAL PRIMARY KEY,
    model_id INT NOT NULL,
    color VARCHAR(10),
    year INT,
    price INT,
    CONSTRAINT fk_tata_vehicle1 FOREIGN KEY(model_id) REFERENCES model(model_id)
    );"""
    return sql_query

def sales():
    sql_query = """CREATE TABLE sales(
    sales_id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    vehicle_id INT NOT NULL UNIQUE,
    sales_date DATE,
    sales_price INT,
    status VARCHAR(10),
    CONSTRAINT fk_tata_sales1 FOREIGN KEY(client_id) REFERENCES client(client_id),
    CONSTRAINT fk_tata_sales2 FOREIGN KEY(vehicle_id) REFERENCES vehicle(vehicle_id)
    );"""
    return sql_query

def parts_inventory():
    sql_query = """CREATE TABLE parts_inventory(
    part_id SERIAL PRIMARY KEY,
    part_name VARCHAR(40),
    supplier_id INT NOT NULL,
    employee_id INT NOT NULL,
    in_stock_quantity INT,
    unit_price INT,
    CONSTRAINT fk_tata_inven1 FOREIGN KEY(supplier_id) REFERENCES supplier(supplier_id),
    CONSTRAINT fk_tata_inven2 FOREIGN KEY(employee_id) REFERENCES employee(employee_id)
    );"""
    return sql_query

def factory():
    sql_query = """CREATE TABLE factory(
    employee_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    work VARCHAR(40),
    CONSTRAINT fk_tata_factory1 FOREIGN KEY(employee_id) REFERENCES employee(employee_id),
    CONSTRAINT fk_tata_factory2 FOREIGN KEY(vehicle_id) REFERENCES vehicle(vehicle_id)
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
                cursor.execute(department())
                cursor.execute(employee())
                cursor.execute(client())
                cursor.execute(supplier())
                cursor.execute(model())
                cursor.execute(vehicle())
                cursor.execute(sales())
                cursor.execute(parts_inventory())
                cursor.execute(factory())
                connection.commit()
                print("ALL TABLES CREATED")
                cursor.close()
        connection.close()
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")

    except psycopg2.Error as e:
        print("!!!!!!!!!!!!!CREATE TABLES UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        connection.rollback()

# main("postgres","2402")