import csv
import os

from src.Data.dataconnection import DataConnection


class DataLoader:
    def __init__(self):
        self._cleaner = self._simple_clean
        self._insert_command = ('INSERT INTO Cereal '
                                '(name, mfr, type, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weight, cups, rating) '
                                'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')

    def _simple_clean(self, row):
        row[-1] = row[-1].replace('.', '')
        return row

    def load(self, path):
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')

            data_connection = DataConnection()

            for row in reader:
                try:
                    cleaned = self._cleaner(row)
                    result = data_connection.execute_command(self._insert_command, cleaned)

                    print(cleaned)
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    loader = DataLoader()
    loader.load('./Data/Cereal.csv')
