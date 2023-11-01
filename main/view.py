import psycopg2
import sys
from tkinter import messagebox
import tkinter as tk

def display(root,usr,psswd):
    message_label = tk.Label(root, text="SELECT TABLE TO VIEW")
    message_label.pack(pady=10)
    selected_option = tk.StringVar()
    options = ["Client", "Employee", "Model", "Parts Inventory", "Sales", "Supplier", "Vehicle", "Factory", "Department"]
    selected_option.set(options[0])
    option_menu = tk.OptionMenu(root, selected_option, *options)
    option_menu.pack(pady=20)
    submit_button = tk.Button(root, text="Submit", command=lambda: view(selected_option.get(),usr,psswd))
    submit_button.pack(pady=20)

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

def view(option,usr,psswd):
    try:
        with psycopg2.connect(database='tatadb',
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432) as connection:
            # display()
            # i = input("Choose index : ")
            sql_query = ""
            match option:
                case "Client": 
                    sql_query = client()
                    output = "ID, NAME, COMPANY, EMAIL"
                case "Employee": 
                    sql_query = employee()
                    output = "ID, FNAME, LNAME, EMAIL, PHONE, ADDRESS, DESIGN, SALARY, DEPARTMENT"
                case "Department": 
                    sql_query = department()
                    output = "ID, DEPARTMENT"
                case "Parts Inventory": 
                    sql_query = parts()
                    output = "ID, NAME, SUPPLIER, EMPLOYEE, QUANTITY, PRICE"
                case "Sales": 
                    sql_query = sales()
                    output = "ID, CLIENT, EMPLOYEE, VEHICLE, DATE, PRICE, STATUS"
                case "Supplier": 
                    sql_query = supplier()
                    output = "ID, NAME, COMPANY, EMAIL"
                case "Vehicle": 
                    sql_query = vehicle()
                    output = "ID, MODEL, COLOR, YEAR, PRICE"
                case "Model": 
                    sql_query = model()
                    output = "ID, NAME, YEAR, ENGINE, FUEL, DIMENSION, 0-60, KM/L"
                case "Factory": 
                    sql_query = factory()
                    output = "EMPLOYEE, VEHICLE, WORK"
                case _:
                    print("INVALID INPUT!!")
                    messagebox.showerror("as", "sdf")
                    exit()

            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                op = cursor.fetchall()
                output = output + "\n"
                for r in op:
                    for c in r:
                        output = output + str(c) + ", "
                    output = output + "\n"
                messagebox.showinfo(option, output)
                connection.commit()
                cursor.close()
        connection.close()
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")
        messagebox.showerror("TATA Motors Database", "INVALID CREDENTIALS\n{}".format(e))
        # print(e)
    except psycopg2.Error as e:
        print(e)
        messagebox.showerror("TATA Motors Database", "INVALID\n{}".format(e))
        connection.rollback()
        
def are_credentials_valid(usr, psswd):
    try:
        with psycopg2.connect(database='tatadb', host="localhost", user=usr, password=psswd, port=5432):
            return True
    except psycopg2.OperationalError:
        return False
    
def main(usr, psswd):
    if are_credentials_valid(usr, psswd):
        root = tk.Tk()
        root.title("VIEW DATABASE")
        root.iconbitmap("blueprints/tata.ico")
        root.geometry("500x300")
        display(root,usr,psswd)
        root.mainloop()
    else:
        print("INVALID CREDENTIALS")
        messagebox.showerror("TATA Motors Database", "INVALID CREDENTIALS")

# main()
if __name__ == "__main__":
    if len(sys.argv) != 3:
        messagebox.showinfo("TATA Motors Database", "FILL THE FIELDS")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        main(username, password)