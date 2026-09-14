#!/usr/bin/env pytho3
""" Cadastro de produtos """
__version__ = "0.1.0"

print()

from pprint import pprint

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 10.0,
        "profundidade": 1.0
    },
    "em_estoque": True,
    "codigo": 123456,
    "codigo_barras": "1234567890123"
}

cliente = {
    "nome": "Rogerio"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}

# pprint(compra)

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra ['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de R$ {total_compra}"
)
