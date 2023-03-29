#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * calcula el factorial de un número                                       *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*
import sys


def factorial(num):
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


desde = 0
hasta = 0
# Si no trae el argumento, lo pide para ingresar
# Si lo trae del "sys.argv" lo extrae
if len(sys.argv) == 1:
    desde = int(input("Ingrese el numero inicial: "))
    hasta = int(input("Ingrese el numero final: "))
else:
    desde = int(sys.argv[1])
    hasta = int(sys.argv[2])

for i in range(desde, hasta + 1):
    print(f"Factorial {i}! es", factorial(i))
