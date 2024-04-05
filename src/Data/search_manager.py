from src.project_enums import ObjectTypes, SearchTypes

from src.Data.dataconnection import DataConnection
from src.Data.object_factory import ObjectFactory
from src.Data.sql_parser import SQLParser


class SearchManager:
    def __init__(self):
        self._data_connection = DataConnection()
        self.sql_parser = SQLParser()

        self._procedures = {
            SearchTypes.CEREAL: {
                'table': 'Cereal',
                'object_type': ObjectTypes.CEREAL
            },
            SearchTypes.USER: {
                'table': 'user',
                'object_type': ObjectTypes.USER
            },
        }

    def search(self, procedure, output='*', fields=()):
        table = self._decider(procedure, 'table')

        command, values = self.sql_parser.generate_select_query(table_name=table,
                                                                output_fields=output,
                                                                data_fields=fields)

        results = self._data_connection.execute_command(command, values)

        factory = ObjectFactory()
        objects = []

        if not isinstance(results, list):
            results = [results]

        item_type = self._decider(procedure, 'object_type')

        for result in results:
            new_object = factory.build(item_type, **result)
            objects.append(new_object)

        return objects

    def _decider(self, procedure, item):
        command = self._procedures[procedure][item]
        return command
