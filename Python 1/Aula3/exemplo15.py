#Maior número
numero = int(input("Digite um número:"))
numero1 = int(input("Digite outro número:"))

if (numero> numero1):
    print (f"Maior número é {numero}")
elif(numero ==  0 and numero1 == 0):
    print("Você digitou dois números 0")
else:
    print(f"O maior número é {numero1}")