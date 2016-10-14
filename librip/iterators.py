# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case') is not None and kwargs.get('ignore_case')
        self.items = iter(items)
        self.seen = set()

    def __next__(self):
        val = self.items.__next__()
        val = str(val).lower() if self.ignore_case else val

        if val not in self.seen:
            self.seen.add(val)
            return val

        return self.__next__()

    def __iter__(self):
        return self
