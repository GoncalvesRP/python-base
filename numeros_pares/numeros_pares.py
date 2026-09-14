#!/usr/bin/env python3

"""
Faça um programa que imprime os numeros pares de 1 a 200

Ex.
python3 numeros_pares.py
2
4
6
...
"""
for num in range(1, 201): # Iteração de 1 a 200
    if num % 2 == 0: # Condicional para verificar se o número é par
        print(num)
