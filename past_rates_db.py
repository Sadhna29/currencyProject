import sqlite3

conn = sqlite3.connect("past_rates.sqlite3")
cursor = conn.cursor()

#cursor.execute("DROP TABLE IF EXISTS exchange_rates")
#possible errors
cursor.execute("""
               CREATE TABLE rates (
               id INTEGER PRIMARY KEY autoincrement,
               base_currency TEXT NOT NULL,
               target_currency TEXT NOT NULL,
               2021_rate REAL NOT NULL,
               2022_rate REAL NOT NULL,
               2023_rate REAL NOT NULL,
               2024_rate REAL NOT NULL,
               2025_rate REAL NOT NULL
)
""") 

currency_data = [
    ("GBP", "USD", 2021_rate, 2022_rate, 2023_rate, 2024_rate, 2025_rate),
] 

cursor.executemany(
    "INSERT INTO exchange_rates (base_currency, target_currency, 2021_rate, 2022_rate, 2023_rate, 2024_rate, 2025_rate) VALUES (?, ?, ?, ?, ?, ?, ?)",
    currency_data
)

conn.commit()
conn.close()

#test to see if it worked
print("database created.")