# TATA-motors-database
* We have created a model database for TATA Motors Dharwad
* Run python gui.py in terminal to open interface
* Interface can:
* * create new database
  * update database
  * view database
  * delete database
* To initialize the database to your postgres admin run init.py using: python init.py
* Then enter the appropriate credentials
* This will create a new database called tatadb and fill it with the sample data given
* NOTE: running init.py also deletes existing tatadb if present
* Also, two users namely employee and boss have been created with restricted database access to them
* Run view.py to view tables present in the database, using: python view.py
* Run update.py to update rows in tables, using: python update.py
