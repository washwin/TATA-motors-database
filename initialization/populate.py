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
                with open(".\sample_data\client.csv", "r") as ip:
                    csv_reader = csv.reader(ip)
                    for record in csv_reader:
                        sql_query = "INSERT INTO client VALUES (" + record[0] + ",\'" + record[1] + "\',\'" + record[2] + "\',\'" + record[3] + "\',\'" + record[4] + "\',\'" + record[5] + "\');"
                        cursor.execute(sql_query)
                        connection.commit()
                print("ALL TABLES POPULATED")
                cursor.close()
        connection.close()
    except psycopg2.OperationalError as e:
        print("INVALID CREDENTIALS")
    except psycopg2.Error as e:
        print("!!!!!!!!!!!!!POPULATE TABLE UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        connection.rollback()
        

# main("postgres","2202")