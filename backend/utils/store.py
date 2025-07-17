import sqlite3
import os

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


def store_comments_to_db(comment_data, db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    for comment in comment_data:
        c.execute('''
            INSERT INTO pr_comments (repo_name, pr_number, comment_id, user, body, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (comment['repo_name'], comment['pr_number'], comment['comment_id'], 
              comment['user'], comment['body'], comment['created_at']))
    
    conn.commit()
    conn.close()


def getAllComments(db_name):
    conn = sqlite3.connect(db_name)
    
    # Using pandas to read SQL query directly into DataFrame
    import pandas as pd
    df = pd.read_sql_query('''
        SELECT * FROM pr_comments
    ''', conn)
    
    conn.close()
    
    return df
