import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Establish a secure DB connection."""
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )

def save_to_db(df, table_name='ohlcv'):
    """Save DataFrame to TimescaleDB."""
    conn = get_db_connection()
    cursor = conn.cursor()
    for index, row in df.iterrows():
        cursor.execute(
            f"""INSERT INTO {table_name} 
            (timestamp, open, high, low, close, volume) 
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (timestamp) DO NOTHING""",
            (index, row['open'], row['high'], row['low'], row['close'], row['volume'])
        )
    conn.commit()
    conn.close()