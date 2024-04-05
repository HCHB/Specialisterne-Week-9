from passlib.handlers.sha2_crypt import sha256_crypt

from src.Data.dataconnection import DataConnection


class User:
    _name: str
    _password: str

    def __init__(self, name: str, password: str, encrypt_password=False):
        self._name = name
        if encrypt_password:
            self._password = sha256_crypt.hash(password)
        else:
            self._password = password

    def add(self):
        command = 'INSERT INTO user (name, password) VALUES(%(name)s, %(password)s);'

        values = self._to_dict()

        connection = DataConnection()
        connection.execute_command(command, values)

        return True

    def update(self):
        command = ('UPDATE user '
                   'SET password=%(password)s, '
                   'WHERE name = %(name)s;')

        values = self._to_dict()

        DataConnection().execute_command(command, values)

        return True

    def remove(self):
        command = ('DELETE FROM user '
                   'WHERE name = %(name)s')

        values = {
            'name': self._name
        }

        DataConnection().execute_command(command, values)

        return True

    def _to_dict(self):
        values = {
            'name': self._name,
            'password': self._password,
        }

        return values

    @property
    def password(self):
        return self._password

    @property
    def name(self):
        return self._name
