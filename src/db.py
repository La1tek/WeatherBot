import datetime

import sqlite3 as sql

from arguments import SQL

def Create_Tables():
    con = sql.connect(SQL.name_db)
    with con:
      cur = con.cursor()

      cur.execute("""
      CREATE TABLE IF NOT EXISTS users(
      id_user INTEGER PRIMARY KEY,
      city TEXT NOT NULL
      )
      """)

      cur.execute("""
      CREATE TABLE IF NOT EXISTS names(
      id_user INTEGER PRIMARY KEY,
      first name TEXT NOT NULL,
      username TEXT NOT NULL
      )
      """)

      cur.execute("""
      CREATE TABLE IF NOT EXISTS logs(
      id_user INTEGER,
      time TEXT NOT NULL,
      message TEXT NOT NULL
      )
      """)

      con.commit()
      cur.close()
    

def City(id, city):
  con = sql.connect(SQL.name_db)
  with con:
    cur = con.cursor()
    info = cur.execute('SELECT * FROM users WHERE id_user = ?', (id, )).fetchone()
    if info == None: 
      print("Запись добавлена")
      cur.execute(f"INSERT INTO users VALUES ('{id}','{city}')")
    else:
      print("Обновлено")
      cur.execute('UPDATE users SET city = ? WHERE id_user = ?', (city, id))
      print(View_city(id))
    con.commit()
    cur.close()

def Log(id, message):
  print(id, message)
  con = sql.connect(SQL.name_db)
  with con:
    cur = con.cursor()
    time = datetime.datetime.now()
    cur.execute(f"INSERT INTO logs VALUES ('{id}','{time}','{message}')")
    con.commit()
    cur.close()

def AddID(id, first_name, username):
  con = sql.connect(SQL.name_db)
  with con:
    cur = con.cursor()
    info = cur.execute('SELECT * FROM users WHERE id_user = ?', (id, )).fetchone()
    if info == None: 
      cur.execute(f"INSERT INTO users VALUES ('{id}','None')")
    info = cur.execute('SELECT * FROM names WHERE id_user = ?', (id, )).fetchone()
    if info == None:
      cur.execute(f"INSERT INTO names VALUES ('{id}','{first_name}','{username}')")
    con.commit()
    cur.close()

def View_city(id):
  con = sql.connect(SQL.name_db)
  with con:
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE id_user = ?", (id,))
    rows = cur.fetchall()
    return rows[0][1]

Create_Tables()

