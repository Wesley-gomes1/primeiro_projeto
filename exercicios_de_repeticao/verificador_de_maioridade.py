

quantidade_de_menores = 0
quantidade_de_maiores = 0
for i in range(7):
    ano_de_nasc = int(input("Digite seu ano de nascimento:"))
    if ano_de_nasc <= 2008:
            quantidade_de_maiores +=1
    else:
            quantidade_de_menores +=1

print(f"quantidade de menores : {quantidade_de_menores}")
print(f"quantidade de maiores : {quantidade_de_maiores}")