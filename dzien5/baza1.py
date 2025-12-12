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
except Exception as e:
    print("Bład podłączennia bazy danych:", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
