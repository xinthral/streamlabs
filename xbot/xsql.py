"""
SLCB runs on IronPython, those cheeky whores:
https://stackoverflow.com/a/66794423/13825434
"""
try:
    import sqlite3
except:
    import clr
    clr.AddReference("IronPython.SQLite.dll")
    clr.AddReference("IronPython.Modules.dll")
finally:
    import re
    import sqlite3

class Database:
    """ Static Class Scope Variables """
    _delim = ';::;'
    # _library = 'library.db'
    _library = 'Services/Scripts/xbot/library.db'
    _tables = ['facts', 'fortunes', 'jokes', 'phrases', 'rather']

    @staticmethod
    def create_connection(db_file=_library):
        """ Establish Connection to database object and return connection object """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Exception as e:
            raise(e)
        return(conn)

    @staticmethod
    def queryTableAll(tbl_name=_tables[0]):
        """ Query all items from a specific database in the database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute("SELECT * FROM {}".format(tbl_name))
        rows = c.fetchall()
        con.close()
        return(rows)

    @staticmethod
    def queryTableID(item_id=0, tbl_name=_tables[0]):
        """ Query a specific items ID from a specific database in the database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute("SELECT * FROM {} WHERE pid={}".format(tbl_name, item_id))
        item = c.fetchone()
        con.close()
        return(item)

    @staticmethod
    def getTableHeaders(tbl_name=_tables[0]):
        """ Query Headers for specific table in database object """
        return([ele[1] for ele in Database.showTableSchema(tbl_name)])

    @staticmethod
    def insert(payload, tbl_name=_tables[0]):
        if len(payload[0].split(Database._delim)) < 1:
            print('Empty Payload')
            return(False)

        con = Database.create_connection()
        c = con.cursor()
        columns = Database.getTableHeaders(tbl_name)
        columns = ', '.join(columns)
        elements = [str(Database.getTableCount(tbl_name))] + list(payload)
        # Yeah, this next line is gross
        elements = ', '.join([("\"{}\"".format(str(ele).encode('UTF-8').replace('"', r"\'"))) for ele in elements])
        sqlQuery = "INSERT INTO {} ({}) VALUES ({})".format(tbl_name, columns, elements)
        c.execute(sqlQuery)
        con.commit()
        con.close()
        return(True)

    @staticmethod
    def insertFact(payload):
        """ Insert fact payload into database object (wrapper) """
        #payload: ['input text', 'category', blocked: 0/1]
        return(Database.insert(payload, 'facts'))

    @staticmethod
    def insertFortune(payload):
        """ Insert fact payload into database object (wrapper) """
        #payload: ['input text', 'category', blocked: 0/1]
        return(Database.insert(payload, 'fortunes'))

    @staticmethod
    def insertJoke(payload):
        """ Inserts joke payload into database object (wrapper) """
        #payload: ['input text', 'category', blocked: 0/1]
        return(Database.insert(payload, 'jokes'))

    @staticmethod
    def insertPhrase(payload):
        """ Inserts phrase payload into database object (wrapper) """
        #payload: ['input text', 'category', blocked: 0/1]
        return(Database.insert(payload, 'phrases'))

    @staticmethod
    def insertRather(payload):
        """ Inserts would you rather payload into database object (wrapper) """
        #payload: ['input text', 'category', blocked: 0/1]
        return(Database.insert(payload, 'rather'))

    @staticmethod
    def updateVisibility(payload):
        """ Update visibility value for a record """
        if len(payload[0].split(Database._delim)) < 1:
            print('Empty Payload')
            return(False)

        # table, column, value, pid
        table, column, value, pid = payload
        table.replace('"', '""')
        column.replace('"', '""')
        con = Database.create_connection()
        c = con.cursor()
        c.execute('UPDATE "{}" SET "{}" = {} WHERE pid = {}'.format(table, column, value, pid))
        con.commit()
        con.close()
        return(True)

    @staticmethod
    def showTables():
        """ Query table names from database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type=\'table\'")
        rows = c.fetchall()
        con.close()
        return(rows)

    @staticmethod
    def showTableSchema(tbl_name=_tables[0]):
        """ Query Schema for specific table in database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute("PRAGMA table_info({})".format(tbl_name))
        rows = c.fetchall()
        con.close()
        return(rows)

    @staticmethod
    def getTableCount(tbl_name=_tables[0]):
        """ Query item count from a specific table in database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute("SELECT COUNT(*) FROM {}".format(tbl_name))
        count = c.fetchone()[0]
        con.close()
        return(count)

    @staticmethod
    def queryTableCategory(tbl_name=_tables[0], cat='dad'):
        """
        Query all elements for a specific category from a table in the database object
        """
        con = Database.create_connection()
        c = con.cursor()
        c.execute("SELECT * FROM {} WHERE category=\'{}\'".format(tbl_name, cat))
        rows = c.fetchall()
        con.close()
        return(rows)
