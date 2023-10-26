import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import getpass
from initialization import deletedb
from initialization import createdb
from initialization import tables
from initialization import populate
from initialization import roles


def main():
    usr = input("Enter username (usually postgres) : ")
    psswd = getpass.getpass("Enter password : ")

    deletedb.main(usr,psswd)
    createdb.main(usr,psswd)
    tables.main(usr,psswd)
    populate.main(usr,psswd)
    roles.main(usr,psswd)
    
# main()
