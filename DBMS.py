# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:55:50 2023

@author: soso2
"""

import sqlite3
import pandas as pd
def setup():
    global conn
    conn = sqlite3.connect('bot.example',check_same_thread=False, timeout=10, isolation_level=None)
    global c
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                        ID INTEGER PRIMARY KEY,
                        Username TEXT ,
                        firstname TEXT NOT NULL,
                        lastname TEXT 
                    )''')
    #c.execute('''ALTER TABLE users ADD COLUMN lastname TEXT''')
    conn.commit()
def add_user(Id,username,first,last):
    try:
        c.execute("INSERT INTO users(ID, Username, firstname, lastname) VALUES (?, ?, ?, ?)", (Id, username, first, last))
        conn.commit()
    except sqlite3.IntegrityError:
        # If the ID already exists, update the user's first and last name
        c.execute("UPDATE users SET firstname=?, lastname=?, Username=? WHERE ID=? ", (first, last , username,Id))
        conn.commit()

def export_to_csv():
    df = pd.read_sql_query("SELECT * FROM users", conn)
    df.to_csv('users.csv', index=False, encoding='utf-16', sep='\t')

def get_user():
    c.execute("SELECT * FROM users")
    table_name="users"
    conn.commit()
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    return df.to_string()
def numOfUsers():
    c.execute("SELECT COUNT(*) FROM users")
    count = c.fetchone()[0]
    return count
def fetch_ID():
    # Retrieve all user IDs from the database
    c.execute("SELECT ID FROM users")
    user_ids = c.fetchall()
    user_ids_df = pd.DataFrame(user_ids, columns=['ID'])  # DataFrame
    # user_ids_array = np.array(user_ids)  # NumPy array
    # Close database connection
    conn.close()
    return user_ids_df

def fetch_last_5_users():
    # Retrieve the last 5 users based on the ID in descending order
    c.execute("SELECT firstname FROM users ORDER BY firstname DESC LIMIT 5")
    lastuser_ids = c.fetchall()
    lastuser_ids_df = pd.DataFrame(lastuser_ids, columns=['firstname'])
    conn.close()
    return lastuser_ids_df 




    


    

