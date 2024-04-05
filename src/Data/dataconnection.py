import mysql.connector

from copy_paste.decorators import singleton


@singleton
class DataConnection:
    _database_name: str = 'hebo_week_9'
    _host: str = 'localhost'
    _user: str = 'hebo_user'
    _password: str = 'test123'

    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        if self.connection:
            self.connection.disconnect()

        connection = mysql.connector.connect(user=self._user,
                                             password=self._password,
                                             host=self._host,
                                             database=self._database_name)

        self.connection = connection

    def disconnect(self):
        if self.connection:
            self.connection.disconnect()

        self.connection = None

    def execute_procedure(self, command, values):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.callproc(procname=command, args=values)
            stored = cursor.stored_results()
            result_sets = [r.fetchall() for r in stored]

            self.connection.commit()

            if len(result_sets) == 1 and len(result_sets[0]) == 1 and len(result_sets[0][0]) == 1:
                return next(iter(result_sets[0][0]))
            elif len(result_sets) == 1 and len(result_sets[0]) == 1:
                return result_sets[0][0]
            elif len(result_sets) == 1:
                return result_sets[0]
            else:
                return result_sets

    def execute_command(self, command, values):
        with self.connection.cursor(prepared=True, dictionary=True) as cursor:
            cursor.execute(command, values)
            results = cursor.fetchall()

            self.connection.commit()

            return results
