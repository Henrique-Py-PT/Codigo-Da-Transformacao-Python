def calcular_media(notas):
    # 1. Verifica se a lista está vazia
    if not notas:
        return "nenhuma nota fornecida"

    media = sum(notas) / len(notas)

    # 3. Define a situação
    if media >= 7.0:
        situacao = "aprovado!!"
    else:
        situacao = "reprovado!!"

    return f"Média: {media:.2f} - Situação: {situacao}"

notas_aluno_b = [5.0, 6.5, 4.0]
print("Aluno B:", calcular_media(notas_aluno_b))