import mysql.connector

def get_db_connection():
    """Establish a connection to the MySQL database"""
    return mysql.connector.connect(
        host="localhost",   # Change if using a remote database
        user="root",        # Change if using a different MySQL username
        password="root",  # Change if using a different MySQL password
        database="library_db" #Tablename = books
    )
