#!/usr/bin/env python3
"""Exibe relatorio de criaças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada um das atiidades.

"""
__version__ = "0.1.1"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos","Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca =  ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Musica", aula_musica),
    ("Danca", aula_danca)
]

# Requisitos
# 1 Lista alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)
    
    # Sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(set(atividade))

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)
    
    print()
    print("-" * 40)