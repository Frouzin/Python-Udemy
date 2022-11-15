name = input('Digite seu nome: ')
altura = (float(input('Digite sua altura: ')))
peso = (float(input('Digite seu peso: ')))
imc = (peso/(altura*altura))

print('{} tem {:.2f} M e pesa {} KG portanto seu imc é {:.1f}'.format(name, altura, peso, imc))

if imc <= 18.5:
    print('Você esta abaixo do peso ideal')
elif imc < 25:
    print('Você está no peso ideal')
elif imc < 30:
    print('Você está com um sobre peso')
elif imc < 40:
    print('Você está Obeso!')
else:
    print('Você está com Obesidade Grave!')
