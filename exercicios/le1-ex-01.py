"""
Exercício 01 - Verificador de Idade

Peça ao usuário para inserir sua idade e, em seguida, informe se a pessoa é maior de idade (idade maior ou igual a 18 anos) ou menor de idade.
"""

# Pedindo para o usuário inserir sua idade
idade = int(input("Digite sua idade: "))

# Informando se o usuário é maior de idade (>=18) ou menor de idade
if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")