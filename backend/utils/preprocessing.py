import sqlite3
import pandas as pd
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Preprocessing function using spaCy
def spacy_preprocess(text):
    if pd.isnull(text):
        return ""
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_digit and token.is_alpha]
    return ' '.join(tokens)

# Function to load data from SQLite
def load_data_from_sqlite(db_path, table_name):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

# Function to save DataFrame to SQLite
def save_data_to_sqlite(df, db_path, table_name):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

# --- Example Usage ---

db_path = './data/comments.db'
table_name = 'pr_comments'

# Load data
df = load_data_from_sqlite(db_path, table_name)

# Apply spaCy preprocessing
df['clean_text'] = df['body'].fillna('').apply(spacy_preprocess)

print(df[['body', 'clean_text']].head())

# Save preprocessed data back to SQLite
save_data_to_sqlite(df, db_path, 'processed_pr_comments')
