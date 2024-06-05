#!/usr/bin/env python3
"""Dependendo da lingua configurada no ambiente o programa exibe a
correspondente.

Como usar

Tenha a variavel LAN devidamente configurada ex:
    export LANG=pt_br

Execução:
    python hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__Author__ = "Thiago Ferreira"
__License__ = "Free"

print('thiago' .upper())
print(56 + 7)

import os
current_language = os.getenv("LANG", "pt_BR") [:5]

#Esse script imprimi o Hello World
current_language = "en_US"

#msg = "Hello, World!"

msg = {
    "en_US": "Hello World",
    "pt_BR": "Ola Mundo",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!",
}


print(msg[current_language])
