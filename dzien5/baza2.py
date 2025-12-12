# baza danych - system prechowywania danych
# silnik - mechanizm zarządzania danymi w bazie
# relacyjne, nierelacyjne
# sql - mysql, posgress, oragle, firebird, mssql, sqlite
# nosql = MogoDB

import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza danych została podłączona")

    query = """
    CREATE TABLE IF NOT EXISTS developers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL);
    """
    c.execute(query)
    conn.commit()

    insert = """
    INSERT INTO developers (id, name, email, salary)
    VALUES (1, 'Radek','raj@raj.pl', 10000);
    """
    # c.execute(insert)
    # conn.commit()

    select = "SELECT * FROM developers;"
    for row in c.execute(select):
        print(row)

    update = """
    UPDATE developers
    SET salary=2000
    WHERE id=1;
    """
    c.execute(update)
    conn.commit()

    delete = """
    DELETE FROM developers WHERE id=1;
    """

    c.execute(delete)
    conn.commit()
except Exception as e:
    print("Bład podłączennia bazy danych:", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
