import sqlite3
from os import getcwd as current_path


class DB(object):
    def __init__(self):
        self._db_path = current_path() + r'/database/db.sqlite'
        self._connected = False
        self._connection = None

    def run(self, sql_code, convert=True, columns=[]):
        if self._connected:
            self.close_connection()

        self._connection = self.connect()
        self._connected = True

        result = self._connection.cursor().execute(sql_code)

        if convert:
            result = self.convert(result, columns)

        return result

    def commit(self):
        if not self._connected:
            return

        self._connection.commit()

    def close_connection(self):
        if not self._connected:
            return

        self._connection.close()
        self._connected = False

    def connect(self):
        return sqlite3.connect(self._db_path)

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
