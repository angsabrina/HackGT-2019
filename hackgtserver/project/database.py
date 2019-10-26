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

def check_mysql_connection():
    try:
        global cnx 
        cnx = mysql.connector.connect(user=mysql_username, password=mysql_password,
                              host=mysql_host,
                              database=mysql_dbname)
        return True
    except mysql.connector.Error as err:
        log('Mysql connection could not be established')
        return False