imc = float(input("Vamos calcular seu índice de massa corporal; Digite seu peso: "))
peso = imc
altura = float(input("Digite sua altura: "))
alt = altura
imc1 = peso / (altura * altura)
if imc1 <= 18.5:
    print("Abaixo do peso!")
elif imc1 <24.9:
    print("Peso ideal, parabéns!")
elif imc1 <29.9:
    print("Levemente acima do peso.")
elif imc1 <30.9:
    print("Obesidade grau 1.")
else:
    print("Obesidade severa/Mórbia.")