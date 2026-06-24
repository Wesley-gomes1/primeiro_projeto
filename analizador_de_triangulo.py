#Exercício 7: Analisador de Triângulos
#Para exercitar a lógica matemática, peça para o usuário digitar o comprimento de três retas (A, B e C). Primeiro, o programa deve verificar se essas retas podem formar um triângulo
#(Regra: a soma de dois lados deve ser sempre maior que o terceiro). Se formarem, o programa deve usar o elif para dizer que tipo de triângulo ele é:
#Equilátero: todos os lados iguais. • Isósceles: dois lados iguais. • Escaleno: todos os lados diferentes.

A = int(input("Digite o valor da primeira reta para descobrirmos o seu tipo de triângulo: "))
b = int(input("Digite o valor da segunda reta: "))
c = int(input("Digite o valor da terceira reta: "))
soma_dos_lados = A + b
soma_dos_lados = A + c
soma_dos_lados = b + c
if  A + b > c or A +c > c or b + c > A:
    print("valido")
    if A + b == c or b + c == A or  A+c == b:
        print("Isóceles")
    elif A == b and b==c and c== A:
            print("Equilátero")
    else:
        print("Escaleno")
else:
    print("Por favor digite um número valido. somente inteiros!")




