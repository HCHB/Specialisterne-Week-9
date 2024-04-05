from src.Data.dataconnection import DataConnection


class Cereal:
    _id: int
    _name: str
    _mfr: str
    _type: str
    _calories: int
    _protein: int
    _fat: int
    _sodium: int
    _fiber: float
    _carbo: float
    _sugars: int
    _potass: int
    _vitamins: int
    _shelf: int
    _weight: float
    _cups: float
    _rating: float

    def __init__(self, name: str, mfr: str, type: str, calories: int,
                 protein: int, fat: int, sodium: int, fiber: float, carbo: float,
                 sugars: int, potass: int, vitamins: int, shelf: int,
                 weight: float, cups: float, rating: float, id=None):

        self._id = id
        self._name = name
        self._mfr = mfr
        self._type = type
        self._calories = calories
        self._protein = protein
        self._fat = fat
        self._sodium = sodium
        self._fiber = fiber
        self._carbo = carbo
        self._sugars = sugars
        self._potass = potass
        self._vitamins = vitamins
        self._shelf = shelf
        self._weight = weight
        self._cups = cups
        self._rating = rating

    def add(self):
        command = 'add_cereal'

        values = [self._name, self._mfr, self._type, self._calories,
                  self._protein, self._fat, self._sodium, self._fiber, self._carbo,
                  self._sugars, self._potass, self._vitamins, self._shelf,
                  self._weight, self._cups, self._rating]

        connection = DataConnection()
        item_id = connection.execute_procedure(command, values)
        self._id = item_id

        return True

    def update(self):
        command = ('UPDATE Cereal '
                   'SET name=%(name)s, '
                   'mfr=%(mfr)s, '
                   'type=%(type)s, '
                   'calories=%(calories)s, '
                   'protein=%(protein)s, '
                   'fat=%(fat)s, '
                   'sodium=%(sodium)s, '
                   'fiber=%(fiber)s, '
                   'carbo=%(carbo)s, '
                   'sugars=%(sugars)s, '
                   'potass=%(potass)s, '
                   'vitamins=%(vitamins)s, '
                   'shelf=%(shelf)s, '
                   'weight=%(weight)s, '
                   'cups=%(cups)s, '
                   'rating=%(rating)s '
                   'WHERE ID = %(id)s;')

        values = self.to_dict()

        DataConnection().execute_command(command, values)

        return True

    def remove(self):
        command = ('DELETE FROM Cereal '
                   'WHERE id = %(id)s')

        values = {
            'id': self._id
        }

        DataConnection().execute_command(command, values)

        return True

    def to_dict(self):
        values = {
            'id': self._id,
            'name': self._name,
            'mfr': self._mfr,
            'type': self._type,
            'calories': self._calories,
            'protein': self._protein,
            'fat': self._fat,
            'sodium': self._sodium,
            'fiber': self._fiber,
            'carbo': self._carbo,
            'sugars': self._sugars,
            'potass': self._potass,
            'vitamins': self._vitamins,
            'shelf': self._shelf,
            'weight': self._weight,
            'cups': self._cups,
            'rating': self._rating
        }

        return values
