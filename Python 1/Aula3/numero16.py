#Calculo do IMC

peso = float(input("Digite seu peso em kg:"))
altura = float(input("Digite sua altura:"))
imc = peso/ (altura**2)
if (imc<18):
    print("Você está abaixo do peso:")
elif(imc>18.5 and imc==24.9):
    print("Você está no peso ideal")
elif(imc==25):
    print("Você está com sobrepeso")
else:
    print("Você está com Obesidade")