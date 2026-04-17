import mysql.connector

config = {
    'user': 'root',
    'password': 'admin',
    'host': '127.0.0.1',
    'database': 'hospitaldb',
    'raise_on_errors': True
}

try:
    con = mysql.connector.connect(**config)
    cur = con.cursor()

    cur.execute('SELECT name, stock_quantity, unit_price FROM medicines LIMIT 10')
    
    rows = cur.fetchall()
    print('ROWS fetched:', len(rows))
    
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print('DATABASE ERROR:', err)
except Exception as e:
    print('GENERAL ERROR:', type(e).__name__, e)

finally:
    if 'cur' in locals():
        cur.close()
    if 'con' in locals() and con.is_connected():
        con.close()