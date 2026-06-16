import sqlite3

DB_NAME = "search_history.db"

def setup_db():
    """Cria a tabela de histórico se ela ainda não existir."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT NOT NULL,
            lat REAL NOT NULL,
            lon REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

### create
def save_search(slug: str, lat: float, lon: float) -> None:
    """Recebe o slug, lat e lon e faz a inserção no banco."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO search_history (slug, lat, lon) VALUES (?, ?, ?)",
        (slug, lat, lon)
    )
    
    conn.commit()
    conn.close()

### read
def find_search_by_term(term: str) -> list:
    """Busca no banco todas as slugs que contêm o termo digitado."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT slug FROM search_history WHERE slug LIKE ?",
        (f"%{term}%",)
    )
    
    results = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    return results