import psycopg2
import getpass

def display():
    print("SELECT TABLE TO VIEW:")
    print("(1)Client")
    print("(2)Employee")
    print("(3)Department")
    print("(4)Parts Inventory")
    print("(5)Sales")
    print("(6)Supplier")
    print("(7)Vehicle")
    print("(8)Model")
    print("(9)Factory")

def client():
    sql_query = """SELECT * FROM client;"""
    return sql_query
def employee():
    sql_query = """SELECT * FROM employee;"""
    return sql_query
def department():
    sql_query = """SELECT * FROM department;"""
    return sql_query
def parts():
    sql_query = """SELECT * FROM parts_inventory;"""
    return sql_query
def sales():
    sql_query = """SELECT * FROM sales;"""
    return sql_query
def supplier():
    sql_query = """SELECT * FROM supplier;"""
    return sql_query
def vehicle():
    sql_query = """SELECT * FROM vehicle;"""
    return sql_query
def model():
    sql_query = """SELECT * FROM model;"""
    return sql_query
def factory():
    sql_query = """SELECT * FROM factory;"""
    return sql_query

def view(usr,psswd):
    try:
        with psycopg2.connect(database='tatadb',
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432) as connection:
            display()
            i = input("Choose index : ")
            sql_query = ""
            match i:
                case "1": 
                    sql_query = client()
                case "2": 
                    sql_query = employee()
                case "3": 
                    sql_query = department()
                case "4": 
                    sql_query = parts()
                case "5": 
                    sql_query = sales()
                case "6": 
                    sql_query = supplier()
                case "7": 
                    sql_query = vehicle()
                case "8": 
                    sql_query = model()
                case "9": 
                    sql_query = factory()
                case _:
                    print("INVALID INPUT!!")
                    exit()

            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                op = cursor.fetchall()
                for o in op:
                    print(o)
                connection.commit()
                cursor.close()
        connection.close()
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")
        # print(e)
    except psycopg2.Error as e:
        print(e)
        connection.rollback()

def main():
    usr = input("Enter username (usually postgres) : ")
    psswd = getpass.getpass("Enter password : ")
    view(usr,psswd)

# main()