from selectors import SelectSelector

nota1 = float(input("Digite sua primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
if media >= 7 :
    print(f"Aluno aprovado com média {media: .2f}" )

elif media >= 3 and media < 7:
    print (f"Aluno em recuperação com média {media: .2f}")
    fez_recuperacao = input("Aluno já fez  a recuperação? s/n: ")
    if fez_recuperacao == "s":
        nota_recuperacao = float(input("digite a nota da recuperação: "))
        if nota_recuperacao >= 5:
            print("Aluno aprovado pela recuperaçãa")
        else:
            print("Aluno não obteve nota suficiente para ser aprovado após a recuperação.")
    else:
        print("Aluno ainda não fez a recuperação")
else:
    print(f"Aluno reprovado com média {media: .2f}" )
