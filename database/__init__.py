import sqlite3
from os import getcwd as currentPath


class DB(object):
  def __init__(self):
    self.db_path = currentPath() + r'/database/db.sqlite'
    self.connection = None
    self.connected = False

  def run(self, sql_code, convert=True, columns=[]):
    if self.connected:
      self.closeConnection()
    self.connection = self.connect()
    self.connected = True
    result = self.connection.cursor().execute(sql_code)
    if convert:
      result = self.convert(result, columns)
    return result

  def commit(self):
    if not self.connected:
      return
    self.connection.commit()

  def closeConnection(self):
    if not self.connected:
      return
    self.connection.close()
    self.connected = False

  def connect(self):
    return sqlite3.connect(self.db_path)

  def convert(self, table, columns):
    table_result, dict_result = [], {}
    for line in table:
      for i, value in enumerate(line):
        dict_result[columns[i]] = value
      table_result.append(dict_result)
      dict_result = {}
    return table_result

  def select(self, table, columns):
    columns = ', '.join(columns)
    return f'SELECT {columns} FROM {table}'

  def insert(self, table, column, valores):
    column = ', '.join(column)
    valores = ', '.join(valores)
    return f'INSERT INTO {table}({column}) VALUES({valores})'
