senha_correta = 123456

for i in range (2,-1,-1):
    senha_digitada = int(input("Digite sua senha: "))
    if senha_digitada == senha_correta:
        print("Acesso Permitido")
        break
    else:
         print("Conta Bloqueada")

