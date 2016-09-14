from .base import Generator


class Select(Generator):

    def get_arguments(self, table=None, where=None, pk='id', **kwargs):
        super(Select, self).get_arguments(**kwargs)

        self.table = table
        self.where = where
        self.pk = pk

    def generate(self):
        backend = self.blueprint.backend

        while True:
            values = backend.select_random(self.table, fields=(self.pk,),
                                           where=self.where, max_rows=10000)
            for value in values:
                yield value