import psycopg2

def main(usr, psswd): 
    connection = psycopg2.connect(database="postgres",
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432)
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        sql_query = ''' CREATE database tatadb ''';    
        cursor.execute(sql_query)
        print("DATABASE CREATED")
    except psycopg2.Error as e:
        print("!!!!!!!!!!!!!CREATE DATABASE UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
    finally:
        connection.close()

main("postgres","2202")