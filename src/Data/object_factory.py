from src.project_enums import ObjectTypes

from src.Data.cereal import Cereal


class CerealBuilder:
    @staticmethod
    def build(**kwargs):
        cereal = Cereal(**kwargs)
        return cereal


class ObjectFactory:
    _builders = {
                 ObjectTypes.CEREAL: CerealBuilder(),
                 }

    def build(self, object_type, **kwargs):
        builder = self._decider(object_type)

        new_object = builder.build(**kwargs)

        return new_object

    def _decider(self, object_type):
        builder = self._builders[object_type]
        return builder

    def add_builder(self, object_type, builder):
        if object_type in self._builders:
            raise Exception(f'A builder for {object_type} already exists')

        self._builders[object_type] = builder

    def replace_builder(self, object_type, builder):
        self._builders[object_type] = builder
