import psycopg2
from tkinter import messagebox

def HR():
    sql_query = """CREATE USER hr with password '12345';
                    GRANT SELECT,INSERT,UPDATE,DELETE ON employee,department,department_department_id_seq,employee_employee_id_seq TO hr;"""
    return sql_query

def PR():
    sql_query = """CREATE USER pr with password '12345';
                    GRANT SELECT,INSERT,UPDATE,DELETE ON sales, sales_sales_id_seq,client, client_client_id_seq TO pr;"""
    return sql_query

def supplyChain():
    sql_query = """CREATE USER supply_chain with password '12345';
                    GRANT SELECT,INSERT,UPDATE,DELETE ON parts_inventory,parts_inventory_part_id_seq,supplier_supplier_id_seq,supplier TO supply_chain;"""
    return sql_query

def manufacturing():
    sql_query = """CREATE USER manufacturing with password '12345';
                    GRANT SELECT,INSERT,UPDATE,DELETE ON vehicle,vehicle_vehicle_id_seq,model,model_model_id_seq,factory TO manufacturing;"""
    return sql_query

def boss():
    sql_query = """CREATE USER boss with password '12345';
                    GRANT SELECT, INSERT, UPDATE, DELETE ON employee,department,department_department_id_seq,employee_employee_id_seq, sales, sales_sales_id_seq,client, client_client_id_seq,parts_inventory,parts_inventory_part_id_seq, vehicle,vehicle_vehicle_id_seq,model,model_model_id_seq,factory, supplier_supplier_id_seq,supplier TO boss;"""
    return sql_query


def main(usr,psswd):
    try:
        with psycopg2.connect(database='tatadb',
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432) as connection:

            with connection.cursor() as cursor:
                cursor.execute(HR())
                cursor.execute(PR())
                cursor.execute(supplyChain())
                cursor.execute(boss())
                cursor.execute(manufacturing())
                connection.commit()
                print("ALL ROLES CREATED")
                # messagebox.showinfo("TATA Motors Database","ALL ROLES CREATED")
            cursor.close()
        connection.close()
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")
        messagebox.showinfo("TATA Motors Database","INVALID CREDENTIALS")
        exit()
        
    except psycopg2.Error as e:
        print("!!!!!!!!!!!!!CREATE ROLES UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        connection.rollback()
        messagebox.showerror("TATA Motors Database", e)
        exit()

#main("postgres", "123456")