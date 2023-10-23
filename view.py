import psycopg2
import getpass

def display():
    print("SELECT TABLE FOR UPDATION:")
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

def view(usr,psswd):
    try:
        with psycopg2.connect(database='tatadb',
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432) as connection:
            display()
            i = input("Choose index : ")
            update_query = ""
            match i:
                case "1": 
                    sql_query = client()
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

main()