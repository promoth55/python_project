import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS std_info (id INTEGER PRIMARY KEY, Std_name text, Roll_no text, Section text, Department text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM std_info")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO std_info VALUES (NULL, ?, ?, ?, ?)",
                         (part, customer, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM std_info WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE std_info SET Std_name = ?, Roll_no = ?, Section = ?, Department = ? WHERE id = ?",
                         (part, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()