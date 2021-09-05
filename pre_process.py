import sqlite3


def main() -> None:
    dbname = "fruit.db"
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        create_table(cur)
        insert(cur)
        select(cur)


def create_table(cur: sqlite3.Cursor) -> None:
    cur.execute("DROP TABLE IF EXISTS fruit")
    cur.execute(
        """
CREATE TABLE fruit(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    名前 STRING,
    値段 INTEGER
)
"""
    )


def insert(cur: sqlite3.Cursor) -> None:
    fruit = [("りんご", 159), ("みかん", 72), ("葡萄", 861)]
    cur.executemany("INSERT INTO fruit(名前, 値段 ) VALUES ( ?, ?)", fruit)


def select(cur: sqlite3.Cursor) -> None:
    results = cur.execute("SELECT * FROM fruit")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
