#variaveis
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")
curso = input("Digite seu curso: ")
nome = input("Digite seu nome: ")

#condicionais
if idade > 18 and cidade == ("Mogi") or curso == ("ADS") or curso == ("RH") and not nome.startswith("Z"):
    print ("Cadastro válido.")
else:
    print ("Cadastro inválido.")