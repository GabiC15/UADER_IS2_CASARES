# coding=utf-8
# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.17 (v2.7.17:c2f86d86e6, Oct 19 2019, 21:01:17) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import json, sys

jsonfile = None
try:
    jsonfile = sys.argv[1]
except IndexError:
    print("Debe pasar el path del archivo JSON\n")
    raise

jsonkey = "token1"
if len(sys.argv) > 2:
    jsonkey = sys.argv[2]

try:
    with open(jsonfile, 'r') as (myfile):
        data = myfile.read()
    obj = json.loads(data)
    print str(obj[jsonkey])
except IOError:
    print("No se ha encontrado el archivo JSON\n")
    raise
except KeyError:
    print("No existe la clave %s en el archivo JSON\n" % jsonkey)
    raise

help =  "\n <<< HELP >>>\n"\
        "\n Extractor de token para acceso API Servicios Banco XXX (version 1.0)\n"\
        "   Este programa permite extraer la clave de acceso API para utilizar los servicios del Banco XXX.\n"\
        "   El programa opera como un microservicio invocado mediante:\n"\
        "        {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json\n"\
        "        ej.     ./getJason.pyc ./sitedata.json\n"\
        "   El token podra recuperarse mediante el standard output de ejecucion en el formato\n"\
        "       {1.0}XXXX-XXXX-XXXX-XXXX\n"

if "-h" in sys.argv:
    print(help)
