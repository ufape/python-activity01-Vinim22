# -*- coding: utf-8 -*-

# Vinícius Moraes da Silva
# UAG00098
# Problem Set 1 - Problem 6
# Description:


"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
O arquivo de entrada contém três valores inteiros.
7 14 106

Processes:
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

maiorAB = (a + b + abs(a - b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Output(s):
Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.
Exemplo:
O maior número é: 106
"""


def main():
    A = int(input("Digite o valor A: "))
    B = int(input("Digite o valor B: "))
    C = int(input("Digite o valor C: "))
    maiorAB = (A + B + abs(A - B)) /2
    maiorABC = (maiorAB + C + abs(maiorAB - C)) /2
    maior = int(maiorABC)
    print(f"O maior número é: {maior}")
    
      
  


if __name__ == '__main__':
    main()
