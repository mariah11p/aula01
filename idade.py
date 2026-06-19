
nome = input("Digite seu nome: ")

ano_nascimento = int(input("Digite o ano em que você nasceu: "))

ano_atual = 2026
idade = ano_atual - ano_nascimento

print(f"Olá, {nome}! Você tem ou vai fazer {idade} anos em {ano_atual}.")

if idade >= 18:
    print("Você já é maior de idade!")
else:
    print("Você é menor de idade!")
