#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuario uima listas dos quartos disponiveis para alugar e o  preço de cada quarto, esta informação está disponivel em um arquivo de texto separado por virgulas.

'quartos.txt'
# codigo, nome, preço
1,Suite Master,500
2,Quato Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuario o nome, qual o numero do quarto a ser reservado e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

'reservas.txt'
# cliente, quarto, dias
Rogerio,3,12

Se outro usuario tentar resrvar o mesmo quarto o programa deve exibir uma mensagem informando que já esta reservado. 
    
"""
import sys
import os
import logging

ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Arquivo reservas.txt não existe")
    sys.exit(1)

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), #TODO: decimal
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe")
    sys.exit(1)


print("Programa de Reserva Hotel Ptython")
print("-" * 40)

if len(ocupados) == len(quartos):
    print("Todos os quartos ocupados - Hotel lotado")
    sys.exit(1)

nome = input("Nome do cliente: ").strip()
print("-" * 40)
print ("Lista de quartos: ")
for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "👎" if not dados['disponivel'] else "👍"
    # TODO: Substituir casa decimal por virgula
    print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {disponivel}".replace('.', ','))


print("-" * 40)
try:
    num_quarto = int(input("Número do quarto: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} esta ocupado.")
        sys.exit(1)
except ValueError:
    logging.error("Numero inválido, digite apenas digitos.")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe!")
    sys.exit(1)

try:
    dias = int(input("Quantos dias: ").strip())
except ValueError:
    logging.error("Numero inválido, digite apenas digitos.")
    sys.exit(1)    

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_quarto * dias

# print(",".join([nome, str(num_quarto), str(dias)]))

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome},{num_quarto},{dias}\n")

print(f"{nome} você escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}")
