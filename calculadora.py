#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 4:
    print
    sys.exit("Error al introducir los comandos")
function = sys.argv[1]
operando1 = sys.argv[2]
operando2 = sys.argv[3]


def sumar(a, b):
    return float(a) + float(b)


def restar(a, b):
    return float(a) - float(b)


def dividir(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        sys.exit("Error: intentar dividir entre cero")


def multiplicar(a, b):
    return float(a) * float(b)


try:

    if (function == "sumar"):
        print str(operando1) + " + " + str(operando2) + \
                  " = " + str(sumar(operando1, operando2))

    elif (function == "restar"):
        print str(operando1) + " - " + str(operando2) + \
                  " = " + str(restar(operando1, operando2))

    elif (function == "multiplicar"):
        print str(operando1) + " x " + str(operando2) + \
                  " = " + str(multiplicar(operando1, operando2))

    elif (function == "dividir"):
        print str(operando1) + " / " + str(operando2) + \
                 " = " + str(dividir(operando1, operando2))


except ValueError:
        sys.exit("Error: solo pueden sumarse números")
