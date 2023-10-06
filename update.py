import psycopg2

def update(usr,psswd,update_query):
    try:
        with psycopg2.connect(database='tatadb',
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432) as connection:

            with connection.cursor() as cursor:
                cursor.execute(update_query)
                connection.commit()
                print("UPDATE SUCCESSFUL")
    except psycopg2.Error as e:
        print(e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def customer():
    print("Enter the following details of customer")
    cid = input("Customer id : ")
    fname = input("First name : ")
    lname = input("Last name : ")
    email = input("Email : ")
    phone = input("Phone no : ")
    address = input("Address(without commas) : ")
    update_query = "INSERT INTO customer VALUES (" + cid + ",\'" + fname + "\',\'" + lname + "\',\'" + email + "\',\'" + phone + "\',\'" + address + "\');"
    return update_query

def main():
    usr = input("Enter username (usually postgres) : ")
    psswd = input("Enter password : ")
    update(usr, psswd, customer())

main()