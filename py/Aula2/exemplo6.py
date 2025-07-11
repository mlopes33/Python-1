print ("Você sabe com quantos anos pode tirar uma CNH?")
nome = input("Qual o seu nome?")
idade = int (input("Qual a sua idade:"))
if (idade>=18):
    print(f"{nome}, você já pode tirar sua CNH!")
else:
    print (f"{nome}, infelizmente você ainda não tem a idade mínima.")