"""
Implemente una clase que permita a un número cualquiera imprimir su valor,
luego agregarle sucesivamente.
    a. Sumarle 2.
    b. Multiplicarle por 2.
    c. Dividirlo por 3.
Mostrar los resultados de la clase sin agregados y con la invocación anidada a
las clases con las diferentes operaciones. Use un patrón decorator para
implementar
"""

class Number:
    def __init__(self, value) -> None:
        self._value = value

    @property
    def number(self):
        return self._value;

    def operation(self):
        print(self._value)
        return self


class NumberDecorator(Number):
    _number: Number = None

    def __init__(self, number: Number) -> None:
        self._number = number

    def operation(self) -> Number:
        return self._number.operation()


class SumarDos(NumberDecorator):

    def operation(self) -> Number:
        value = self._number.operation().number
        return Number(value + 2)
    
class MultiplicarPorDos(NumberDecorator):

    def operation(self) -> Number:
        value = self._number.operation().number
        return Number(value * 2)
    
class DividirPorTres(NumberDecorator):

    def operation(self) -> Number:
        value = self._number.operation().number
        return Number(value / 3)


def client_code(number: Number) -> None:
    print(f"Resutado: {number.operation().number}", end="")


if __name__ == "__main__":
    print("")

    number = Number(5)

    sumar_dos = SumarDos(number)
    mult_por_dos = MultiplicarPorDos(sumar_dos)
    div_por_tres = DividirPorTres(mult_por_dos)

    client_code(div_por_tres)

    print("")
   
