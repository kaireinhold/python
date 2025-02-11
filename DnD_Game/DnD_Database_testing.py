import sqlite3
import pandas as pd
import os

#if os.path.exists("DnD_Database.db"):
#    os.remove("DnD_Database.db")

conn = sqlite3.connect("DnD_Database.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        race TEXT NOT NULL,
        class TEXT NOT NULL,
        background TEXT,
        level INTEGER DEFAULT 1
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        hit_die TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Races (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        ability_bonus TEXT,
        features TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Backgrounds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        skill_proficiencies TEXT,
        starting_equipment TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ability_Scores (
        character_id INTEGER PRIMARY KEY,
        Str INTEGER DEFAULT 10 NOT NULL,
        Dex INTEGER DEFAULT 10 NOT NULL,
        Con INTEGER DEFAULT 10 NOT NULL,
        Int INTEGER DEFAULT 10 NOT NULL,
        Wis INTEGER DEFAULT 10 NOT NULL,
        Cha INTEGER DEFAULT 10 NOT NULL,
        FOREIGN KEY (character_id) REFERENCES Characters(id) ON DELETE CASCADE
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        item_name TEXT NOT NULL,
        quantity INTEGER DEFAULT 1,
        FOREIGN KEY (character_id) REFERENCES Characters(id) ON DELETE CASCADE
    );
""")

conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in database:", tables)

conn.close()
