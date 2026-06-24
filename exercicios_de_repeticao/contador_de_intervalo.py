numero = int(input("Digite seu número inicial para determinar seu intervalo: "))
final = int(input("Digite seu valor final: "))
intervalo = int(input("Digite o seu intervalo: "))
for i in range(numero, final,  intervalo):
    print(f"Seu intervalo customizado é {i}")