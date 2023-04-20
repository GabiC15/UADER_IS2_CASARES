# Provea una clase que dado un número entero cualquiera retorne el factorial del
# mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma
# instancia de clase.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Factorial(metaclass=SingletonMeta):
    def calculate(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")

        elif num == 0:
            return 1

        else:
            fact = 1
            while (num > 1):
                fact *= num
                num -= 1
            return fact


fact1 = Factorial()
fact2 = Factorial()

if (fact1 == fact2):
    print("Son las mismas instancias")

print(fact1.calculate(5))

print(fact2.calculate(3))
