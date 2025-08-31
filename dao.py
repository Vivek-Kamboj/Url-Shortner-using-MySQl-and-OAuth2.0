import mysql.connector
from mysql.connector import Error

class MySQLDAO:
    def __init__(self, host="localhost", user="root", password="yourpassword", database="testdb"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def _get_connection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def create_table(self):
        """Create table if not exists"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id INT AUTO_INCREMENT PRIMARY KEY,
                code VARCHAR(10) UNIQUE NOT NULL,
                url TEXT NOT NULL
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()

    def insert_url(self, code: str, url: str):
        """Insert a short code → URL mapping"""
        conn = self._get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO urls (code, url) VALUES (%s, %s)"
        cursor.execute(sql, (code, url))
        conn.commit()
        cursor.close()
        conn.close()

    def get_url(self, code: str):
        """Retrieve original URL from short code"""
        conn = self._get_connection()
        cursor = conn.cursor()
        sql = "SELECT url FROM urls WHERE code=%s"
        cursor.execute(sql, (code,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row[0] if row else None
