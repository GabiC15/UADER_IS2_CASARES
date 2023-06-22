# coding=utf-8
"""Programa getJason"""
# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.17 (v2.7.17:c2f86d86e6, Oct 19 2019, 21:01:17)
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
# copyright IS2 © 2022,2023 todos los derechos reservados
import json
import sys

class GetJason(object):
    "Clase GetJason"
    _instance = None

    def __init__(self):
        pass

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def getJason(self):
        "Ejecuta el programa getJason"
        jsonfile = None
        try:
            jsonfile = sys.argv[1]
        except IndexError:
            print "Debe pasar el path del archivo JSON\n"
            return

        jsonkey = "token1"
        if len(sys.argv) > 2:
            jsonkey = sys.argv[2]

        try:
            with open(jsonfile, 'r') as (myfile):
                data = myfile.read()
            obj = json.loads(data)
            print str(obj[jsonkey])
        except IOError:
            print "No se ha encontrado el archivo JSON\n"
            return
        except KeyError:
            print "No existe la clave %s en el archivo JSON\n" % jsonkey
            return

        help_string = "\n <<< HELP >>>\n"\
        "\n Extractor de token para acceso API Servicios Banco XXX (version 1.0)\n"\
        "   Este programa permite extraer la clave de acceso API para utilizar los servicios\n"\
        "   del Banco XXX. El programa opera como un microservicio invocado mediante:\n"\
        "        {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json\n"\
        "        ej.     ./getJason.pyc ./sitedata.json\n"\
        "   El token podra recuperarse mediante el standard output de ejecucion en el formato\n"\
        "       {1.0}XXXX-XXXX-XXXX-XXXX\n"

        if "-h" in sys.argv:
            print help_string
        
        return str(obj[jsonkey])

class Banco:
    _instance = None
    banco = None
    historial = []
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, banco):
        self.banco = banco
    
    def pagar(self, monto = None):
        cuenta1 = Cuenta(1000)
        cuenta2 = Cuenta(2000)

        token = GetJason().getJason()
        print "Se eligio el token: %s" % token

        salir = "Si"
        while salir == "Si":
            if len(sys.argv) > 4:
                monto = sys.argv[4]
            if monto is None:
                monto = input("Ingrese un monto: ")
        
            cuenta1.restar_saldo(monto)
            cuenta2.sumar_saldo(monto)

            self.historial.append("\nPago por $%i\nCuenta 1: $%s\nCuenta 2: $%r\n" % (monto, cuenta1.saldo, cuenta2.saldo))
            
            salir = raw_input("Quiere hacer otro pago (Si/No)? ")
            print(salir)

        for pago in self.historial:
            print(pago)

class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def restar_saldo(self, monto):
        self.saldo -= monto

    def sumar_saldo(self, monto):
        self.saldo += monto

banco = None
if len(sys.argv) > 3:
    banco = sys.argv[3]

print "Se eligio el banco: %s" % banco

Banco(banco).pagar()

print("\n")

print("Se realiza un pago por $500")
Banco(banco).pagar(500)
