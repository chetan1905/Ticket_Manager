from connect_db import get_connection

def init_table():
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
                        id SERIAL PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        description TEXT,
                        status VARCHAR(50) DEFAULT 'open',
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );
""")
            print("Initialized tickets table.")
    conn.close()