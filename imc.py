print("Sistema de calculo de IMC")
#Pedir a altura
altura = float(input('Digite sua Altura (m): '))
#PEdir o peso
peso = float(input('Digite seu peso (kg): '))

#Calcular o IMC -> Peso / Altura²
imc = peso / (altura*altura)

print("IMC: ", imc)

if imc <= 18.5:
    print("Baixo Peso")
elif imc > 18.5 and imc < 25: 
    print("Peso Normal")
#entre 25 e 29.9 -> Sobrepeso
#entre 30 e 34.9 -> Obesidade grau I
#entre 35 e 39.9 -> obesidade grau II
#maior que 40 -> obesidade grau III