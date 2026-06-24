
soma = 0
for impar in range (3, 100, 3):
    if  impar % 2 != 0:
        soma += impar
        print(f"a soma dos ímpares multiplos de 3 é igual a : {impar}")
print(f"soma de todos os ímpares multiplos de 3 é igual a", soma)