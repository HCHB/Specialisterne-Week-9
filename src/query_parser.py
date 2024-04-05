class QueryParser:
    # ImmutableMultiDict([('fat[ne]', '1'), ('calories[lt]', '100'), ('calories[gt]', '10')])

    def __init__(self):
        self._comparators = {
            'lt': '<',
            'leq': '<=',
            'gt': '>',
            'geq': '>=',
            'ne': '!=',
        }

    def parse(self, args):
        fields = []
        for arg, value in args.items():
            if '[' in arg and ']' not in arg:
                raise Exception

            if ']' in arg and '[' not in arg:
                raise Exception

            arg = arg.replace(']', '[').split('[')

            if len(arg) > 1:
                field = QueryField(arg[0], self._comparators[arg[1]], value)
            else:
                field = QueryField(arg[0], '=', value)

            fields.append(field)
        return fields


class QueryField:
    def __init__(self, name, query_type, value):
        self._field_name = name
        self._comparison_type = query_type
        self._value = value

    def __str__(self):
        return f'{self._field_name}{self._comparison_type}{self._value}'

    @property
    def value(self):
        return self._value

    @property
    def name(self):
        return self._field_name

    @property
    def comparator(self):
        return self._comparison_type
