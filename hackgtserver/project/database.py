import mysql.connector

mysql_username = ''
mysql_password = ''
mysql_host = ''
mysql_dbname = ''

# ================
# Here are the sql Statements

INSERT_INTO_DB_SQL = 'INSERT INTO Users(username, password) VALUES(%s, %s);'
SELECT_USER_EXISTS_SQL = 'SELECT id FROM Users WHERE username = %s;'
# ================

def create_user(username, hashed_password):
    if not check_mysql_connection():
        return False
    global cnx
    try:
        cursor = cnx.cursor()
        # first let's check if the username exists
        cursor.execute(SELECT_USER_EXISTS_SQL, (username))
        row = cursor.fetchone()
        if row is not None:
            # Row exists
            return False
        # User name is available
        cursor.close()
        cursor = cnx.cursor()
        cursor.execute(INSERT_INTO_DB_SQL, (username, hashed_password))
        return True
    finally:
        cnx.commit()
        cursor.close()
        
def is_user_exists(username):
    if not check_mysql_connection():
        return None
    global cnx
    try:
        cursor = cnx.cursor()
        # first let's check if the username exists
        cursor.execute(SELECT_USER_EXISTS_SQL, (username))
        row = cursor.fetchone()
        if row is not None:
            # Row exists
            return False
        # User name is available
        return True
    finally:
        cursor.close()

def check_mysql_connection():
    sq = 'SELECT NOW()'
    global cnx
    try:
        cursor = cnx.cursor()
        cursor.execute(sq)
    except mysql.connector.Error as e:
        if e.errno == 2006:
            return connect()
        else:
            print ( "No connection with database." )
            return False
    finally:
        cursor.close()
        
def connect():
    try:
        global cnx 
        cnx = mysql.connector.connect(user=mysql_username, password=mysql_password,
                              host=mysql_host,
                              database=mysql_dbname)
        return True
    except mysql.connector.Error as err:
        print('Mysql connection could not be established')
        return False
        
if __name__ == '__main__':
    if not check_mysql_connection():
        sys.exit(0)