import sqlite3
import streamlit as st

def create_database():
    conn = sqlite3.connect('cancer.db')
    c = conn.cursor()
    c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND  name='result'""")
    if not c.fetchone():
        c.execute("""CREATE TABLE result
                  (name TEXT, feat1 NUMERIC, feat2 NUMERIC, feat3 NUMERIC, feat4 NUMERIC, feat5 NUMERIC, feat6 NUMERIC, feat7 NUMERIC)""")
        conn.commit()
    conn.close()

def add_result(name, feat1, feat2, feat3, feat4, feat5, feat6, feat7):
    conn = sqlite3.connect('cancer.db')
    c= conn.cursor()
    c.execute("INSERT INTO result VALUES (?,?,?,?,?,?,?)", (name,feat1,feat2,feat3,feat4,feat5,feat6,feat7))
    conn.commit()
    conn.close()

def delete_result(name):
    conn = sqlite3.connect('cancer.db')
    c= conn.cursor()
    c.execute("DELETE FROM result WHERE name = ?", (name))
    conn.commit()
    conn.close()
