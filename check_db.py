import os
import sqlite3

db_path = 'db.sqlite3'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    print(f"Tables: {tables}")
    
    # Check migration history
    try:
        cursor.execute("SELECT app, name FROM django_migrations;")
        migrations = cursor.fetchall()
        print(f"Applied Migrations: {migrations}")
    except sqlite3.OperationalError:
        print("django_migrations table not found")
        
    conn.close()
else:
    print("Database not found")
