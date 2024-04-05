class SQLParser:
    def generate_select_query(self, table_name='Cereal', output_fields=(), data_fields=()):
        sql_select = self._generate_selection_clause(output_fields)
        sql_from = self._generate_from_clause(table_name)
        sql_where, values = self._generate_where_clause(data_fields)
        return (f'{sql_select}'
                f'{sql_from}'
                f'{sql_where}'), values

    def _generate_selection_clause(self, fields):
        clause = 'SELECT'

        if len(fields) == 0:
            clause += ' *'
            return clause

        is_first = True
        for field in fields:
            if is_first:
                is_first = False
                clause += ' '
            else:
                clause += ', '

            clause += field

        return clause

    def _generate_from_clause(self, table_name):
        clause = f' FROM {table_name}'
        return clause

    def _generate_where_clause(self, data):
        clause = ''
        values = []
        is_first = True

        if len(data) > 0:
            clause += ' WHERE '
        else:
            return clause, values

        for field in data:
            if is_first:
                is_first = False
            else:
                clause += ' AND '

            clause += f'{field.name} {field.comparator} ?'  # TODO if adding LIKE
            values.append(field.value)

        clause.strip()

        return clause, values
