import psycopg2

def employee():
    sql_query = """CREATE USER employee with password '12345';
                    GRANT SELECT,INSERT,UPDATE,DELETE ON sales, sales_sales_id_seq,client, client_client_id_seq,parts_inventory,parts_inventory_part_id_seq, vehicle,vehicle_vehicle_id_seq,model,model_model_id_seq,factory, supplier_supplier_id_seq,supplier TO employee;"""
    return sql_query

def boss():
    sql_query = """CREATE USER boss with password '12345';
                    GRANT SELECT, INSERT, UPDATE, DELETE ON employee, sales, sales_sales_id_seq,client, client_client_id_seq,parts_inventory,parts_inventory_part_id_seq, vehicle,vehicle_vehicle_id_seq,model,model_model_id_seq,factory, supplier_supplier_id_seq,supplier TO boss;"""
    return sql_query


def main(usr,psswd):
    try:
        with psycopg2.connect(database='tatadb',
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432) as connection:

            with connection.cursor() as cursor:
                cursor.execute(employee())
                cursor.execute(boss())
                connection.commit()
                print("ALL ROLES CREATED")
            cursor.close()
        connection.close()
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")
        
    except psycopg2.Error as e:
        print("!!!!!!!!!!!!!CREATE ROLES UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        connection.rollback()

# main("postgres", "2202")