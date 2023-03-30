class FactorialOPP:
    def factorial(self, num):
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

    def run(self, min, max):
        for i in range(min, max + 1):
            print(f"Factorial {i}! es", self.factorial(i))


FactorialOPP().run(1, 10)
