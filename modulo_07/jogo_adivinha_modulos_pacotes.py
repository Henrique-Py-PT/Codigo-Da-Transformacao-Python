import random
import math

def jogar_adivinhacao():
    print("\n--- Jogo de Adivinhação ---")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 7
    
    print(f"Adivinhe o número secreto entre 1 e 100. Você tem {max_tentativas} tentativas!")

    while tentativas < max_tentativas:
        try:
            chute = int(input("Seu chute: "))
        except ValueError:
            print("erro. Digite um número inteiro.")
            continue
        
        tentativas += 1

        if chute == numero_secreto:
            print(f"🎉 **Parabéns!** Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            return
        elif chute < numero_secreto:
            print("Seu chute foi **baixo**! Tente um número maior.")
        else:
            print("Seu chute foi **alto**! Tente um número menor.")
            
        print(f"Tentativas restantes: {max_tentativas - tentativas}")

    print(f"\nGame Over! O número secreto era **{numero_secreto}**.")

jogar_adivinhacao()