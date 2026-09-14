#!/usr/bin/env python3

"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---

    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
    1 x 4 = 4
...
################
---Tabuada do 2---

    2 x 1 = 2
    2 x 2 = 4
    2 x 4 = 8
    2 x 6 = 12
...
#################
"""

__version__ = "0.1.1"
__author__ = "Rogerio"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iterable (percorriveis)
numeros = list(range(1, 11))

# para cada numero em numeros(variavel):

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"), "\N{red apple}")
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)
    print()

