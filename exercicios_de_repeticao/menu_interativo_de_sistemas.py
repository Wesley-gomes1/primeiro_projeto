# \n or """
while True: #while True nao precisa de variavel
    opcao = int(input("""    1 - Somar
    2 - subtrair 
    3 - multiplicar
    4 - dividir
    5 - sair
    Digite uma opção: """))
    if opcao == 5:
        print("saindo...")
        break
