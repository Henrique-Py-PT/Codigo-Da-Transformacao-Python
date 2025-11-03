numeros = [1, 4, 7, 10, 15, 22, 33, 40]

pares = []
impares = [] 

for numero in numeros:

    if numero % 2 == 0:  
        pares.append(numero)
    else:
        impares.append(numero)

print(f"\n----- resultados -----")
print(f"conjnto original: {numeros}")     
print(f"conjunto de pares: {pares}")
print(f"conjunto de impares: {impares}")   