#!/usr/bin/env python3
"""
Alerta de temperatura

Faça um script que pergunta ao usuario qual a temperatura 
atual e o indice de umidade do ar sendo que caso será 
exibida uma mensagem de alerta dependendo das condições:

Se temp maior 45: ALERTA!!! Perigo calor extremo.
Senão temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor umido.
... temp entre 10 e 30 graus: Normal!!!
... temp entre 0 e 10 graus: Frio!!!
... temp abaixo de 0: ALERTA!!! Frio extremo.
"""

import sys
import logging
log = logging.getLogger("alerta")

info = {
    
    "temperatura": None,
    "umidade": None
}
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual {key}? ").strip())
    except ValueError:
        log.error(f"({key.capitalize()}) inválida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

if temp >  45:
    print("ALERTA!!! 🥵 Perigo, calor extremo.")
elif temp * 3 >= umidade:
    print("ALERTA!!! 🥵 Perigo, tempo úmido.")
elif temp >= 10 and temp <= 30:
    print("NORMAL!!! Normal, temperatura agradável.")
elif temp >= 0 and temp <= 10:
    print("FRIO!!! Frio, temperatura baixa.")
elif temp < 0:
    print("ALERTA DE FRIO!!! 🥶 Frio extremo.")