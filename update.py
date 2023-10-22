import psycopg2
import getpass

def display():
    print("SELECT TABLE FOR UPDATION:")
    print("(1)Client")
    print("(2)Employee")
    print("(3)Employee Training")
    print("(4)Parts Inventory")
    print("(5)Sales")
    print("(6)Supplier")
    print("(7)Vehicle")

def update(usr,psswd):
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
                    update_query = client()
                case _: 
                    print("INVALID INPUT!!")
                    exit()

            with connection.cursor() as cursor:
                cursor.execute(update_query)
                connection.commit()
                print("UPDATE SUCCESSFUL")
                cursor.close()
        connection.close()
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")
        # print(e)
    except psycopg2.Error as e:
        print("!!!!!!!!!!!!!UPDATE UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        connection.rollback()

def client():
    print("Enter the following details of client")
    cid = input("client id : ")
    fname = input("First name : ")
    lname = input("Last name : ")
    email = input("Email : ")
    phone = input("Phone no : ")
    address = input("Address(without commas) : ")
    update_query = "INSERT INTO client VALUES (" + cid + ",\'" + fname + "\',\'" + lname + "\',\'" + email + "\',\'" + phone + "\',\'" + address + "\');"
    return update_query

def main():
    usr = input("Enter username (usually postgres) : ")
    psswd = getpass.getpass("Enter password : ")
    update(usr,psswd)


main()