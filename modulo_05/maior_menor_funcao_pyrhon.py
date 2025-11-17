def maior_menor(lista_de_numeros):
   
    if not lista_de_numeros:
        return None, None
    
    maior = max(lista_de_numeros)
    menor = min(lista_de_numeros)

    return maior, menor

# Exemplo de uso:
numeros = [12, 5, 45, 8, 23, 1]
maior, menor = maior_menor(numeros)

print(f"Lista: {numeros}")
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")