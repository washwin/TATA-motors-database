import psycopg2
import getpass

def display():
    print("SELECT TABLE FOR UPDATION:")
    print("(1)Client")
    print("(2)Employee")
    print("(3)Model")
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
                case "2":
                    update_query = employee()
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
    name = input("Client name : ")
    company = input("Company : ")
    email = input("Email : ")
    update_query = "INSERT INTO client (client_name,company_name,email) VALUES (\'" + name + "\',\'" + company + "\',\'" + email + "\');"
    return update_query

def employee():
    print("Enter the following details of employee")
    fname = input("First name : ")
    lname = input("Last name : ")
    email = input("Email : ")
    phno = input("Phone : ")
    address = input("Address(without commas) : ")
    desgn = input("Designation : ")
    dept = input("Department : ")
    update_query = "INSERT INTO client (client_name,company_name,email) VALUES (\'" + fname + "\',\'" + lname + "\',\'" + email + "\',"  +phno+ ",\'" +address+ "\',\'" +desgn+ "\'," +dept+ ");"
    return update_query


def main():
    usr = input("Enter username (usually postgres) : ")
    psswd = getpass.getpass("Enter password : ")
    update(usr,psswd)

# main()