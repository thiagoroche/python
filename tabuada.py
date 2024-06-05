#!/usr/bin/env python3
""" imprime a tabuada do 1 ao 10.

---Tabuada do 1---
   
    1 x 1 = 1
    2 x 2 = 2
    3 x 1 = 3
...
###################
---Tabuada do 2---
   
   2 x 1 = 2
   2 x 2 = 4
...
###################
"""
__version__ = "0.0.1"
__Author__ = "Thiago Ferreira"
__License__ = "Free"


#numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1, 11))

#for numero in numeros: 
#    print("Tabuada do:", numero)
#    for outro_numero in numeros:
#        print(numero * outro_numero)
#    print("--------------")

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)
