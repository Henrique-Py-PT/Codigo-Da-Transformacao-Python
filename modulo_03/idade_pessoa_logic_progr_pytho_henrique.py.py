print("*****************************")
print("seja bem vindo ao CDT")
print("****************************")


nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))


if idade <= 10:
    print("olá, {nome}!! você é uma crinça.")

elif idade <= 17:
    print(f"olá, {nome}!!! Você é um adolescente.") 
    
elif idade <= 59:
    print(f"olá, {nome}!! Você é adulto.")

else:
    print(f"olá, {nome}! Você é um idoso.")