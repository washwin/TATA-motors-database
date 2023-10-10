from initialization import deletedb
from initialization import createdb
from initialization import tables
from initialization import populate
from initialization import roles

def main():
    usr = input("Enter username (usually postgres) : ")
    psswd = input("Enter password : ")

    deletedb.main(usr,psswd)
    createdb.main(usr,psswd)
    tables.main(usr,psswd)
    populate.main(usr,psswd)
    roles.main(usr,psswd)
    print("INITIALIZATION SUCCESSFUL!")
    
main()
