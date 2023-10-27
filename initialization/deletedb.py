import psycopg2
import sys
from tkinter import messagebox

def main(usr, psswd): 
    try:
        connection = psycopg2.connect(database="postgres",
                                host="localhost",
                                user=usr,
                                password=psswd,
                                port=5432)
        connection.autocommit = True
        cursor = connection.cursor()

        sql_query = ''' DROP database tatadb '''    
        cursor.execute(sql_query)
        sql_query = ''' DROP USER IF EXISTS employee'''
        cursor.execute(sql_query)
        sql_query = ''' DROP USER IF EXISTS boss'''
        cursor.execute(sql_query)
        # print("DATABASE DELETED")
        messagebox.showinfo("TATA Motors Database", "DATABASE DELETED SUCCESSFULLY")
        connection.close()

    except psycopg2.OperationalError as e:
        # print("INVALID CREDENTIALS")
        messagebox.showerror("TATA Motors Database", "INVALID CREDENTIALS\n\n{}".format(e))
        exit()
    except psycopg2.Error as e:
        # print("!!!!!!!!!!!!!DELETE DATABASE UNSUCCESSFUL!!!!!!!!!!!!!")
        print(e)
        messagebox.showerror("TATA Motors Database", e)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: init.py <username> <password>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        main(username, password)

# main("postgres","2202")