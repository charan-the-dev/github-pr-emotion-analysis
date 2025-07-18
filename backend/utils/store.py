import sqlite3
import pandas as pd

def init_db(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS pr_comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repo_name TEXT,
            pr_number INTEGER,
            comment_id INTEGER,
            user TEXT,
            body TEXT,
            created_at TEXT
        )
    ''')
    
    conn.commit()
    conn.close()


def load_data_from_sqlite(db_path, table_name):
    conn = sqlite3.connect(db_path)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def save_data_to_sqlite(df, db_path, table_name):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()


def getAllTables(db_name):
    conn = sqlite3.connect(db_name)
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql_query(query, conn)
    conn.close()
    return tables


def getAllComments(db_name, table_name):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f'SELECT * FROM {table_name}', conn)
    conn.close()
    return df
