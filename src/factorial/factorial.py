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


hasta = 0
desde = 0
# Si no trae el argumento, lo pide para ingresar
# Si lo trae del "sys.argv" lo extrae
if len(sys.argv) == 1:
    desde = input('Ingrese el numero "desde": ')
    hasta = input('Ingrese el numero "hasta": ')

    # Verifico si el usuario cargo el parametro
    # Si lo cargo lo transformo a entero
    # Si no le asigno "None"
    desde = int(desde) if desde != '' else None
    hasta = int(hasta) if hasta != '' else None
else:
    arg = sys.argv[1]
    args = arg.split('-')
    desde = int(args[0])
    hasta = int(args[1])

for i in range(desde, hasta + 1):
    print(f"Factorial {i}! es", factorial(i))
