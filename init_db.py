import sqlite3


conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS exchange_rates")
cursor.execute("""
               CREATE TABLE exchange_rates (
               id INTEGER PRIMARY KEY autoincrement,
               base_currency TEXT NOT NULL,
               target_currency TEXT NOT NULL,
               rate REAL NOT NULL
)
""")

currency_data = [
    ("GBP", "USD", 1.35),
    ("GBP", "INR", 116.93),
    ("GBP", "EUR", 1.18),
    ("GBP", "GBP", 1),
    ("USD", "USD", 1.00),
    ("USD", "INR", 86.60),
    ("USD", "GBP", 0.74),
    ("USD", "EUR", 0.87),
    ("INR", "USD", 0.012),
    ("INR", "INR", 1),
    ("INR", "GBP", 0.0086),
    ("INR", "EUR", 0.01),
    ("EUR", "USD", 1.15),
    ("EUR", "INR", 99.83),
    ("EUR", "GBP", 0.85),
    ("EUR", "EUR", 1)
] 

cursor.executemany(
    "INSERT INTO exchange_rates (base_currency, target_currency, rate) VALUES (?, ?, ?)",
    currency_data
)

conn.commit()
conn.close()

#test to see if it worked
print("database created.")