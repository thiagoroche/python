#!/usr/bin/env python3
""" Hello World Multi Linguas
Dependendo da lingua configurada no ambiente o programa exibe a
correspondente.

Como usar

Tenha a variavel LAN devidamente configurada ex:
    export LANG=pt_br

Execução:
    python hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__Author__ = "Thiago Ferreira"
__License__ = "Free"

print('thiago' .upper())
print(56 + 7)

import os
current_language = os.getenv("LANG") [:5]

#Esse script imprimi o Hello World
current_language = "en_US"

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "en_SP":
    msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"



print(msg)


#print("Hello, World!")
