import sqlite3  

def create_teble():
    connection = sqlite3.connect('save.db')
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS saves (savename TEXT, xp INT)""")
    connection.commit()
    connection.close()
    
def view():
    conn=sqlite3.connect("save.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM saves")
    rows=cur.fetchall()
    conn.close()
    for i in rows:
        print(i)
        
def load(a):
    conn=sqlite3.connect("save.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM saves WHERE savename==?",(a,))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(a):
    conn=sqlite3.connect("save.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Auto_Morgue WHERE savename=?",(a,))
    conn.commit()
    conn.close()

def add_row(a,b):
    conn=sqlite3.connect("save.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO saves VALUES (?,?)",(a,b))
    conn.commit()
    conn.close()
    
create_teble()