import sqlite3

con = sqlite3.connect('adet-rest/database.sqlite')
cur = con.cursor()
try:
    cur.execute('SELECT name, stock_quantity, unit_price FROM medicines LIMIT 10')
    rows = cur.fetchall()
    print('ROWS', len(rows))
    for row in rows:
        print(row)
except Exception as e:
    print('ERROR', type(e).__name__, e)
finally:
    con.close()
