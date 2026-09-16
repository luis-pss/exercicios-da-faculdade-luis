#variaveis
A = int(input("primeiro número: "))
B = int(input("segundo número: "))
C = int(input("terceiro número: "))

#condicionais
if A >= 0 and B > A or C % 2 == 0 and C > 10 and (A + B + C) > 100:
    print ("Aprovado.")
else:
    print ("Reprovado.")