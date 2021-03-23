#!/usr/bin/python3
import sqlite3

def seed_db():
    con = sqlite3.connect('testr.db')
    con.close()