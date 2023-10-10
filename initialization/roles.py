import psycopg2

def client():
    sql_query = """CREATE USER client with password '12345';"""
    return sql_query

def employee():
    sql_query = """CREATE USER employee with password '12345';"""
    return sql_query

def boss():
    sql_query = """CREATE USER boss with password '12345';"""
    return sql_query


def main(usr,psswd):
    try:
        with psycopg2.connect(database='tatadb',
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432) as connection:

            with connection.cursor() as cursor:  
                cursor.execute(client())
                cursor.execute(employee())
                cursor.execute(boss())
                connection.commit()
                print("ALL ROLES CREATED")
                
    except psycopg2.Error as e:
        print("!!!!!!!!!!!!!CREATE ROLES UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

main("postgres", "2202")