class Observer:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, emitted_id):
        if emitted_id == self.observer_id:
            print(f"El ID {emitted_id} coincide con el ID del Observer {self.observer_id}.")


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, emitted_id):
        for observer in self.observers:
            observer.update(emitted_id)


def ejecutar():
    subject = Subject()

    observer1 = Observer("Hola")
    observer2 = Observer("Chau")
    observer3 = Observer("1234")
    observer4 = Observer("5678")

    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)
    subject.attach(observer4)

    ids = ["Hola", "QWERT", "Chau", "9999", "ZXCV", "1234", "ASDF", "5678"]
    for id in ids:
        subject.notify(id)


if __name__ == "__main__":
    ejecutar()
