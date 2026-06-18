# Casar ou Comprar uma Bicicleta ?
print("casar ou comprar uma bicicleta? ")
resposta = input("você está gordo? s/n ")
if  resposta == "s":
    quer_emagrecer = input("Você quer emagrecer? s/n ")
    if quer_emagrecer == "s":
     print("Compre uma bicicleta!")
    else:
     print("Então case!")
else:
    quer_engordar = input("você quer engordar? s/n ")
    if quer_engordar == "s":
        print("Então case!")
    else:
        print("então compre uma bicicleta!")