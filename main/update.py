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
    print("(8)Factory")

def type():
    print("SELECT TYPE OF UPDATION:")
    print("(1)Add")
    print("(2)Delete")
    print("(3)Update")

def update(usr,psswd):
    try:
        with psycopg2.connect(database='tatadb',
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432) as connection:
            display()
            i = input("Choose index : ")
            type()
            j=input("Choose the type of update : ")
            update_query = ""
            if(i=='1'):
                if(j=='1'):
                    update_query = add_client()
                elif(j=='2'):
                    update_query = del_client()
                else:
                    print("NOT AVAILABALE OPTION")

            elif(i=='2'):
                if(j=='1'):
                    update_query = add_employee()
                elif(j=='2'):
                    update_query = del_employee()
                else:
                    update_query=update_employee()

            elif(i=='3'):
                if(j=='1'):
                    update_query = add_model()
                elif(j=='2'):
                    update_query = del_model()
                else:
                    print("NOT AVAILABALE OPTION")

            elif(i=='4'):
                if(j=='1'):
                    update_query = add_part()
                elif(j=='2'):
                    update_query = del_part()
                else:
                    update_query=update_part()

            elif(i=='5'):
                if(j=='1'):
                    update_query = add_sale()
                elif(j=='3'):
                    update_query = update_sale()
                else:
                    print("NOT AVAILABALE OPTION")

            elif(i=='6'):
                if(j=='1'):
                    update_query = add_supply()
                elif(j=='2'):
                    update_query = del_supply()
                else:
                    print("NOT AVAILABALE OPTION")

            elif(i=='7'):
                if(j=='1'):
                    update_query = add_veh()
                elif(j=='2'):
                    update_query = del_veh()
                else:
                    print("NOT AVAILABALE OPTION")

            elif(i=='8'):
                if(j=='1'):
                    update_query = add_worker()
                elif(j=='2'):
                    update_query = del_veh()
                else:
                    print("NOT AVAILABALE OPTION")



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

def add_client():
    print("Enter the following details of client")
    name = input("Client name : ")
    company = input("Company : ")
    email = input("Email : ")
    update_query = "INSERT INTO client (client_name,company_name,email) VALUES (\'" + name + "\',\'" + company + "\',\'" + email + "\');"
    return update_query

def del_client():
    print("Enter the following details of client")
    id = input("Client ID : ")
    update_query = f"DELETE FROM client WHERE client_id={id};"
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
    update_query=f"UPDTAE employee SET designation='{role}' salary={salary} WHERE employee_id={id};"
    return update_query

def add_model():
    print("Enter the following details of model")
    name = input("Model name : ")
    design_year = input("Desugn Year : ")
    fuel_typel = input("Fuel Type : ")
    dimensions= input("Dimensions : ")
    zero_to_sixty= input("Zero to Sixty : ")
    km_per_litres= input("Kilometers per Litre : ")
    update_query = "INSERT INTO model (model_name,design_year,engine_type,fuel_type,dimensions,zero_to_sixty,km_per_litres) VALUES (\'" + name + "\'," + design_year + ",\'" + fuel_typel + "\',\'" + dimensions + "\'," + zero_to_sixty + "," + km_per_litres + ");"
    return update_query

def del_model():
    print("Enter the following details of model")
    id = input("Model ID : ")
    update_query = f"DELETE FROM model WHERE model_id={id};"
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
    update_query=f"UPDTAE parts_inventory SET in_stock_quantity={quantity} WHERE part_id={id};"
    return update_query


def update_sale():
    sales_id=input("Enter Sales ID: ")
    status = input("Enter current status: ")
    update_query=f"UPDATE sales SET status = {status} WHERE sales_id = {sales_id};"
    

def add_sale():
    client_id = input("Enter Client ID: ")
    emp_id = input("Enter Employee ID: ")
    price = input("Enter Sales price: ")
    status = input("Enter current status of the sale: ")
    date = input("Enter date of Sales : ")
    veh_id = input("Enter Vegicle ID: ")
    update_query = "INSERT INTO sales (client_id,employee_id,vehicle_id,sales_date,sales_price,status) VALUES (" + client_id + "," + emp_id + "," +veh_id + ",\'" +date+ "\'," + price + ",\'" +status+ "\');"
    return update_query

def add_supply():
    print("Enter the following details of client")
    name = input("Supplier name : ")
    company = input("Company : ")
    email = input("Email : ")
    update_query = "INSERT INTO supplier (supplier_name,company_name,email) VALUES (\'" + name + "\',\'" + company + "\',\'" + email + "\');"
    return update_query

def del_supply():
    print("Enter the following details of client")
    id = input("Supplier ID : ")
    update_query = f"DELETE FROM supplier WHERE supplier_id={id};"
    return update_query

def add_veh():
    print("Enter the following details of vehicle")
    id = input("Model ID : ")
    color = input("Color : ")
    year = input("Year : ")
    price = input("Price : ")
    update_query = "INSERT INTO vehicle (model_id,color,year,price) VALUES (" + id + ",\'" + color    + "\',\'" + email + "\');"
    return update_query

def del_veh():
    print("Enter the following details of vehicle")
    id = input("Vehicle ID : ")
    update_query = f"DELETE FROM vehicle WHERE vehicle_id={id};"
    return update_query


def add_worker():
    print("Enter the following details of worker")
    id = input("Employee ID : ")
    veh = input("Vehicle ID : ")
    work = input("Work description : ")
    update_query = "INSERT INTO factory (employee_id,vehicle_id,work) VALUES (" + id + "," + veh + ",\'" + work + "\');"
    return update_query

def are_credentials_valid(usr, psswd):
    try:
        with psycopg2.connect(database='tatadb', host="localhost", user=usr, password=psswd, port=5432):
            return True
    except psycopg2.OperationalError:
        return False

def main():
    usr = input("Enter username (usually postgres) : ")
    psswd = getpass.getpass("Enter password : ")
    # update(usr,psswd)
    if are_credentials_valid(usr, psswd):
        update(usr, psswd)
    else:
        print("INVALID CREDENTIALS")



main()