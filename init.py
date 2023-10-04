from initialization import deletedb
from initialization import createdb
from initialization import tables
from initialization import populate


deletedb.main("postgres","2202")
createdb.main("postgres","2202")
tables.main("postgres","2202")
populate.main("postgres","2202")