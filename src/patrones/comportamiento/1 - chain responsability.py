class Handler:
    def __init__(self, next=None):
        self.next = next

    def handle_request(self, number):
        if self.can_handle(number):
            self.execute(number)
        elif self.next is not None:
            self.next.handle_request(number)
        else:
            print(f"El número {number} no pudo ser consumido.")

    def can_handle(self, number):
        raise NotImplementedError()

    def execute(self, number):
        raise NotImplementedError()


class PrimosHandler(Handler):
    def can_handle(self, number):
        return self.is_prime(number)

    def execute(self, number):
        print(f"El número {number} es primo.")

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


class ParesHandler(Handler):
    def can_handle(self, number):
        return number % 2 == 0

    def execute(self, number):
        print(f"El número {number} es par.")


def ejecutar():
    primos_handler = PrimosHandler()
    pares_handler = ParesHandler()

    primos_handler.next = pares_handler

    for number in range(1, 101):
        primos_handler.handle_request(number)


if __name__ == "__main__":
    ejecutar()
