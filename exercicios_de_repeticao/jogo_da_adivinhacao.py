import random

numero = random.randint(1 , 20)
adivinhacao = 0

while adivinhacao != numero:
    adivinhacao = int(input("Digite um numero que eu pensei: "))
    if adivinhacao < numero:
        print("muito baixo")

    elif adivinhacao > numero:
        print("muito alto, tente de novo")
    else:
        print("Voce acertou!")
        break

