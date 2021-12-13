import sqlite3

conn = sqlite3.connect('product-database.sqlite3')
c = conn.cursor()

# Create Table
c.execute("""CREATE TABLE IF NOT EXISTS transaction_history (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tid TEXT,
                stamp TEXT,
                product TEXT,
                price REAL,
                quan REAL,
                total REAL )""")

print('success')

def insert_transaction(data):
    # data = {'tid':'12312312','stamp':'2021-12-13 14:35:23'...}
    ID = None 
    tid = data['tid']
    stamp = data['stamp']
    product = data['product']
    price = data['price']
    quan = data['quan']
    total = data['total']

    with conn: 
        command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
        c.execute(command,(ID,tid,stamp,product,price,quan,total))
        conn.commit()
    print('inserted!')

def view_transaction():
    with conn:
        c.execute("SELECT * FROM transaction_history")
        data = c.fetchall()
        print(data)

view_transaction()

transaction = {'tid':'987978989789',
               'stamp': '2021-12-13 13:48:38',
               'product': 'ทุเรียน',
               'price':100,
               'quan':50,
               'total':5000}

# insert_transaction(transaction)
