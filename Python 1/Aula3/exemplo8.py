#divisão inteira e resto
numero1 = float(input("Digite um número para divisão"))
divisor = float(input("Digite o número para dividir"))
divisaoInteira = numero1/divisor
restoDivisao = numero1%divisor

print(f"A divisão do número{numero1}/{divisor}={divisaoInteira}")
print(f"O resto da divisão de{numero1} é {restoDivisao}")