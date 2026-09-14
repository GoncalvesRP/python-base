#!/usr/bin/env python3

"""
Repete vogais

Faça um programa que pode ao usuario que gigite uma ou mais palavras e imprima cada uma das palavras 
com suas vogais duplicadas.

Exemplo:
python3 repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Rogerio
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Rogrioo   
    
"""
import sys 
import logging


words = []
while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    if not word:
        break
    
    final_word = ""
    for letter in word:
        # TODO: Remover acentos das vogais usando função
        
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
        
        # If ternario alternativo
        # final_word += letter * 2 if letter.lower() in "aeiouãáàâä" else letter
        
    words.append(final_word)

print(*words, sep="\n")
# for word in words:
#     print(word)