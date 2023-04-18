import sqlite3
a = sqlite3.connect('user_data.db')
c = a.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS user_details (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL
);
"""
c.execute(create_table_query)
a.commit()
a.close()
