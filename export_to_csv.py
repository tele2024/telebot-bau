# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 06:59:21 2024

@author: soso2
"""

import sqlite3
import pandas as pd

def export_to_csv():
    conn = sqlite3.connect('bot.example')
    df = pd.read_sql_query("SELECT * FROM users", conn)
    df.to_csv('users.csv', index=False)

if __name__ == "__main__":
    export_to_csv()
