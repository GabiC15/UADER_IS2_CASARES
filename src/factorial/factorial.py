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
    desde = input("Ingrese el numero desde: ")
    hasta = input("Ingrese el numero hasta: ")

    # Verifico si el usuario cargo el parametro
    # Si lo cargo lo transformo a entero
    # Si no le asigno "None"
    desde = int(desde) if desde != '' else None
    hasta = int(hasta) if hasta != '' else None
else:
    arg = sys.argv[1]
    args = arg.split('-')
    if args.count("") > 0:
        args.remove("")  # Elimino el caracter vacio ("")
    # En base a la cantidad de argumentos puede tomar dos caminos
    if (len(args) == 2):
        # Ya que contiene dos argumentos indica todo el rango
        desde = int(args[0])
        hasta = int(args[1])
    else:
        # Como no trae ambos argumentos inferimos con
        # condicionales si trae el "desde" o el "hasta"
        desde = int(args[0]) if arg[0] != "-" else None
        hasta = int(args[0]) if arg[-1] != "-" else None

# Si las variables son None, establezco los
# limites inferior y superior de la consigna
if (hasta is None):
    hasta = 60
if (desde is None):
    desde = 1

for i in range(desde, hasta + 1):
    print(f"Factorial {i}! es", factorial(i))
