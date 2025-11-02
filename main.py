"""
Punto de entrada de RubriAI (versión escritorio con Tkinter).
Ejecutar: python main.py
"""
from gui.main_window import MainWindow
import pathlib
import os
import core.db as db

DB_PATH = pathlib.Path("data")
DB_PATH.mkdir(exist_ok=True)
DB_FILE = DB_PATH / "rubriai.sqlite3"

def ensure_db():
    conn = db.connect(str(DB_FILE))
    db.init_db(conn)
    conn.close()

def main():
    ensure_db()
    app = MainWindow(str(DB_FILE))
    app.run()

if __name__ == "__main__":
    main()