import psycopg2
import getpass
import sys
import os
import tkinter as tk
from tkinter import messagebox
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def display(root,usr,psswd):
    message_label = tk.Label(root, text="SELECT TABLE FOR UPDATION")
    message_label.pack(pady=10)
    selected_option = tk.StringVar()
    options = ["Client", "Employee", "Model", "Parts Inventory", "Sales", "Supplier", "Vehicle", "Factory", "Department"]
    selected_option.set(options[0])
    option_menu = tk.OptionMenu(root, selected_option, *options)
    option_menu.pack(pady=20)
    submit_button = tk.Button(root, text="Submit", command=lambda: type(root, selected_option.get(),usr,psswd))
    submit_button.pack(pady=20)


def type(root,selected_option,usr,psswd):
    type_window = tk.Toplevel(root)
    type_window.title("TATA Motors Database")
    type_window.iconbitmap('./blueprints/tata.ico')
    type_window.geometry("300x150")

    selected_type = tk.StringVar()
    label = tk.Label(type_window, text=f"SELECTED: {selected_option}")
    label.pack()
    message_label = tk.Label(type_window, text="SELECT TYPE OF UPDATION")
    message_label.pack()
    # radio_button1.deselect()
    # radio_button2.deselect()
    # radio_button3.deselect()
    radio_button1 = tk.Radiobutton(type_window, text="Add", variable=selected_type, value="1")
    radio_button2 = tk.Radiobutton(type_window, text="Delete", variable=selected_type, value="2")
    radio_button3 = tk.Radiobutton(type_window, text="Update", variable=selected_type, value="3")
    radio_button1.pack()
    radio_button2.pack()
    radio_button3.pack()
    submit = tk.Button(type_window, text="SUBMIT", command=lambda: update(usr,psswd,selected_option, selected_type.get()))
    submit.pack()

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
                messagebox.showinfo("TATA Motors Database", "UPDATE SUCCESSFUL")
                cursor.close()
        connection.close()
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")
        messagebox.showerror("TATA Motors Database", "INVALID CREDENTIALS\n{}".format(e))
        # print(e)
    except psycopg2.Error as e:
        #print(f"Error updating employee's promotion: {e}")
        print("!!!!!!!!!!!!!UPDATE UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        messagebox.showerror("TATA Motors Database", "UPDATE UNSUCCESSFUL\n{}".format(e))
        connection.rollback()
    finally:
        cursor.close()


def update(usr,psswd,selected_option, selected_type):
    
    i = selected_option
    j=selected_type
    #print(i+"\n"+j)
    update_query = ""
    match i:
        case 'Client':
            match j:
                case '1':
                    add_client(usr,psswd)
                case '2':
                    del_client(usr,psswd)
                case '3':
                    update_client(usr,psswd)
                case _:
                    print("INVALID OPTION")
            
        case 'Employee':
            match j:
                case '1':
                    add_employee(usr,psswd)
                case '2':
                    del_employee(usr,psswd)
                case '3':
                    update_employee(usr,psswd)
                case _:
                    print("INVALID OPTION")
            
        case 'Model':
            match j:
                case '1':
                    add_model(usr,psswd)
                case '2':
                    del_model(usr,psswd)
                case '3':
                    update_model(usr,psswd)
                case _:
                    print("INVALID OPTION")
            
        case 'Parts Inventory':
            match j:
                case '1':
                    add_part(usr,psswd)
                case '2':
                    del_part(usr,psswd)
                case '3':
                    update_part(usr,psswd)
                case _:
                    print("INVALID OPTION")
            
        case 'Sales':
            match j:
                case '1':
                    add_sale(usr,psswd)
                case '2':
                    del_sale(usr,psswd)
                case '3':
                    update_sale(usr,psswd)
                case _:
                    print("INVALID OPTION")
            
        case 'Supplier':
            match j:
                case '1':
                    add_supply(usr,psswd)
                case '2':
                    del_supply(usr,psswd)
                case '3':
                    update_supply(usr,psswd)
                case _:
                    print("INVALID OPTION")
            
        case 'Vehicle':
            match j:
                case '1':
                    add_veh(usr,psswd)
                case '2':
                    del_veh(usr,psswd)
                case '3':
                    update_veh(usr,psswd)
                case _:
                    print("INVALID OPTION")
            
        case 'Factory':
            match j:
                case '1':
                    add_factory(usr,psswd)
                case '2':
                    del_employee(usr,psswd)
                case '3':
                    update_factory(usr,psswd)
                case _:
                    print("INVALID OPTION")
        case 'Dapartment':
            match j:
                case '1':
                    add_dept(usr,psswd)
                case '2':
                    del_dept(usr,psswd)
                case '3':
                    update_dept(usr,psswd)
                case _:
                    print("INVALID OPTION")
        case _:
            print("INVALID INPUT")

def add_client(usr,psswd):
    client_window = tk.Tk()
    client_window.title("Add Client")
    client_window.geometry("400x500")
    # Create labels and entry fields for client details
    client_name_label = tk.Label(client_window, text="Client Name:")
    client_name_entry = tk.Entry(client_window)
    
    company_label = tk.Label(client_window, text="Company:")
    company_entry = tk.Entry(client_window)
    
    email_label = tk.Label(client_window, text="Email:")
    email_entry = tk.Entry(client_window)

    def client_to_db(usr,psswd):
        name = client_name_entry.get()
        company = company_entry.get()
        email = email_entry.get()
        update_query = f"INSERT INTO client (client_name, company_name, email) VALUES ('{name}', '{company}', '{email}')"
        execute(usr,psswd,update_query)

    add_button = tk.Button(client_window, text="Add Client", command=lambda:client_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    client_name_label.pack(pady=20)
    client_name_entry.pack(pady=20)
    company_label.pack(pady=20)
    company_entry.pack(pady=20)
    email_label.pack(pady=20)
    email_entry.pack(pady=20)
    add_button.pack(pady=20)
    
    client_window.mainloop()

def del_client(usr,psswd):
    # print("Enter the following details of client")
    # id = input("Client ID : ")
    # update_query = f"DELETE FROM client WHERE client_id={id};"
    # return update_query
    client_window = tk.Tk()
    client_window.title("Delete Client")
    client_window.geometry("400x500")
    # Create labels and entry fields for client details
    client_id_label = tk.Label(client_window, text="Client ID:")
    client_id_entry = tk.Entry(client_window)

    def client_to_db(usr,psswd):
        id = client_id_entry.get()
        update_query = f"DELETE FROM client WHERE client_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(client_window, text="Delete Client", command=lambda:client_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    client_id_label.pack()
    client_id_entry.pack()
    add_button.pack()
    
    client_window.mainloop()

def update_client(usr,psswd):
    # print("Enter the client ID and new details of client")
    # id=input("Client ID : ")
    # name = input("Client name : ")
    # company = input("Company : ")
    # email = input("Email : ")
    # update_query =f"UPDATE client SET client_name='{name}' company_name='{company}' email='{email}' WHERE client_id={id};"
    # return update_query
    client_window = tk.Tk()
    client_window.title("Update Client")
    client_window.geometry("400x500")
    # Create labels and entry fields for client details

    client_id_label = tk.Label(client_window, text="Client ID:")
    client_id_entry = tk.Entry(client_window)

    client_name_label = tk.Label(client_window, text="Client Name:")
    client_name_entry = tk.Entry(client_window)
    
    company_label = tk.Label(client_window, text="Company:")
    company_entry = tk.Entry(client_window)
    
    email_label = tk.Label(client_window, text="Email:")
    email_entry = tk.Entry(client_window)

    def client_to_db(usr,psswd):
        name = client_name_entry.get()
        company = company_entry.get()
        email = email_entry.get()
        id=client_id_entry.get()
        update_query = f"UPDATE client SET client_name='{name}',company_name='{company}',email='{email}' WHERE client_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(client_window, text="Update Client", command=lambda:client_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    client_id_label.pack()
    client_id_entry.pack()
    client_name_label.pack()
    client_name_entry.pack()
    company_label.pack()
    company_entry.pack()
    email_label.pack()
    email_entry.pack()
    add_button.pack()
    
    client_window.mainloop()
    

def add_employee(usr,psswd):
    # print("Enter the following details of employee")
    # fname = input("First name : ")
    # lname = input("Last name : ")
    # email = input("Email : ")
    # phno = input("Phone : ")
    # address = input("Address(without commas) : ")
    # desgn = input("Designation : ")
    # dept = input("Department : ")
    # update_query = "INSERT INTO employee (first_name,last_name,email,phone_no,address,designation,salary,department_id) VALUES (\'" + fname + "\',\'" + lname + "\',\'" + email + "\',"  +phno+ ",\'" +address+ "\',\'" +desgn+ "\'," +dept+ ");"
    # return update_query
    employee_window = tk.Tk()
    employee_window.title("Add employee")
    employee_window.geometry("400x500")
    # Create labels and entry fields for employee details

    employee_fname_label = tk.Label(employee_window, text="Employee First Name:")
    employee_fname_entry = tk.Entry(employee_window)

    employee_lname_label = tk.Label(employee_window, text="Employee Last Name:")
    employee_lname_entry = tk.Entry(employee_window)
    
    phno_label = tk.Label(employee_window, text="Phone Number:")
    phno_entry = tk.Entry(employee_window)
    
    email_label = tk.Label(employee_window, text="Email:")
    email_entry = tk.Entry(employee_window)

    addrs_label = tk.Label(employee_window, text="Address:")
    addrs_entry = tk.Entry(employee_window)

    dsgn_label = tk.Label(employee_window, text="Designation:")
    dsgn_entry = tk.Entry(employee_window)

    dept_label = tk.Label(employee_window, text="DepartmentID:")
    dept_entry = tk.Entry(employee_window)

    salary_label = tk.Label(employee_window, text="Salary:")
    salary_entry = tk.Entry(employee_window)

    def employee_to_db(usr,psswd):
        fname = employee_fname_entry.get()
        lname=employee_lname_entry.get()
        phno = phno_entry.get()
        address=addrs_entry.get()
        email = email_entry.get()
        desgn=dsgn_entry.get()
        dept=dept_entry.get()
        salary=salary_entry.get()
        update_query = "INSERT INTO employee (first_name,last_name,email,phone_no,address,designation,salary,department_id) VALUES (\'" + fname + "\',\'" + lname + "\',\'" + email + "\',"  +phno+ ",\'" +address+ "\',\'" +desgn+ "\'," +salary+"," +dept+ ");"
        execute(usr,psswd,update_query)

    add_button = tk.Button(employee_window, text="Add employee", command=lambda:employee_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    employee_fname_label.pack()
    employee_fname_entry.pack()
    employee_lname_label.pack()
    employee_lname_entry.pack()
    phno_label.pack()
    phno_entry.pack()
    addrs_label.pack()
    addrs_entry.pack()
    email_label.pack()
    email_entry.pack()
    salary_label.pack()
    salary_entry.pack()
    dsgn_label.pack()
    dsgn_entry.pack()
    dept_label.pack()
    dept_entry.pack()
    add_button.pack()
    
    employee_window.mainloop()

def del_employee(usr,psswd):
    # print("Enter the following details of employee")
    # id = input("Employee ID : ")
    # update_query = f"DELETE FROM employee WHERE employee_id={id};"
    # return update_query
    employee_window = tk.Tk()
    employee_window.title("Delete employee")
    employee_window.geometry("400x500")
    # Create labels and entry fields for employee details
    employee_id_label = tk.Label(employee_window, text="Employee ID:")
    employee_id_entry = tk.Entry(employee_window)

    def employee_to_db(usr,psswd):
        id = employee_id_entry.get()
        update_query = f"DELETE FROM employee WHERE employee_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(employee_window, text="Delete employee", command=lambda:employee_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    employee_id_label.pack()
    employee_id_entry.pack()
    add_button.pack()
    
    employee_window.mainloop()

def update_employee(usr,psswd):
    # id = input("Enter Employee ID : ")
    # role=input("Enter the new designation")
    # salary = input("Enter new employee salary : ")
    # update_query=f"UPDATE employee SET designation='{role}' salary={salary} WHERE employee_id={id};"
    # return update_query
    employee_window = tk.Tk()
    employee_window.title("Update employee")
    employee_window.geometry("400x500")
    # Create labels and entry fields for employee details
    employee_id_label = tk.Label(employee_window, text="Employee ID:")
    employee_id_entry = tk.Entry(employee_window)

    employee_role_label = tk.Label(employee_window, text="Updated Designation:")
    employee_role_entry = tk.Entry(employee_window)

    employee_salary_label = tk.Label(employee_window, text="Updated salary:")
    employee_salary_entry = tk.Entry(employee_window)
    
    

    def employee_to_db(usr,psswd):
        role = employee_role_entry.get()
        salary=employee_salary_entry.get()
        id=employee_id_entry.get()
        update_query = f"UPDATE employee SET designation='{role}', salary={salary} WHERE employee_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(employee_window, text="Update employee", command=lambda:employee_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    employee_role_label.pack()
    employee_role_entry.pack()
    employee_salary_label.pack()
    employee_salary_entry.pack()
    employee_id_label.pack()
    employee_id_entry.pack()
    add_button.pack()
    
    employee_window.mainloop()

def add_model(usr,psswd):
    # print("Enter the following details of model")
    # name = input("Model name : ")
    # design_year = input("Design Year : ")
    # engine_type=input("Engine Type : ")
    # fuel_type = input("Fuel Type : ")
    # dimensions= input("Dimensions : ")
    # zero_to_sixty= input("Zero to Sixty : ")
    # km_per_litres= input("Kilometers per Litre : ")
    # update_query = "INSERT INTO model (model_name,design_year,engine_type,fuel_type,dimensions,zero_to_sixty,km_per_litres) VALUES (\'" + name + "\'," + design_year + ",\'" + engine_type + "\',\'" + fuel_type + "\',\'" + dimensions + "\'," + zero_to_sixty + "," + km_per_litres + ");"
    # return update_query
    model_window = tk.Tk()
    model_window.title("Add model")
    model_window.geometry("400x500")
    # Create labels and entry fields for model details

    model_name_label = tk.Label(model_window, text="Model Name:")
    model_name_entry = tk.Entry(model_window)
    
    engine_type_label = tk.Label(model_window, text="Engine Type:")
    engine_type_entry = tk.Entry(model_window)
    
    fuel_type_label = tk.Label(model_window, text="Fuel Type:")
    fuel_type_entry = tk.Entry(model_window)

    dimensions_label = tk.Label(model_window, text="Dimensions:")
    dimensions_entry= tk.Entry(model_window)

    design_year_label = tk.Label(model_window, text="Design Year:")
    design_year_entry = tk.Entry(model_window)

    zero_to_sixty_label = tk.Label(model_window, text="zero_to_sixty:")
    zero_to_sixty_entry = tk.Entry(model_window)

    km_per_litres_label = tk.Label(model_window, text="km_per_litres:")
    km_per_litres_entry = tk.Entry(model_window)

    def model_to_db(usr,psswd):
        name = model_name_entry.get()
        engine_type=engine_type_entry.get()
        fuel_type = fuel_type_entry.get()
        dimensions=dimensions_entry.get()
        zero_to_sixty = zero_to_sixty_entry.get()
        design_year=design_year_entry.get()
        km_per_litres=km_per_litres.get()
        update_query = "INSERT INTO model (model_name,design_year,engine_type,fuel_type,dimensions,zero_to_sixty,km_per_litres) VALUES (\'" + name + "\'," + design_year + ",\'" + engine_type + "\',\'" + fuel_type + "\',\'" + dimensions + "\'," + zero_to_sixty + "," + km_per_litres + ");"
        execute(usr,psswd,update_query)

    add_button = tk.Button(model_window, text="Add model", command=lambda:model_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    model_name_label.pack()
    model_name_entry.pack()
    engine_type_label.pack()
    engine_type_entry.pack()
    fuel_type_label.pack()
    fuel_type_entry.pack()
    dimensions_label.pack()
    dimensions_entry.pack()
    zero_to_sixty_label.pack()
    zero_to_sixty_entry.pack()
    design_year_label.pack()
    design_year_entry.pack()
    km_per_litres_label.pack()
    km_per_litres_entry.pack()
    add_button.pack()
    
    model_window.mainloop()


def del_model(usr,psswd):
    # print("Enter the following details of model")
    # id = input("Model ID : ")
    # update_query = f"DELETE FROM model WHERE model_id={id};"
    # return update_query
    model_window = tk.Tk()
    model_window.title("Delete model")
    model_window.geometry("400x500")
    # Create labels and entry fields for model details
    model_id_label = tk.Label(model_window, text="Model ID:")
    model_id_entry = tk.Entry(model_window)

    def model_to_db(usr,psswd):
        id = model_id_entry.get()
        update_query = f"DELETE FROM model WHERE model_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(model_window, text="Delete model", command=lambda:model_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    model_id_label.pack()
    model_id_entry.pack()
    add_button.pack()
    
    model_window.mainloop()

def update_model(usr,psswd):
    # print("Enter the model ID and new details of model")
    # id=input("Model ID : ")
    # name = input("Model name : ")
    # design_year = input("Desugn Year : ")
    # engine_type=input("Engine Type : ")
    # fuel_type = input("Fuel Type : ")
    # dimensions= input("Dimensions : ")
    # zero_to_sixty= input("Zero to Sixty : ")
    # km_per_litres= input("Kilometers per Litre : ")
    # update_query = f"UPDATE model SET model_name='{name}' design_year={design_year} engine_type='{engine_type}' fuel_type='{fuel_type}' dimensions='{dimensions}' zero_to_sixty={zero_to_sixty} km_per_litres={km_per_litres}   WHERE model_id={id};"
    # return update_query
    model_window = tk.Tk()
    model_window.title("Update model")
    model_window.geometry("400x500")
    # Create labels and entry fields for model details

    model_id_label = tk.Label(model_window, text="Model ID:")
    model_id_entry = tk.Entry(model_window)

    model_name_label = tk.Label(model_window, text="Model Name:")
    model_name_entry = tk.Entry(model_window)
    
    engine_type_label = tk.Label(model_window, text="Engine Type:")
    engine_type_entry = tk.Entry(model_window)
    
    fuel_type_label = tk.Label(model_window, text="Fuel Type:")
    fuel_type_entry = tk.Entry(model_window)

    dimensions_label = tk.Label(model_window, text="Dimensions:")
    dimensions_entry= tk.Entry(model_window)

    design_year_label = tk.Label(model_window, text="Design Year:")
    design_year_entry = tk.Entry(model_window)

    zero_to_sixty_label = tk.Label(model_window, text="zero_to_sixty:")
    zero_to_sixty_entry = tk.Entry(model_window)

    km_per_litres_label = tk.Label(model_window, text="km_per_litres:")
    km_per_litres_entry = tk.Entry(model_window)

    def model_to_db(usr,psswd):
        id=model_id_entry.get()
        name = model_name_entry.get()
        engine_type=engine_type_entry.get()
        fuel_type = fuel_type_entry.get()
        dimensions=dimensions_entry.get()
        zero_to_sixty = zero_to_sixty_entry.get()
        design_year=design_year_entry.get()
        km_per_litres=km_per_litres.get()
        update_query = f"UPDATE model SET model_name='{name}' ,design_year={design_year}, engine_type='{engine_type}', fuel_type='{fuel_type}', dimensions='{dimensions}' ,zero_to_sixty={zero_to_sixty} ,km_per_litres={km_per_litres}   WHERE model_id={id};"
        execute(usr,psswd,update_query)
    add_button = tk.Button(model_window, text="Update model", command=lambda:model_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    
    model_id_label.pack()
    model_id_entry.pack()
    model_name_label.pack()
    model_name_entry.pack()
    engine_type_label.pack()
    engine_type_entry.pack()
    fuel_type_label.pack()
    fuel_type_entry.pack()
    dimensions_label.pack()
    dimensions_entry.pack()
    zero_to_sixty_label.pack()
    zero_to_sixty_entry.pack()
    design_year_label.pack()
    design_year_entry.pack()
    km_per_litres_label.pack()
    km_per_litres_entry.pack()
    add_button.pack()
    
    model_window.mainloop()

def add_part(usr,psswd):
    # print("Enter the following details of part")
    # name = input("Part name : ")
    # supplier_id = input("Supplier ID: ")
    # employee_id = input("Employee ID : ")
    # qunatity= input("Qunatity : ")
    # price= input("Price : ")
    # update_query = "INSERT INTO parts_inventory (name,supplier_id,employee_id ,qunatity,price) VALUES (\'" + name + "\'," + supplier_id + "," + employee_id + "," + qunatity + "," + price + ");"
    # return update_query
    part_window = tk.Tk()
    part_window.title("Add part")
    part_window.geometry("400x500")
    # Create labels and entry fields for part details

    part_name_label = tk.Label(part_window, text="Part Name:")
    part_name_entry = tk.Entry(part_window)
    
    supplier_id_type_label = tk.Label(part_window, text="Supplier ID:")
    supplier_id_type_entry = tk.Entry(part_window)
    
    employee_id_label = tk.Label(part_window, text="Employee ID:")
    employee_id_entry = tk.Entry(part_window)

    qunatity_label = tk.Label(part_window, text="Qunatity:")
    qunatity_entry= tk.Entry(part_window)

    price_label = tk.Label(part_window, text="Price:")
    price_entry = tk.Entry(part_window)

    def part_to_db(usr,psswd):
        name = part_name_entry.get()
        supplier_id=supplier_id_type_entry.get()
        employee_id = employee_id_entry.get()
        qunatity=qunatity_entry.get()
        price=price_entry.get()
        update_query = "INSERT INTO parts_inventory (name,supplier_id,employee_id ,qunatity,price) VALUES (\'" + name + "\'," + supplier_id + "," + employee_id + "," + qunatity + "," + price + ");"
        execute(usr,psswd,update_query)

    add_button = tk.Button(part_window, text="Add part", command=lambda:part_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    part_name_label.pack()
    part_name_entry.pack()
    supplier_id_type_label.pack()
    supplier_id_type_entry.pack()
    employee_id_label.pack()
    employee_id_entry.pack()
    qunatity_label.pack()
    qunatity_entry.pack()
    price_label.pack()
    price_entry.pack()
    add_button.pack()
    
    part_window.mainloop()


def del_part(usr,psswd):
    # print("Enter the following details of part")
    # id = input("Part ID : ")
    # update_query = f"DELETE FROM parts_inventory WHERE part_id={id};"
    # return update_query
    part_window = tk.Tk()
    part_window.title("Delete Part")
    part_window.geometry("400x500")
    # Create labels and entry fields for part details
    part_id_label = tk.Label(part_window, text="Part ID:")
    part_id_entry = tk.Entry(part_window)

    def part_to_db(usr,psswd):
        id = part_id_entry.get()
        update_query = f"DELETE FROM parts_inventory WHERE part_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(part_window, text="Delete part", command=lambda:part_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    part_id_label.pack()
    part_id_entry.pack()
    add_button.pack()
    
    part_window.mainloop()

def update_part(usr,psswd):
    part_window = tk.Tk()
    part_window.title("Add part")
    part_window.geometry("400x500")
    # Create labels and entry fields for part details

    part_id_label = tk.Label(part_window, text="Part ID:")
    part_id_entry = tk.Entry(part_window)

    # part_name_label = tk.Label(part_window, text="Part Name:")
    # part_name_entry = tk.Entry(part_window)
    
    # supplier_id_type_label = tk.Label(part_window, text="Engine Type:")
    # supplier_id_type_entry = tk.Entry(part_window)
    
    # employee_id_label = tk.Label(part_window, text="Fuel Type:")
    # employee_id_entry = tk.Entry(part_window)

    qunatity_label = tk.Label(part_window, text="Quantity:")
    qunatity_entry= tk.Entry(part_window)

    # price_label = tk.Label(part_window, text="Design Year:")
    # price_entry = tk.Entry(part_window)

    def part_to_db(usr,psswd):
        id=part_id_entry.get()
        # name = part_name_entry.get()
        # supplier_id=supplier_id_type_entry.get()
        # employee_id = employee_id_entry.get()
        quantity=qunatity_entry.get()
        #price_year=price_entry.get()
        update_query = f"UPDATE parts_inventory SET in_stock_quantity={quantity} WHERE part_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(part_window, text="Update part", command=lambda:part_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    # part_name_label.pack()
    # part_name_label.pack()
    # supplier_id_type_entry.pack()
    # supplier_id_type_entry.pack()
    part_id_entry.pack()
    part_id_label.pack()
    qunatity_entry.pack()
    qunatity_label.pack()
    # price_entry.pack()
    # price_label.pack()
    add_button.pack()
    
    part_window.mainloop()


def update_sale(usr,psswd):
    # sales_id=input("Enter Sales ID: ")
    # status = input("Enter current status: ")
    # update_query=f"UPDATE sales SET status = '{status}' WHERE sales_id = {sales_id};"
    sales_window = tk.Tk()
    sales_window.title("Add sales")
    sales_window.geometry("400x500")
    # Create labels and entry fields for sales details

    sales_id_label = tk.Label(sales_window, text="sales ID:")
    sales_id_entry = tk.Entry(sales_window)

    # sales_name_label = tk.Label(sales_window, text="sales Name:")
    # sales_name_entry = tk.Entry(sales_window)
    
    # supplier_id_type_label = tk.Label(sales_window, text="Engine Type:")
    # supplier_id_type_entry = tk.Entry(sales_window)
    
    # employee_id_label = tk.Label(sales_window, text="Fuel Type:")
    # employee_id_entry = tk.Entry(sales_window)

    status_label = tk.Label(sales_window, text="Status:")
    status_entry= tk.Entry(sales_window)

    # price_label = tk.Label(sales_window, text="Design Year:")
    # price_entry = tk.Entry(sales_window)

    def sales_to_db(usr,psswd):
        id=sales_id_entry.get()
        # name = sales_name_entry.get()
        # supplier_id=supplier_id_type_entry.get()
        # employee_id = employee_id_entry.get()
        status=status_entry.get()
        #price_year=price_entry.get()
        update_query = f"UPDATE sales SET status = '{status}' WHERE sales_id = {id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(sales_window, text="Update sales", command=lambda:sales_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    # sales_name_label.pack()
    # sales_name_label.pack()
    # supplier_id_type_entry.pack()
    # supplier_id_type_entry.pack()
    sales_id_label.pack()
    sales_id_entry.pack()
    status_label.pack()
    status_entry.pack()
    # price_entry.pack()
    # price_label.pack()
    add_button.pack()
    
    sales_window.mainloop()
    

def add_sale(usr,psswd):
    # client_id = input("Enter Client ID: ")
    # emp_id = input("Enter Employee ID: ")
    # price = input("Enter Sales price: ")
    # status = input("Enter current status of the sale: ")
    # date = input("Enter date of Sales : ")
    # veh_id = input("Enter Vegicle ID: ")
    # update_query = "INSERT INTO sales (client_id,employee_id,vehicle_id,sales_date,sales_price,status) VALUES (" + client_id + "," + emp_id + "," +veh_id + ",\'" +date+ "\'," + price + ",\'" +status+ "\');"
    # return update_query
    sales_window = tk.Tk()
    sales_window.title("Add sales")
    sales_window.geometry("400x500")
    # Create labels and entry fields for sales details

    veh_id_label = tk.Label(sales_window, text="Vehicle ID:")
    veh_id_entry = tk.Entry(sales_window)
    
    client_id_type_label = tk.Label(sales_window, text="Client ID:")
    client_id_type_entry = tk.Entry(sales_window)
    
    employee_id_label = tk.Label(sales_window, text="Employee ID:")
    employee_id_entry = tk.Entry(sales_window)

    status_label = tk.Label(sales_window, text="Current status:")
    status_entry= tk.Entry(sales_window)

    price_label = tk.Label(sales_window, text="Sales price:")
    price_entry = tk.Entry(sales_window)

    date_label = tk.Label(sales_window, text="Date of Sales:")
    date_entry = tk.Entry(sales_window)

    def sales_to_db(usr,psswd):
        veh_id = veh_id_entry.get()
        client_id=client_id_type_entry.get()
        emp_id = employee_id_entry.get()
        status=status_entry.get()
        price=price_entry.get()
        date=date_entry.get()
        update_query = "INSERT INTO sales (client_id,employee_id,vehicle_id,sales_date,sales_price,status) VALUES (" + client_id + "," + emp_id + "," +veh_id + ",\'" +date+ "\'," + price + ",\'" +status+ "\');"
        execute(usr,psswd,update_query)

    add_button = tk.Button(sales_window, text="Add sales", command=lambda:sales_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    veh_id_label.pack()
    veh_id_entry.pack()
    client_id_type_label.pack()
    client_id_type_entry.pack()
    employee_id_label.pack()
    employee_id_entry.pack()
    status_label.pack()
    status_entry.pack()
    price_label.pack()
    price_entry.pack()
    date_label.pack()
    date_entry.pack()

    add_button.pack()
    
    sales_window.mainloop()


def del_sale(usr,psswd):
    # print("Enter the following details of the sale")
    # id = input("Sale ID : ")
    # update_query = f"DELETE FROM sales WHERE sales_id={id};"
    # return update_query
    sales_window = tk.Tk()
    sales_window.title("Delete sales")
    sales_window.geometry("400x500")
    # Create labels and entry fields for sales details
    sales_id_label = tk.Label(sales_window, text="Sales ID:")
    sales_id_entry = tk.Entry(sales_window)

    def sales_to_db(usr,psswd):
        id = sales_id_entry.get()
        update_query = f"DELETE FROM sales WHERE sales_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(sales_window, text="Delete sales", command=lambda:sales_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    sales_id_label.pack()
    sales_id_entry.pack()
    add_button.pack()
    
    sales_window.mainloop()

def add_supply(usr,psswd):
    # print("Enter the following details of supplier")
    # name = input("Supplier name : ")
    # company = input("Company : ")
    # email = input("Email : ")
    # update_query = "INSERT INTO supplier (supplier_name,company_name,email) VALUES (\'" + name + "\',\'" + company + "\',\'" + email + "\');"
    # return update_query
    supplier_window = tk.Tk()
    supplier_window.title("Add supplier")
    supplier_window.geometry("400x500")
    # Create labels and entry fields for supplier details
    supplier_name_label = tk.Label(supplier_window, text="Supplier Name:")
    supplier_name_entry = tk.Entry(supplier_window)
    
    company_label = tk.Label(supplier_window, text="Company:")
    company_entry = tk.Entry(supplier_window)
    
    email_label = tk.Label(supplier_window, text="Email:")
    email_entry = tk.Entry(supplier_window)

    def supplier_to_db(usr,psswd):
        name = supplier_name_entry.get()
        company = company_entry.get()
        email = email_entry.get()
        update_query = "INSERT INTO supplier (supplier_name,company_name,email) VALUES (\'" + name + "\',\'" + company + "\',\'" + email + "\');"
        execute(usr,psswd,update_query)

    add_button = tk.Button(supplier_window, text="Add supplier", command=lambda:supplier_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    supplier_name_label.pack()
    supplier_name_entry.pack()
    company_label.pack()
    company_entry.pack()
    email_label.pack()
    email_entry.pack()
    add_button.pack()
    
    supplier_window.mainloop()
def del_supply(usr,psswd):
    # print("Enter the following details of supplier")
    # id = input("Supplier ID : ")
    # update_query = f"DELETE FROM supplier WHERE supplier_id={id};"
    # return update_query
    supplier_window = tk.Tk()
    supplier_window.title("Delete supplier")
    supplier_window.geometry("400x500")
    # Create labels and entry fields for supplier details
    supplier_id_label = tk.Label(supplier_window, text="Supplier ID:")
    supplier_id_entry = tk.Entry(supplier_window)

    def supplier_to_db(usr,psswd):
        id = supplier_id_entry.get()
        update_query = f"DELETE FROM supplier WHERE supplier_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(supplier_window, text="Delete supplier", command=lambda:supplier_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    supplier_id_label.pack()
    supplier_id_entry.pack()
    add_button.pack()
    
    supplier_window.mainloop()

def update_supply(usr,psswd):
    # print("Enter the supplier ID and new details of supplier")
    # id=input("Supplier ID : ")
    # name = input("Supplier name : ")
    # company = input("Company : ")
    # email = input("Email : ")
    # update_query =f"UPDATE supplier SET supplier_name='{name}' company_name='{company}' email='{email}' WHERE supplier_id={id};"
    # return update_query
    supplier_window = tk.Tk()
    supplier_window.title("Update supplier")
    supplier_window.geometry("400x500")
    # Create labels and entry fields for supplier details

    supplier_id_label = tk.Label(supplier_window, text="supplier ID:")
    supplier_id_entry = tk.Entry(supplier_window)

    supplier_name_label = tk.Label(supplier_window, text="supplier Name:")
    supplier_name_entry = tk.Entry(supplier_window)
    
    company_label = tk.Label(supplier_window, text="Company:")
    company_entry = tk.Entry(supplier_window)
    
    email_label = tk.Label(supplier_window, text="Email:")
    email_entry = tk.Entry(supplier_window)

    def supplier_to_db(usr,psswd):
        name = supplier_name_entry.get()
        company = company_entry.get()
        email = email_entry.get()
        id=supplier_id_entry.get()
        update_query = f"UPDATE supplier SET supplier_name='{name}' ,company_name='{company}' ,email='{email}' WHERE supplier_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(supplier_window, text="Update supplier", command=lambda:supplier_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    supplier_id_label.pack()
    supplier_id_entry.pack()
    supplier_name_label.pack()
    supplier_name_entry.pack()
    company_label.pack()
    company_entry.pack()
    email_label.pack()
    email_entry.pack()
    add_button.pack()
    
    supplier_window.mainloop()
    

def add_veh(usr,psswd):
    # print("Enter the following details of vehicle")
    # id = input("Model ID : ")
    # color = input("Color : ")
    # year = input("Year : ")
    # price = input("Price : ")
    # update_query = "INSERT INTO vehicle (model_id,color,year,price) VALUES (" + id + ",\'" + color    + "\'," + year + "," + price + ");"
    # return update_query
    vehicle_window = tk.Tk()
    vehicle_window.title("Add vehicle")
    vehicle_window.geometry("400x500")
    # Create labels and entry fields for vehicle details

    model_id_label = tk.Label(vehicle_window, text="Model ID:")
    model_id_entry = tk.Entry(vehicle_window)
    
    color_label = tk.Label(vehicle_window, text="color:")
    color_entry = tk.Entry(vehicle_window)
    
    year_label = tk.Label(vehicle_window, text="year:")
    year_entry = tk.Entry(vehicle_window)

    price_label = tk.Label(vehicle_window, text="Price:")
    price_entry = tk.Entry(vehicle_window)

    def vehicle_to_db(usr,psswd):
        id=model_id_entry.get()
        color=color_entry.get()
        year = year_entry.get()
        price=price_entry.get()
        update_query = "INSERT INTO vehicle (model_id,color,year,price) VALUES (" + id + ",\'" + color    + "\'," + year + "," + price + ");"
        execute(usr,psswd,update_query)

    add_button = tk.Button(vehicle_window, text="Add vehicle", command=lambda:vehicle_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    model_id_label.pack()
    model_id_entry.pack()
    color_label.pack()
    color_entry.pack()
    year_label.pack()
    year_entry.pack()
    price_label.pack()
    price_entry.pack()
    add_button.pack()
    
    vehicle_window.mainloop()

def del_veh(usr,psswd):
    # print("Enter the following details of vehicle")
    # id = input("Vehicle ID : ")
    # update_query = f"DELETE FROM vehicle WHERE vehicle_id={id};"
    # return update_query
    vehicle_window = tk.Tk()
    vehicle_window.title("Delete vehicle")
    vehicle_window.geometry("400x500")
    # Create labels and entry fields for vehicle details
    vehicle_id_label = tk.Label(vehicle_window, text="vehicle ID:")
    vehicle_id_entry = tk.Entry(vehicle_window)

    def vehicle_to_db(usr,psswd):
        id = vehicle_id_entry.get()
        update_query = f"DELETE FROM vehicle WHERE vehicle_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(vehicle_window, text="Delete vehicle", command=lambda:vehicle_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    vehicle_id_label.pack()
    vehicle_id_entry.pack()
    add_button.pack()
    
    vehicle_window.mainloop()

def update_veh(usr,psswd):
    # print("Enter the vehicle ID and following new details of vehicle")
    # veh=input("Vehicle ID : ")
    # id = input("Model ID : ")
    # color = input("Color : ")
    # year = input("Year : ")
    # price = input("Price : ")
    # update_query = f"UPDATE vehicle SET model_id={id} color='{color}' year={year} price={price} WHERE vehicle_id={veh} ;"
    # return update_query
    vehicle_window = tk.Tk()
    vehicle_window.title("Add vehicle")
    vehicle_window.geometry("400x500")
    # Create labels and entry fields for vehicle details
    veh_id_label=tk.Label(vehicle_window,text="Vehicle ID")
    veh_id_entry = tk.Entry(vehicle_window)

    model_id_label = tk.Label(vehicle_window, text="Model ID:")
    model_id_entry = tk.Entry(vehicle_window)
    
    color_label = tk.Label(vehicle_window, text="color:")
    color_entry = tk.Entry(vehicle_window)
    
    year_label = tk.Label(vehicle_window, text="year:")
    year_entry = tk.Entry(vehicle_window)

    price_label = tk.Label(vehicle_window, text="Price:")
    price_entry = tk.Entry(vehicle_window)

    def vehicle_to_db(usr,psswd):
        veh=veh_id_entry.get()
        id=model_id_entry.get()
        color=color_entry.get()
        year = year_entry.get()
        price=price_entry.get()
        update_query = f"UPDATE vehicle SET model_id={id} ,color='{color}' ,year={year} ,price={price} WHERE vehicle_id={veh} ;"
        execute(usr,psswd,update_query)

    add_button = tk.Button(vehicle_window, text="Update vehicle", command=lambda:vehicle_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    veh_id_label.pack()
    veh_id_entry.pack()
    model_id_label.pack()
    model_id_entry.pack()
    color_label.pack()
    color_entry.pack()
    year_label.pack()
    year_entry.pack()
    price_label.pack()
    price_entry.pack()
    add_button.pack()
    
    vehicle_window.mainloop()


def add_factory(usr,psswd):
    # print("Enter the following details of worker")
    # id = input("Employee ID : ")
    # veh = input("Vehicle ID : ")
    # work = input("Work description : ")
    # update_query = "INSERT INTO factory (employee_id,vehicle_id,work) VALUES (" + id + "," + veh + ",\'" + work + "\');"
    # return update_query
    factory_window = tk.Tk()
    factory_window.title("Add factory")
    factory_window.geometry("400x500")
    # Create labels and entry fields for factory details
    factory_id_label = tk.Label(factory_window, text="Employee ID:")
    factory_id_entry = tk.Entry(factory_window)
    
    veh_id_label = tk.Label(factory_window, text="Vehicle ID:")
    veh_id_entry = tk.Entry(factory_window)
    
    work_label = tk.Label(factory_window, text="Work description:")
    work_entry = tk.Entry(factory_window)

    def factory_to_db(usr,psswd):
        id = factory_id_entry.get()
        veh = veh_id_entry.get()
        work = work_entry.get()
        update_query = "INSERT INTO factory (employee_id,vehicle_id,work) VALUES (" + id + "," + veh + ",\'" + work + "\');"
        execute(usr,psswd,update_query)

    add_button = tk.Button(factory_window, text="Add factory", command=lambda:factory_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    factory_id_label.pack()
    factory_id_entry.pack()
    veh_id_label.pack()
    veh_id_entry.pack()
    work_label.pack()
    work_entry.pack()
    add_button.pack()
    
    factory_window.mainloop()

def update_factory(usr,psswd):
    # id = input("Enter Employee ID : ")
    # veh=input("Enter the Vehicle ID")
    # work = input("Enter updated work : ")
    # update_query=f"UPDATE factory SET work='{work}' WHERE employee_id={id} AND vehicle_id={veh};"
    # return update_query
    factory_window = tk.Tk()
    factory_window.title("Add factory")
    factory_window.geometry("400x500")
    # Create labels and entry fields for factory details
    factory_id_label = tk.Label(factory_window, text="Employee ID:")
    factory_id_entry = tk.Entry(factory_window)
    
    veh_id_label = tk.Label(factory_window, text="Vehicle ID:")
    veh_id_entry = tk.Entry(factory_window)
    
    work_label = tk.Label(factory_window, text="Updated Work description:")
    work_entry = tk.Entry(factory_window)

    def factory_to_db(usr,psswd):
        id = factory_id_entry.get()
        veh = veh_id_entry.get()
        work = work_entry.get()
        update_query = f"UPDATE factory SET work='{work}' WHERE employee_id={id} AND vehicle_id={veh};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(factory_window, text="Update factory", command=lambda:factory_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    factory_id_label.pack()
    factory_id_entry.pack()
    veh_id_label.pack()
    veh_id_entry.pack()
    work_label.pack()
    work_entry.pack()
    add_button.pack()
    
    factory_window.mainloop()

def add_dept(usr,psswd):
    # print("Enter the following details of Department")
    # name=input("Department name : ")
    # update_query = "INSERT INTO department (department_name) VALUES (\'" + name + "\');"
    # return update_query
    dept_window = tk.Tk()
    dept_window.title("Add Department")
    dept_window.geometry("400x500")

    dept_name_label = tk.Label(dept_window, text="Department Name:")
    dept_name_entry = tk.Entry(dept_window)

    def dept_to_db(usr,psswd):
        name=dept_name_entry.get()
        update_query = "INSERT INTO department (department_name) VALUES (\'" + name + "\');"
        execute(usr,psswd,update_query)

    add_button = tk.Button(dept_window
    , text="Update Department", command=lambda:dept_to_db(usr,psswd))
    dept_name_label.pack()
    dept_name_entry.pack()
    add_button.pack()
    
    dept_window.mainloop()


def del_dept(usr,psswd):
    # print("Enter the following details of Department")
    # id = input("Department ID : ")
    # update_query = f"DELETE FROM department WHERE vehicle_id={id};"
    # return update_query
    dept_window = tk.Tk()
    dept_window.title("Delete Department")
    dept_window.geometry("400x500")
    # Create labels and entry fields for dept details
    dept_id_label = tk.Label(dept_window, text="dept ID:")
    dept_id_entry = tk.Entry(dept_window)

    def dept_to_db(usr,psswd):
        id = dept_id_entry.get()
        update_query = f"DELETE FROM department WHERE department_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(dept_window, text="Delete department", command=lambda:dept_to_db(usr,psswd))
    
    # Pack labels, entry fields, and the button
    dept_id_label.pack()
    dept_id_entry.pack()
    add_button.pack()
    
    dept_window.mainloop()

def update_dept(usr,psswd):
    # print("Enter the department ID and following new details of Department")
    # id=input("Department ID : ")
    # name=input("Department name : ")
    # update_query = f"UPDATE department SET department_name='{name}' WHERE department_id={id};"
    # return update_query
    dept_window = tk.Tk()
    dept_window.title("Add Department")
    dept_window.geometry("400x500")

    dept_id_label = tk.Label(dept_window, text="Department ID:")
    dept_id_entry = tk.Entry(dept_window)

    dept_name_label = tk.Label(dept_window, text="Department Name:")
    dept_name_entry = tk.Entry(dept_window)

    def dept_to_db(usr,psswd):
        id=dept_id_entry.get()
        name=dept_name_entry.get()
        update_query = f"UPDATE department SET department_name='{name}' WHERE department_id={id};"
        execute(usr,psswd,update_query)

    add_button = tk.Button(dept_window, text="Update Department", command=lambda:dept_to_db(usr,psswd))
    dept_id_label.pack()
    dept_id_entry.pack()
    dept_name_label.pack()
    dept_name_entry.pack()
    add_button.pack()
    
    dept_window.mainloop()


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
        root.geometry("300x300")
        root.iconbitmap('./blueprints/tata.ico')
        display(root,usr,psswd)
        root.mainloop()
    else:
        print("INVALID CREDENTIALS")
        messagebox.showerror("TATA Motors Database", "INVALID CREDENTIALS")



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: init.py <username> <password>")
        messagebox.showinfo("TATA Motors Database", "FILL THE FIELDS")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        main(username, password)