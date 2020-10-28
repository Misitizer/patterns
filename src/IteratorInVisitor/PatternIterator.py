from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):

    def __init__(self, collection, cursor):
        self.collection = collection
        self.cursor = cursor

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class ListIterator(Iterator):
    def __init__(self, collection: list):
        super().__init__(collection, 0)

    def current(self):
        if self.cursor < len(self.collection):
            return self.collection[self.cursor]

    def next(self):
        if self.cursor + 1 <= len(self.collection):
            self.cursor += 1
            return self.collection[self.cursor]

    def has_next(self):
        if self.cursor + 1 < len(self.collection):
            return True
        return False


class DictIterator(Iterator):
    def __init__(self, collection: dict):
        self.collection = collection
        self.keys = list(self.collection.keys())
        self.cursor = self.keys.pop(0)

    def current(self):
        if self.cursor in self.collection:
            return self.collection[self.cursor]

    def next(self):
        if len(self.keys) > 0:
            self.cursor = self.keys.pop(0)
            return self.collection[self.cursor]

    def has_next(self):
        if len(self.keys) > 0:
            return True
        return False


class Collection(metaclass=ABCMeta):

    @abstractmethod
    def iterator(self):
        pass


class ListCollection(Collection):

    def __init__(self, collection: list):
        self.collection = collection

    def iterator(self):
        return ListIterator(self.collection)


class DictCollection(Collection):

    def __init__(self, collection: dict):
        self.collection = collection

    def iterator(self):
        return DictIterator(self.collection)


def chooseYourCollection(collection=Collection):
    iterator = collection.iterator()
    print(iterator.current())
    print(iterator.has_next())
    iterator.next()
    print(iterator.current())
    iterator.next()
    print(iterator.current())
    iterator.next()
    print(iterator.current())
    iterator.next()
    print(iterator.current())
    print(iterator.has_next())


if __name__ == "__main__":
    chooseYourCollection(ListCollection([132, 4214, 514125, 213124, 32141]))
    print('------------------')
    chooseYourCollection(DictCollection({'Kirill': 132, 'Nastya': 4214, 'Pasha': 514125, 'Sanya': 213124, 'Anton': 32141}))