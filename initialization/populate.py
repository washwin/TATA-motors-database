import psycopg2
import csv

def main(usr,psswd):
    try:
        with psycopg2.connect(database='tatadb',
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432) as connection:

            with connection.cursor() as cursor:
                with open("..\sample_data\client.csv", "r") as ip:
                    csv_reader = csv.reader(ip)
                    for record in csv_reader:
                        sql_query = "INSERT INTO client (client_name,company_name,email) VALUES (\'" + record[0] + "\',\'" + record[1] + "\',\'" + record[2] + "\');"
                        cursor.execute(sql_query)
                        connection.commit()

                with open("..\sample_data\department.csv", "r") as ip:
                    csv_reader = csv.reader(ip)
                    for record in csv_reader:
                        sql_query = "INSERT INTO department (department_name) VALUES (\'" + record[0] + "\');"
                        cursor.execute(sql_query)
                        connection.commit()
                
                with open("..\sample_data\employee.csv", "r") as ip:
                    csv_reader = csv.reader(ip)
                    for record in csv_reader:
                        sql_query = "INSERT INTO employee (first_name,last_name,email,phone_no,address,designation,salary,department_id) VALUES (\'" + record[0] + "\',\'" + record[1] + "\',\'" + record[2] + "\',\'" + record[3] + "\',\'" + record[4] + "\',\'" + record[5] + "\'," + record[6] + "," + record[7] + ");"
                        cursor.execute(sql_query)
                        connection.commit()
                
                with open("..\sample_data\supplier.csv", "r") as ip:
                    csv_reader = csv.reader(ip)
                    for record in csv_reader:
                        sql_query = "INSERT INTO supplier (supplier_name,company_name,email) VALUES (\'" + record[0] + "\',\'" + record[1] + "\',\'" + record[2] + "\');"
                        cursor.execute(sql_query)
                        connection.commit()

                with open("..\sample_data\model.csv", "r") as ip:
                    csv_reader = csv.reader(ip)
                    for record in csv_reader:
                        sql_query = "INSERT INTO model (model_name,design_year,engine_type,fuel_type,dimensions,zero_to_sixty,km_per_litres) VALUES (\'" + record[0] + "\'," + record[1] + ",\'" + record[2] + "\',\'" + record[3] + "\',\'" + record[4] + "\'," + record[5] + "," + record[6] + ");"
                        cursor.execute(sql_query)
                        connection.commit()
                    
                with open("..\sample_data\Vehicle.csv", "r") as ip:
                    csv_reader = csv.reader(ip)
                    for record in csv_reader:
                        sql_query = "INSERT INTO vehicle (model_id,color,year,price) VALUES (" + record[0] + ",\'" + record[1] + "\'," + record[2] + "," + record[3] + ");"
                        cursor.execute(sql_query)
                        connection.commit()

                with open("..\sample_data\sales.csv", "r") as ip:
                    csv_reader = csv.reader(ip)
                    for record in csv_reader:
                        sql_query = "INSERT INTO sales (client_id,employee_id,vehicle_id,sales_date,sales_price,status) VALUES (" + record[0] + "," + record[1] + "," + record[2] + ",\'" + record[3] + "\'," + record[4] + ",\'" + record[5] + "\');"
                        cursor.execute(sql_query)
                        connection.commit()

                with open("..\sample_data\parts_inventory.csv", "r") as ip:
                    csv_reader = csv.reader(ip)
                    for record in csv_reader:
                        sql_query = "INSERT INTO parts_inventory (part_name,supplier_id,employee_id,in_stock_quantity,unit_price) VALUES (\'" + record[0] + "\'," + record[1] + "," + record[2] + "," + record[3] + "," + record[4] + ");"
                        cursor.execute(sql_query)
                        connection.commit()

                with open("..\sample_data\Factory.csv", "r") as ip:
                    csv_reader = csv.reader(ip)
                    for record in csv_reader:
                        sql_query = "INSERT INTO factory (employee_id,vehicle_id,work) VALUES (" + record[0] + "," + record[1] + ",\'" + record[2] + "\');"
                        cursor.execute(sql_query)
                        connection.commit()
                print("ALL TABLES POPULATED")
                cursor.close()
        connection.close()
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")
        print(e)
    except psycopg2.Error as e:
        print("!!!!!!!!!!!!!POPULATE TABLE UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        connection.rollback()
        

# main("postgres","2202")