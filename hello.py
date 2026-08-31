#!/usr/bin/env python3
"""Hello World multi language.
Depending on the language configured in the environment, the program displays 
the corresponding message.

Usage:
Ensure the LANG variable is properly configured. E.g.:
   export LANG=pt_BR
Execution:
   python3 hello.py
   or
   ./hello.py
"""

__version__ = "0.1.3"
__author__ = "Rogerio Goncalves"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:

   try:
      key, value = arg.split("=")
   except ValueError as e:
      # TODO: Logging
      print(f"[ERROR] {str(e)}")
      print("You need to use '=' ")
      print(f"You passed {arg}")
      print("try with --key=value")
      sys.exit(1)
      
   key = key.lstrip("-").strip()
   value = value.strip()
   
   # Valadation
   if key not in arguments:
      print(f"Invalid Option '{key}'")
      sys.exit()
   arguments[key] = value
   
current_language = arguments["lang"]
if current_language is None:
   #TODO: Usar repetição
   if "LANG" in os.environ:
      current_language = os.getenv("LANG")
   else:
      current_language = input("Please, inform the language (e.g.: en_US): ")

current_language = current_language[:5]

msg = {
   "en_US": "Hello World!",
   "pt_BR": "Olá, Mundo!",
   "it_IT": "Ciao, Mondo!",
   "es_ES": "Hola, Mundo!",
   "fr_FR": "Bonjour Monde!"
}

"""
# try com valor default
message = msg.get(current_language, msg["en_US"])
"""

# EAFP
try:
   message = msg[current_language]
except KeyError as e:
   print(f"[ERROR] {str(e)}")
   print(f"Language is invalid, choose from: {list(msg.keys())}")
   sys.exit(1)

print(
   message * int(arguments["count"])
) 

