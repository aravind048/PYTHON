from mysql.connector import connect, errorcode, Error

class Mysqldb:
    def __init__(self, host, user, pw, db):
        self.host = host
        self.username = user
        self.password = pw
        self.dbname = db
        self.mcnx = None

        print("MySQL database initialized")

    def connectdb(self):
        try:
            self.mcnx = connect(user=self.username, password=self.password, host=self.host, database=self.dbname)

        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            print("MySQL Database Connected...")

    def close(self):
        if self.mcnx:
            self.mcnx.close()
            print("MySQL Database Connection Closed.")
