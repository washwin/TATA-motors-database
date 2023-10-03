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
        sql_query = ''' DROP database tatadb ''';    
        cursor.execute(sql_query)
        print("DATABASE DELETED")
    except psycopg2.Error as e:
        print(e)
    finally:
        connection.close()

main("postgres","2202")