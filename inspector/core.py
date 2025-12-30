# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import sqlite3
import os

def get_connection(db_path):
    if not os.path.exists(db_path):
        raise Exception(f"Database file '{db_path}' not found.")
    return sqlite3.connect(db_path)

def list_tables(db_path):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tables

def get_table_info(db_path, table_name):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    
    # Get schema
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
    schema = cursor.fetchone()
    
    # Get row count
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    
    conn.close()
    return {
        "name": table_name,
        "schema": schema[0] if schema else "N/A",
        "row_count": count
    }

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
