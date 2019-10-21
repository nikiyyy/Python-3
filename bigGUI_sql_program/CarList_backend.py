import sqlite3 as sql
from random import randint

def add_row(a,b,c,d):
    conn=sql.connect("cars.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Auto_Morgue VALUES(?,?,?,?,?)",(randint(1,999999),a,b,c,d))
    conn.commit()
    conn.close()

def view():
    conn=sql.connect("cars.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Auto_Morgue")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(a="",b="",c=0,d=""):
    conn=sql.connect("cars.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Auto_Morgue WHERE Brand==? OR Model==? OR Year==? OR Number==?",(a,b,c,d))
    rows=cur.fetchall()
    conn.close()
    return rows
def delete(a):
    conn=sql.connect("cars.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Auto_Morgue WHERE id=?",(a,))
    conn.commit()
    conn.close()
    
def update(a="",b="",c=0,d="",e=""):
    conn=sql.connect("cars.db")
    cur=conn.cursor()
    cur.execute("UPDATE Auto_Morgue SET Brand==?, Model==?, Year==?, Number==? WHERE id=?",(a,b,c,d,e))
    conn.commit()
    conn.close()

conn=sql.connect("cars.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Auto_Morgue (id INTEGER PRIMARY KEY,Brand TEXT, Model TEXT, Year INTEGER ,milage TEXT)")
#add_row("mazda","mx-5 NA",1993,"45300")
#print(view())
#print(search("Volvo"))
conn.commit()
conn.close()

