#variaveis
nota = int(input("Digite a sua nota: "))
status = input("Qual o seu status atual (ativo ou inativo)? ")
turma = input("Qual sua turma (manhã, tarde, noite)? ")
matricula = input("Digite o número de sua matrícula: ")

#condicionais
if nota >= 7 and status == "ativo" or turma is not "noite" and matricula > 1000:
    print ("Aluno aprovado.")
else:
    print ("Aluno reprovado.")