import psycopg2
import getpass
import sys
import os
import tkinter as tk
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def display(root,usr,psswd):
    message_label = tk.Label(root, text="SELECT TABLE FOR UPDATION")
    message_label.pack()
    selected_option = tk.StringVar()
    radio_button1 = tk.Radiobutton(root, text="Client", variable=selected_option, value="1")
    radio_button2 = tk.Radiobutton(root, text="Employee", variable=selected_option, value="2")
    radio_button3 = tk.Radiobutton(root, text="Model", variable=selected_option, value="3")
    radio_button4 = tk.Radiobutton(root, text="Parts Inventory", variable=selected_option, value="4")
    radio_button5 = tk.Radiobutton(root, text="Sales", variable=selected_option, value="5")
    radio_button6 = tk.Radiobutton(root, text="Supplier", variable=selected_option, value="6")
    radio_button7 = tk.Radiobutton(root, text="Vehicle", variable=selected_option, value="7")
    radio_button8 = tk.Radiobutton(root, text="Factory", variable=selected_option, value="8")
    radio_button9 = tk.Radiobutton(root, text="Department", variable=selected_option, value="9")
    radio_button_submit = tk.Button(root, text="Submit", command=lambda: type(root, selected_option.get(),usr,psswd))
    radio_button1.pack()
    radio_button2.pack()
    radio_button3.pack()
    radio_button4.pack()
    radio_button5.pack()
    radio_button6.pack()
    radio_button7.pack()
    radio_button8.pack()
    radio_button9.pack()
    radio_button_submit.pack()

def type(root,selected_option,usr,psswd):
    selected_type = tk.StringVar()
    label = tk.Label(root, text=f"SELECTED: {selected_option}")
    label.pack()
    message_label = tk.Label(root, text="SELECT TYPE OF UPDATION")
    message_label.pack()
    radio_button1 = tk.Radiobutton(root, text="Add", variable=selected_type, value="1")
    radio_button2 = tk.Radiobutton(root, text="Delete", variable=selected_type, value="2")
    radio_button3 = tk.Radiobutton(root, text="Update", variable=selected_type, value="3")
    radio_button_submit = tk.Button(root, text="Submit", command=lambda: update(usr,psswd,selected_option, selected_type.get()))
    radio_button1.pack()
    radio_button2.pack()
    radio_button3.pack()
    radio_button_submit.pack()

def execute(usr,psswd,update_query):
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
                cursor.close()
        connection.close()
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")
        # print(e)
    except psycopg2.Error as e:
        #print(f"Error updating employee's promotion: {e}")
        print("!!!!!!!!!!!!!UPDATE UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        connection.rollback()
    finally:
        cursor.close()


def update(usr,psswd,selected_option, selected_type):
    
    i = selected_option
    j=selected_type
    print(i+"\n"+j)
    update_query = ""
    match i:
        case '1':
            match j:
                case '1':
                    add_client(usr,psswd)
                case '2':
                    del_client()
                case '3':
                    update_client()
                case _:
                    print("INVALID OPTION")
            
        case '2':
            match j:
                case '1':
                    update_query = add_employee()
                case '2':
                    update_query = del_employee()
                case '3':
                    update_query = update_employee()
                case _:
                    print("INVALID OPTION")
            
        case '3':
            match j:
                case '1':
                    update_query = add_model()
                case '2':
                    update_query = del_model()
                case '3':
                    update_query = update_model()
                case _:
                    print("INVALID OPTION")
            
        case '4':
            match j:
                case '1':
                    update_query = add_part()
                case '2':
                    update_query = del_part()
                case '3':
                    update_query = update_part()
                case _:
                    print("INVALID OPTION")
            
        case '5':
            match j:
                case '1':
                    update_query = add_sale()
                case '2':
                    update_query = del_sale()
                case '3':
                    update_query = update_sale()
                case _:
                    print("INVALID OPTION")
            
        case '6':
            match j:
                case '1':
                    update_query = add_supply()
                case '2':
                    update_query = del_supply()
                case '3':
                    update_query = update_supply()
                case _:
                    print("INVALID OPTION")
            
        case '7':
            match j:
                case '1':
                    update_query = add_veh()
                case '2':
                    update_query = del_veh()
                case '3':
                    update_query = update_veh()
                case _:
                    print("INVALID OPTION")
            
        case '8':
            match j:
                case '1':
                    update_query = add_factory()
                case '2':
                    update_query = del_employee()
                case '3':
                    update_query = update_factory()
                case _:
                    print("INVALID OPTION")
        case '9':
            match j:
                case '1':
                    update_query = add_dept()
                case '2':
                    update_query = del_dept()
                case '3':
                    update_query = update_dept()
                case _:
                    print("INVALID OPTION")
        case _:
            print("INVALID INPUT")

def add_client(usr,psswd):
    client_window = tk.Tk()
    client_window.title("Add Client")
    
    # Create labels and entry fields for client details
    client_name_label = tk.Label(client_window, text="Client Name:")
    client_name_entry = tk.Entry(client_window)
    
    company_label = tk.Label(client_window, text="Company:")
    company_entry = tk.Entry(client_window)
    
    email_label = tk.Label(client_window, text="Email:")
    email_entry = tk.Entry(client_window)

    def add_client_to_db():
        name = client_name_entry.get()
        company = company_entry.get()
        email = email_entry.get()
        
        # Create a database connection and execute the SQL query to add the client
        try:
            conn = psycopg2.connect(database='tatadb', host='localhost', user=usr, password=psswd, port=5432)
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO client (client_name, company_name, email) VALUES ('{name}', '{company}', '{email}')")
            conn.commit()
            cursor.close()
            conn.close()
            #print("Client added successfully.")
            message_label = tk.Label(client_window, text="Client added successfully.")
            message_label.pack()
        except psycopg2.Error as e:
            print(f"Error adding client: {e}")
            message_label = tk.Label(client_window, text="Updation unsuccessfull.")
            message_label.pack()

    add_button = tk.Button(client_window, text="Add Client", command=add_client_to_db)
    
    # Pack labels, entry fields, and the button
    client_name_label.pack()
    client_name_entry.pack()
    company_label.pack()
    company_entry.pack()
    email_label.pack()
    email_entry.pack()
    add_button.pack()
    
    # Start the GUI main loop
    client_window.mainloop()
    # print("Enter the following details of client")
    
    # name = input("Client name : ")
    # company = input("Company : ")
    # email = input("Email : ")
    # update_query = "INSERT INTO client (client_name,company_name,email) VALUES (\'" + name + "\',\'" + company + "\',\'" + email + "\');"
    # return update_query

def del_client():
    print("Enter the following details of client")
    id = input("Client ID : ")
    update_query = f"DELETE FROM client WHERE client_id={id};"
    return update_query

def update_client():
    print("Enter the client ID and new details of client")
    id=input("Client ID : ")
    name = input("Client name : ")
    company = input("Company : ")
    email = input("Email : ")
    update_query =f"UPDATE client SET client_name='{name}' company_name='{company}' email='{email}' WHERE client_id={id};"
    return update_query

def add_employee():
    print("Enter the following details of employee")
    fname = input("First name : ")
    lname = input("Last name : ")
    email = input("Email : ")
    phno = input("Phone : ")
    address = input("Address(without commas) : ")
    desgn = input("Designation : ")
    dept = input("Department : ")
    update_query = "INSERT INTO employee (first_name,last_name,email,phone_no,address,designation,salary,department_id) VALUES (\'" + fname + "\',\'" + lname + "\',\'" + email + "\',"  +phno+ ",\'" +address+ "\',\'" +desgn+ "\'," +dept+ ");"
    return update_query

def del_employee():
    print("Enter the following details of employee")
    id = input("Employee ID : ")
    update_query = f"DELETE FROM employee WHERE employee_id={id};"
    return update_query

def update_employee():
    id = input("Enter Employee ID : ")
    role=input("Enter the new designation")
    salary = input("Enter new employee salary : ")
    update_query=f"UPDATE employee SET designation='{role}' salary={salary} WHERE employee_id={id};"
    return update_query

def add_model():
    print("Enter the following details of model")
    name = input("Model name : ")
    design_year = input("Design Year : ")
    engine_type=input("Engine Type : ")
    fuel_type = input("Fuel Type : ")
    dimensions= input("Dimensions : ")
    zero_to_sixty= input("Zero to Sixty : ")
    km_per_litres= input("Kilometers per Litre : ")
    update_query = "INSERT INTO model (model_name,design_year,engine_type,fuel_type,dimensions,zero_to_sixty,km_per_litres) VALUES (\'" + name + "\'," + design_year + ",\'" + engine_type + "\',\'" + fuel_type + "\',\'" + dimensions + "\'," + zero_to_sixty + "," + km_per_litres + ");"
    return update_query

def del_model():
    print("Enter the following details of model")
    id = input("Model ID : ")
    update_query = f"DELETE FROM model WHERE model_id={id};"
    return update_query

def update_model():
    print("Enter the model ID and new details of model")
    id=input("Model ID : ")
    name = input("Model name : ")
    design_year = input("Desugn Year : ")
    engine_type=input("Engine Type : ")
    fuel_type = input("Fuel Type : ")
    dimensions= input("Dimensions : ")
    zero_to_sixty= input("Zero to Sixty : ")
    km_per_litres= input("Kilometers per Litre : ")
    update_query = f"UPDATE model SET model_name='{name}' design_year={design_year} engine_type='{engine_type}' fuel_type='{fuel_type}' dimensions='{dimensions}' zero_to_sixty={zero_to_sixty} km_per_litres={km_per_litres}   WHERE model_id={id};"
    return update_query

def add_part():
    print("Enter the following details of part")
    name = input("Part name : ")
    supplier_id = input("Supplier ID: ")
    employee_id = input("Employee ID : ")
    qunatity= input("Qunatity : ")
    price= input("Price : ")
    update_query = "INSERT INTO parts_inventory (name,supplier_id,employee_id ,qunatity,price) VALUES (\'" + name + "\'," + supplier_id + "," + employee_id + "," + qunatity + "," + price + ");"
    return update_query

def del_part():
    print("Enter the following details of part")
    id = input("Part ID : ")
    update_query = f"DELETE FROM parts_inventory WHERE part_id={id};"
    return update_query

def update_part():
    id = input("Enter Employee ID : ")
    quantity = input("Enter quantity of part in stock : ")
    update_query=f"UPDATE parts_inventory SET in_stock_quantity={quantity} WHERE part_id={id};"
    return update_query


def update_sale():
    sales_id=input("Enter Sales ID: ")
    status = input("Enter current status: ")
    update_query=f"UPDATE sales SET status = '{status}' WHERE sales_id = {sales_id};"
    

def add_sale():
    client_id = input("Enter Client ID: ")
    emp_id = input("Enter Employee ID: ")
    price = input("Enter Sales price: ")
    status = input("Enter current status of the sale: ")
    date = input("Enter date of Sales : ")
    veh_id = input("Enter Vegicle ID: ")
    update_query = "INSERT INTO sales (client_id,employee_id,vehicle_id,sales_date,sales_price,status) VALUES (" + client_id + "," + emp_id + "," +veh_id + ",\'" +date+ "\'," + price + ",\'" +status+ "\');"
    return update_query

def del_sale():
    print("Enter the following details of the sale")
    id = input("Sale ID : ")
    update_query = f"DELETE FROM sales WHERE sales_id={id};"
    return update_query

def add_supply():
    print("Enter the following details of supplier")
    name = input("Supplier name : ")
    company = input("Company : ")
    email = input("Email : ")
    update_query = "INSERT INTO supplier (supplier_name,company_name,email) VALUES (\'" + name + "\',\'" + company + "\',\'" + email + "\');"
    return update_query

def del_supply():
    print("Enter the following details of supplier")
    id = input("Supplier ID : ")
    update_query = f"DELETE FROM supplier WHERE supplier_id={id};"
    return update_query

def update_supply():
    print("Enter the supplier ID and new details of supplier")
    id=input("Supplier ID : ")
    name = input("Supplier name : ")
    company = input("Company : ")
    email = input("Email : ")
    update_query =f"UPDATE supplier SET supplier_name='{name}' company_name='{company}' email='{email}' WHERE supplier_id={id};"
    return update_query

def add_veh():
    print("Enter the following details of vehicle")
    id = input("Model ID : ")
    color = input("Color : ")
    year = input("Year : ")
    price = input("Price : ")
    update_query = "INSERT INTO vehicle (model_id,color,year,price) VALUES (" + id + ",\'" + color    + "\'," + year + "," + price + ");"
    return update_query

def del_veh():
    print("Enter the following details of vehicle")
    id = input("Vehicle ID : ")
    update_query = f"DELETE FROM vehicle WHERE vehicle_id={id};"
    return update_query

def update_veh():
    print("Enter the vehicle ID and following new details of vehicle")
    veh=input("Vehicle ID : ")
    id = input("Model ID : ")
    color = input("Color : ")
    year = input("Year : ")
    price = input("Price : ")
    update_query = f"UPDATE vehicle SET model_id={id} color='{color}' year={year} price={price} WHERE vehicle_id={veh} ;"
    return update_query


def add_factory():
    print("Enter the following details of worker")
    id = input("Employee ID : ")
    veh = input("Vehicle ID : ")
    work = input("Work description : ")
    update_query = "INSERT INTO factory (employee_id,vehicle_id,work) VALUES (" + id + "," + veh + ",\'" + work + "\');"
    return update_query

def update_factory():
    id = input("Enter Employee ID : ")
    veh=input("Enter the Vehicle ID")
    work = input("Enter updated work : ")
    update_query=f"UPDATE factory SET work='{work}' WHERE employee_id={id} AND vehicle_id={veh};"
    return update_query

def add_dept():
    print("Enter the following details of Department")
    name=input("Department name : ")
    update_query = "INSERT INTO department (department_name) VALUES (\'" + name + "\');"
    return update_query

def del_dept():
    print("Enter the following details of Department")
    id = input("Department ID : ")
    update_query = f"DELETE FROM department WHERE vehicle_id={id};"
    return update_query

def update_dept():
    print("Enter the department ID and following new details of Department")
    id=input("Department ID : ")
    name=input("Department name : ")
    update_query = f"UPDATE department SET department_name='{name}' WHERE department_id={id};"
    return update_query


def are_credentials_valid(usr, psswd):
    try:
        with psycopg2.connect(database='tatadb', host="localhost", user=usr, password=psswd, port=5432):
            return True
    except psycopg2.OperationalError:
        return False

def main(usr,psswd):
    if are_credentials_valid(usr, psswd):
        root = tk.Tk()
        root.title("Database Updation")
        root.geometry("600x600")
        display(root,usr,psswd)
        root.mainloop()
    else:
        print("INVALID CREDENTIALS")
        message_label = tk.Label(root, text="INVALID CREDENTIALS")
        message_label.pack()



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: init.py <username> <password>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        main(username, password)