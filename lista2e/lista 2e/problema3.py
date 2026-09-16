#variaveis
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))
num4 = float(input("Informe o quarto número: "))

#condicionais
if num1 == num2 and num3 and num4:
    print ("O primeiro número é repetido.")
elif num2 == num1 and num3 and num4:
    print ("O segundo número é repetido.")
elif num3 == num1 and num2 and num4:
    print ("O terceiro número é repetido.")
elif num4 == num1 and num2 and num3:
    print ("O quarto número é repetido.")
else:
    print ("Todos os números são diferentes.")