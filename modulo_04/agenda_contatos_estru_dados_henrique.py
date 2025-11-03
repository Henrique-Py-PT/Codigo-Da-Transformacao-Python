agenda_de_contatos = {} 

def adicionar_contatos():

    nome = input("digite o nome do contato: ").strip().title()
    telefone = input("digite seu numero de telefone: ").strip()

    agenda_de_contatos[nome] = telefone
    print(f"\ncontato '{nome}' adicionado atualizado com sucesso")

def buscar_contato():
    nome = input("digite o nome do contato para buscar: ").strip().title()
    if nome in agenda_de_contatos:
        telefone = agenda_de_contatos[nome]
        print(f"\n {nome}: {telefone}")
    else:
        print(f"\ncontato '{nome}' nao encontrado na agenda.")


def remover_contato():
    nome = input("digite o nome do contato que deseja remover: ").strip().title()

    if nome in agenda_de_contatos:

        del agenda_de_contatos[nome]
        print(f"\ncontato '{nome}' deletado com sucesso.")
    else: 
        print(f"\ncontato '{nome} nao encontrado. impossivel remover.")

while True: 
     print("\n---- menu da agenda de contatos")
     print("\n1. adicionar contato")
     print("\n2. buscar contato")
     print("\n3. remover contato")
     print("\n4. sair")
     
     escolha = input("digite o numero de sua escolha: ")
     if escolha == '1':
         adicionar_contatos()      
     elif escolha == '2':
         buscar_contato() 
     elif escolha == '3':
        remover_contato()
     elif escolha == '4':
         print("saindo do programa")
         break
     else:
         print("opcao invalida. tente uma opcao valida!")
    
'''verso_flip.png'''








