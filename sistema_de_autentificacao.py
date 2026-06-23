#Exercício 9: Sistema de Autenticação com Operadores Lógicos
#Crie um sistema de login que exija duas informações: o nome de usuário (string) e a chave de segurança token (número inteiro). O acesso só deve ser concedido se o usuário for exatamente "admin"
#E o token for igual a 9988. Se um dos dois dados (ou ambos) estiver incorreto, o programa deve exibir "Dados de acesso inválidos".

usuario = str(input("Digite seu login: "))
usuario1 = "admin"
senha = 9988
if usuario == usuario1:
    print("bem-vindo!")
    senha = int(input("Agora digite sua senha: "))
    if senha == 9988:
        print("Seja bem-vindo!")

else:
    print("Dados de acesso inválidos!")