import psycopg2

def main(usr, psswd): 
    connection = psycopg2.connect(database="postgres",
                            host="localhost",
                            user=usr,
                            password=psswd,
                            port=5432)
    cursor = connection.cursor()
    sql_query = """SELECT FROM pg_database WHERE datname = 'tatadb'"""
    cursor.execute(sql_query)
    # print(len(cursor.fetchall()))
    l = len(cursor.fetchall())
    if(l==0):
        sql_query = "CREATE DATABASE tatadb"
        sql_query = """SELECT 'CREATE DATABASE tatadb' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'tatadb')"""
        cursor.execute(sql_query)
        print("DATABASE CREATED")
    else:
        sql_query = "SELECT 'CREATE DATABASE tatadb' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'tatadb')"
        cursor.execute(sql_query)
        print("DATABASE ALREADY EXISTS")              
    cursor.close()
    connection.close()

main("postgres","2202")