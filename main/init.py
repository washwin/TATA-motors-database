import sys
import os
from tkinter import messagebox
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import getpass
from initialization import deletedb
from initialization import createdb
from initialization import tables
from initialization import populate
from initialization import roles


def main(usr,psswd):
    # usr = input("Enter username (usually postgres) : ")
    # psswd = getpass.getpass("Enter password : ")

    deletedb.main(usr,psswd)
    createdb.main(usr,psswd)
    tables.main(usr,psswd)
    populate.main(usr,psswd)
    roles.main(usr,psswd)
    
    messagebox.showinfo("TATA Motors Database", "NEW DATABASE CREATED")
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: init.py <username> <password>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        main(username, password)