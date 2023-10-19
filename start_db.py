import sqlite3

def start_db(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consultants (
            code TEXT,
            name TEXT,
            phone TEXT,
            level TEXT,
            status TEXT,
            debit_status TEXT,
            perks TEXT,
            points REAL,
            points_to_copper REAL,
            points_to_silver REAL,
            points_to_gold REAL,
            points_to_diamond REAL,
            won_copper INTEGER,     -- New attribute for copper
            won_silver INTEGER,     -- New attribute for silver
            won_gold INTEGER,       -- New attribute for gold
            won_diamond INTEGER     -- New attribute for diamond
        )
    ''')
    conn.commit()
    conn.close()

# Call the function to create the database

