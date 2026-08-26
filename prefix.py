#!/usr/bin/env python3

"""Calculadora prefix.
    
Funcionamento:
    
[operação] [n1] [2]

Operações:

sum -> +
sub -> -
mul -> *
div -> /

Uso:

$ python3 prefix.py sum 1 2
3

$ python3 prefix.py mul 10 5
50

$ python3 prefix.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em prefixcal.log"
"""

__version__ = "0.1.1"
__author__ = "Rogerio Goncalves"
__license__ = "Unlicense"   

import os
import sys

from datetime import datetime

arguments = sys.argv[1:]

#TODO: Exception
if not arguments:
    operation = input("operação: ")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Invalid number of arguments")
    print("Exemple: 'sum 5 5'")
    sys.exit(1)
    
operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print(f"Invalid operation")
    print(valid_operations)
    sys.exit(2)

validate_numbers = []
for num in nums:
    # TODO: Repetição while + exception
    if not num.replace('.', '').isdigit():
        print(f"Invalid number: {num}")
        sys.exit(3)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validate_numbers.append(num)

n1, n2 = validate_numbers
# TODO: Usar dic de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":   
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER','anonymous')

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")

print(f"O resultado é {result}")