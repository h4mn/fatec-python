"""
## Exercício 2: Conversor de Temperatura

Crie um programa que permita ao usuário converter temperaturas de Celsius para Fahrenheit.
Peça ao usuário para inserir uma temperatura em graus Celsius e exiba a temperatura
equivalente em Fahrenheit usando a fórmula: Fahrenheit = (Celsius * 9/5) + 32.
"""

# Pedindo para o usuário inserir uma temperatura em graus Celsius
celsius = float(input("Digite uma temperatura em graus Celsius: "))

# Calculando a temperatura equivalente em Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibindo a temperatura equivalente em Fahrenheit
print(f"{celsius} graus Celsius equivalem a {fahrenheit} graus Fahrenheit.")
