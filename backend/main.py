from store import init_db, store_comments_to_db
from data_fetching import fetch_pr_comments_for_repo
import sqlite3
import pandas as pd
import os

if __name__ == '__main__':
    repo_name = "freeCodeCamp/freeCodeCamp"
    max_comments = 30
    database_name = "github_pr_comments.db"

    # Initialize the Database
    init_db()

    # Fetch the PR comments
    comments = fetch_pr_comments_for_repo(repo_name, max_comments)
    print(f"Fetched {len(comments)} PR comments from {repo_name}.")

    # Store the comments in the database
    store_comments_to_db(comments, os.path.join("data", database_name))

    # Display stored comments from the Database
    conn = sqlite3.connect(os.path.join("data", database_name))
    df = pd.read_sql_query("SELECT * FROM pr_comments", conn)
    print(df.head())
    print(df.tail())
    conn.close()

