import os
import sqlite3

db_path = 'db.sqlite3'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Identify tables to drop
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND (name LIKE 'pages_%' OR name LIKE 'homepage_options_%' OR name LIKE 'about_options_%');")
    tables_to_drop = [row[0] for row in cursor.fetchall()]
    
    print(f"Dropping tables: {tables_to_drop}")
    for table in tables_to_drop:
        cursor.execute(f"DROP TABLE IF EXISTS \"{table}\";")
    
    # Clear migration records
    apps_to_clear = ['pages', 'about_options', 'homepage_options']
    print(f"Clearing migration history for: {apps_to_clear}")
    for app in apps_to_clear:
        cursor.execute(f"DELETE FROM django_migrations WHERE app = '{app}';")
        
    conn.commit()
    conn.close()
    print("Database cleanup complete.")
else:
    print("Database not found.")
