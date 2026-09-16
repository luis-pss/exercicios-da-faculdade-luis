#variaveis
M=int(input("primeiro número: "))
N=int(input("segundo número: "))

#condicionais
if N % 5 == 0 and M > 100 or N + M < 200 and N + M >= 0:
    print ("valores aceitos.")
else:
    print ("valores não aceitos.")