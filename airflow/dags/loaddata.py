import sys
import sqlite3
import pandas as pd

def load_csv_to_sqlite(csv_path, db_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table if it does not exist
    # Adjust the table creation statement based on your CSV structure
    table_name = 'domains'
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            Domain TEXT,
            Type TEXT,
            SponsoringOrganization TEXT,
            Date TEXT
        )
    ''')

    # Insert the data into the table
    df.to_sql(table_name, conn, if_exists='append', index=False)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    csv_path = sys.argv[1]
    db_path = sys.argv[2]
    load_csv_to_sqlite(csv_path, db_path)
