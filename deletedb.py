import psycopg2

def main(usr, psswd): 
    connection = psycopg2.connect(
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432)
    cursor = connection.cursor()
    sql_query = "SELECT FROM pg_database WHERE datname = 'tatadb'"
    cursor.execute(sql_query)
    if(len(cursor.fetchall())==0):
        print("DATABASE DOES NOT EXIST")              
    else:
        sql_query = "DROP DATABASE tatadb"
        cursor.execute(sql_query)
        print("DATABASE DELETED")
    cursor.close()
    connection.close()

main("postgres","2202")