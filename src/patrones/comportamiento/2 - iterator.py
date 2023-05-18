class ReversoIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def has_next(self):
        return self.index > 0

    def next(self):
        self.index -= 1
        return self.data[self.index]


class CorrectoIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def has_next(self):
        return self.index < len(self.data)

    def next(self):
        value = self.data[self.index]
        self.index += 1
        return value


class StringCollection:
    def __init__(self, string):
        self.string = string

    def create_correcto_iterator(self):
        return CorrectoIterator(self.string)

    def create_reverso_iterator(self):
        return ReversoIterator(self.string)


def main():
    collection = StringCollection("Hola! Como estás?")

    print("Recorrido en sentido directo:")
    directo_iterator = collection.create_correcto_iterator()
    while directo_iterator.has_next():
        print(directo_iterator.next())

    print("\n")
    print("Recorrido en sentido reverso:")
    reverso_iterator = collection.create_reverso_iterator()
    while reverso_iterator.has_next():
        print(reverso_iterator.next())


if __name__ == "__main__":
    main()
