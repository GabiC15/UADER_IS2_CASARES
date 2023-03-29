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


num = 0
# Si no trae el argumento, lo pide para ingresar
# Si lo trae del "sys.argv" lo extrae
if len(sys.argv) == 1:
    num = int(input("Ingrese un numero: "))
else:
    num = int(sys.argv[1])

print("Factorial ", num, "! es ", factorial(num))
