from sqlite3 import connect

conn = connect('ComponentData.db')
c = conn.cursor()

c.execute('INSERT INTO SavedConfigs(config_id) VALUES(1)')
conn.commit()
# c.execute("""CREATE TABLE ComponentData (
# 			id INTEGER PRIMARY KEY,
# 			config_id INTEGER NOT NULL DEFAULT '',
# 			type CHAR(20) NOT NULL DEFAULT '',
# 			name NVARCHAR(320) NOT NULL DEFAULT '',
# 			metric REAL NOT NULL DEFAULT 0.0,
# 			quantity INTEGER NOT NULL DEFAULT 0,
# 			individual_cost INTEGER NOT NULL DEFAULT 0.0,
# 			total_cost INTEGER NOT NULL DEFAULT 0.0,
# 			FOREIGN KEY(config_id) REFERENCES SavedConfigs(config_id)
# 			)""")
# conn.commit()

# c.execute("""CREATE TABLE SavedConfigs (
# 			config_id INTEGER PRIMARY KEY
# 			)""")
# conn.commit()
