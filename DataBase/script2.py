import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user = 'postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, qu, price):
    conn=psycopg2.connect("dbname='database1' user = 'postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" %(item,qu,price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,qu,price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user = 'postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT*FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user = 'postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item))
    conn.commit()
    conn.close()

def update(qu, price, item):
    conn=psycopg2.connect("dbname='database1' user = 'postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(qu, price, item))
    conn.commit()
    conn.close()

#create_table()
#insert('Apple',10,15)
update(20,28, 'Apple')
#insert('Water Glass', 10,5)
#delete("Wine Glass")
#update(11,6.3, 'Water Glass')
#print(view())
