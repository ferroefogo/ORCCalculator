from sqlite3 import connect

conn = connect('ComponentData.db')
c = conn.cursor()


c.execute("""CREATE TABLE ComponentData (
			id INTEGER PRIMARY KEY,
			type CHAR(20) NOT NULL DEFAULT '',
			name NVARCHAR(320) NOT NULL DEFAULT '',
			metric REAL NOT NULL DEFAULT 0.0,
			quantity INTEGER NOT NULL DEFAULT 0,
			individual_cost INTEGER NOT NULL DEFAULT 0.0,
			total_cost INTEGER NOT NULL DEFAULT 0.0
			)""")
conn.commit()