#Exercício 8: Calculadora de Desconto de Black Friday
#Enunciado: Uma loja de departamento está aplicando descontos progressivos baseados no valor total da compra do cliente. Escreva um script que leia o valor total das compras e aplique o desconto correto usando a estrutura condicional:
#Compras até R$ 100,00: Sem desconto. • Compras de R$ 100,01 até R$ 300,00: 5% de desconto. • Compras de R$ 300,01 até R$ 500,00: 10% de desconto. •
#Compras acima de R$ 500,00: 15% de desconto. Ao final, exiba o valor original, o valor do desconto aplicado e o total a pagar com desconto.

promocao = float(input("Digite o valor total da sua compra para verificarmos o seu desconto: "))
desconto5 = promocao * 0.5
desconto10 = promocao * 0.10
desconto15 = promocao * 0.15
if promocao <= 100:
    print("Não tem desconto!")
elif desconto5<= 300:
    print(f"sua compra foi de {promocao} com desconto de {desconto5} no total de {promocao - desconto5}")
elif desconto10:
    print(f"sua compra foi de {promocao} com desconto de {desconto10} no total de {promocao - desconto10}")
else:
    print(f"sua compra foi de {promocao} com desconto de {desconto15} no total de {promocao - desconto15}")

