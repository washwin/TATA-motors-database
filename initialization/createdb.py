import psycopg2

def main(usr, psswd): 
    try:
        connection = psycopg2.connect(database="postgres",
                                host="localhost",
                                user=usr,
                                password=psswd,
                                port=5432)
        connection.autocommit = True
        cursor = connection.cursor()

        sql_query = ''' CREATE database tatadb ''';    
        cursor.execute(sql_query)
        print("DATABASE CREATED")
        connection.close()
        
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")
    except psycopg2.Error as e:
        print("!!!!!!!!!!!!!CREATE DATABASE UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)

        
# main("postgres","2202")