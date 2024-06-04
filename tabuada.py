#!/usr/bin/env python3
""" imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
-------------
Tabuada do 2
2
4
...
--------------
"""
__version__ = "0.0.1"
__Author__ = "Thiago Ferreira"
__License__ = "Free"

#base = [1,2,3,4,5,6,7,8,9,10]
base = list(range(1, 11))

for numero in base: 
    print("Tabuada do:", numero)
    for outro_numero in base:
        print(numero * outro_numero)
    print("--------------")
#print(base)
