ano_de_nasc = int(input("Digíte o ano de seu nascimento para liberarmos acesso:"))

ano_de_nasc = 2026 - ano_de_nasc
if ano_de_nasc >=16:
    print("Acesso ao filme liberado!")
else:
    print("Acesso bloqueado: Conteúdo não recomendado para menores de 16 anos!!")