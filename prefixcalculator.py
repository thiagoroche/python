#!/usr/bin/env python3
""" Calculadora Infix

Funcionamento:

[operacação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalculator.py sum 5 2
7

$ prefixcalculator.py sum 10 5
50

$ prefixcalculator.py
operação: sum
n1: 5
n2: 4
9
"""

___version___ = "0.1.0"

import sys
arguments = sys.argv[1:]


if not arguments:
    operation = input("operação:")
    n1 = input ("n1:")
    n2 = input ("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Numero de Argumentos Invalidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação invalida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero Invalido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O Resultado é {result}")
