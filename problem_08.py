

# -*- coding: utf-8 -*-

# Vinícius Moraes da Silva
# UAG00098
# Problem Set 1 - Problem 7
# Description:


"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Seis valores, negativos e/ou positivos.
Exemplo:
Valor (1/6): 7
Valor (2/6): -5
Valor (3/6): 6
Valor (4/6): -3.4
Valor (5/6): 4.6
Valor (6/6): 12

Processes:
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Output(s):
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
Exemplo:
Detectamos 4 valores positivos.
"""


def main():
  positivos = 0  

  for i in range(6):
    valor = float(input(f"Valor ({i+1}/6): "))  
    if valor > 0:  
        positivos += 1  

  print(f"Detectamos {positivos} valores positivos.")


if __name__ == '__main__':
    main()
