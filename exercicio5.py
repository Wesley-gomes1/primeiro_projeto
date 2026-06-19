bruto = float(input("Digíte seu salário bruto: "))
parcela = float(input("Digíte o valor da parcela desejado: "))
maximo = bruto * 0.3
if parcela > maximo:
    print("Crédito negado!")
else:
    print("Acesso liberado!")

