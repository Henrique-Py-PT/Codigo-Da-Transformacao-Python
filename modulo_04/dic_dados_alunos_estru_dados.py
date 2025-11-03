print("----------_----------_------")
print(" seja bem vindo ao CDT")
print("----------_----------_------")


aluno = {

"nome": "cleiton",
"idade": "20",
"notas": [1.7, 10, 8,0]

}

print("historico de notas do aluno")

print(f"nome: {aluno['nome']}")
print(f"idade: {aluno['idade']} anos")

media_notas = sum(aluno['notas']) / len(aluno['notas'])

print(f"media das notas: {media_notas: : .2f}")

print("---------------------------------------")

print(f"notas: {aluno['notas']}")


print("todas as informacoes")

for chave, valor in aluno.items():
    print(f"{chave.captalize}(): {valor}")
