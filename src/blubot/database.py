#!/usr/bin/python3
import os
import sqlite3
import webbrowser
import subprocess
from uw.character import parse_character
import json

class Db:
  def __init__(self):
    self.conn = sqlite3.connect("uw.db")

  def create_tables(self):
    c = self.conn.cursor()    
    sql = '''
        CREATE TABLE IF NOT EXISTS character
        (
          character_id INTEGER PRIMARY KEY AUTOINCREMENT,
          user_id INTEGER, 
          name TEXT,
          data TEXT,
          active BOOLEAN
        );
      '''
    c.execute(sql)

    self.conn.commit()

  def insert_character(self, user_id, name, data):
    c = self.conn.cursor()
    sql = '''
        INSERT OR IGNORE INTO character(user_id, name, data) VALUES(?, ?, ?);
        '''
    c.execute(sql, (user_id, name, data,))
    self.conn.commit()

  def update_character(self, user_id, name, data):
    c = self.conn.cursor()
    sql = '''
        UPDATE character
        SET data = ?
        WHERE user_id = ? AND name = ?;
        '''
    c.execute(sql, (data, user_id, name,))
    self.conn.commit()

  def set_active_character(self, user_id, name):
    c = self.conn.cursor()
    sql = '''
        UPDATE character
        SET active = CASE name WHEN ? THEN true else false END
        WHERE user_id = ?;
        '''
    c.execute(sql, (name, user_id))
    self.conn.commit()

  def get_active_character(self, user_id):
    c = self.conn.cursor()
    sql = '''
        SELECT data FROM character WHERE user_id = ? and active = true;
        '''
    cursor = c.execute(sql, (user_id,))
    row = cursor.fetchone()
    if row is not None:
      return row[0]
    return None

  def get_all_characters(self, user_id):
    characters = []
    c = self.conn.cursor()
    sql = '''
        SELECT name FROM character WHERE user_id = ?;
        '''
    for row in c.execute(sql, (user_id,)):
        characters.append(row[0]) 
    return characters

  def get_character(self, user_id, name):
    c = self.conn.cursor()
    sql = '''
        SELECT data FROM character WHERE user_id = ? and name = ?;
        '''
    cursor = c.execute(sql, (user_id, name,))
    row = cursor.fetchone()
    if row is not None:
      return row[0]
    return None

  def delete_character(self, user_id, name):
    characters = []
    c = self.conn.cursor()
    sql = '''
        DELETE FROM character WHERE user_id = ? AND name = ?;
        '''
    c.execute(sql, (user_id, name,))
    self.conn.commit()

# Init the tables
def main():
  print("Creating tables")
  db = Db()
  db.create_tables()
  print("Table creation complete")

main()