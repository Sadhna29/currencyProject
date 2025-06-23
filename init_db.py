import sqlite3
import os

# database file name
DB_FILE = "db.sqlite3"

def init_db():
    """Initializes the SQLite database and creates necessary tables and populates currency data."""
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        #create logins table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logins (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                security_answer TEXT NOT NULL
            )
        """)

        # create history table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                base TEXT NOT NULL,
                target TEXT NOT NULL,
                amount REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (username) REFERENCES logins(username)
            )
        """)

        # create error_log table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS error_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                base_currency TEXT,
                target_currency TEXT,
                amount TEXT,
                error_message TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # create currency_data table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS currency_data (
                base_currency TEXT PRIMARY KEY,
                rate2021 REAL NOT NULL,
                rate2022 REAL NOT NULL,
                rate2023 REAL NOT NULL,
                rate2024 REAL NOT NULL,
                rate2025 REAL NOT NULL
            )
        """)

        # currency data to insert - AI generated
        currency_data = [
            ("USD", 100.0, 100.0, 100.0, 100.0, 100.0), # Added .0 to make them floats
            ("GBP", 73.0, 87.0, 92.0, 87.0, 74.0),
            ("INR", 7457.0, 8135.0, 8229.0, 8347.0, 8684.0),
            ("EUR", 84.56, 94.0, 92.0, 92.8, 87.0),
            ("CAD", 125.0, 129.0, 135.0, 137.0, 141.0),
            ("AUD", 133.0, 144.0, 151.0, 151.0, 155.0),
            ("JPY", 10976.0, 13145.0, 14050.0, 15145.0, 14917.0),
            ("CNY", 645.0, 673.0, 708.0, 719.0, 725.0),
            ("CHF", 91.4, 95.5, 89.9, 88.1, 81.76),
            ("NZD", 141.5, 157.8, 160.9, 165.4, 163.0),
            ("SGD", 134.4, 137.9, 133.9, 133.6, 128.5),
            ("HKD", 777.3, 783.1, 783.7, 780.3, 784.9),
            ("KRW", 114488.0, 129173.0, 132748.0, 136415.0, 136000.0),
            ("SEK", 858.4, 1012.2, 1076.9, 1057.7, 966.1),
            ("NOK", 859.8, 961.9, 1080.7, 1075.6, 1007.0),
            ("DKK", 629.0, 707.7, 685.5, 689.6, 647.8),
            ("MXN", 2028.4, 2011.0, 1774.9, 1833.0, 1700.0),
            ("SAR", 375.0, 375.0, 375.0, 375.0, 375.0),
            ("TRY", 890.4, 1657.2, 2382.4, 3286.7, 3968.0),
            ("PLN", 390.0, 450.0, 417.9, 400.0, 420.0),
            ("BRL", 539.5, 516.5, 499.4, 539.2, 548.4),
            ("ZAR", 1478.9, 1637.7, 1845.7, 1832.6, 1799.0)
        ]

        # Insert currency data if the table is empty
        cursor.execute("SELECT COUNT(*) FROM currency_data")
        if cursor.fetchone()[0] == 0:
            print("Populating currency_data table...")
            cursor.executemany("""
                INSERT INTO currency_data (base_currency, rate2021, rate2022, rate2023, rate2024, rate2025)
                VALUES (?, ?, ?, ?, ?, ?)
            """, currency_data)
            conn.commit()
            print("Currency data populated.")
        else:
            print("Currency data table already populated.")


        conn.commit()
        print(f"Database tables created or checked in {DB_FILE}.")

    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':

    init_db() # This line calls the function!