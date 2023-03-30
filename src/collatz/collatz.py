import matplotlib.pyplot as plt
import numpy as np


# Funcion que ejecuta la conjetura de collatz
def collatz(n):
    result = [n]
    # Itera mientras N sea mayor que 1
    while n > 1:
        if (n % 2) == 0:
            # Si es par
            n = n / 2
        else:
            # Si es impar
            n = n * 3 + 1
        result.append(n)

    return result


yaxis = []
xaxis = list(range(1, 10000))
# Ejecuta la funcion collatz desde 1 a 10000
for i in range(1, 10000):
    sec = collatz(i)
    # Agrego en el eje de ordenadas la cantidad de iteraciones
    yaxis.append(len(sec))

# Este variable indica el valor limite de n
# para que el grafico sea práctico de visualizar.
# En este caso elegí 10, pero puede cualquier otro
# valor menor o igual que 10000.
limite = 10

xaxis = np.array(xaxis[:limite])
yaxis = np.array(yaxis[:limite])

print("Valores de N:", xaxis)
print("Iteraciones: ", yaxis)

plt.plot(xaxis, yaxis)
plt.title("Collatz")
plt.xlabel("Secuencia N")
plt.ylabel("Cantidad de iteraciones")
plt.show()
