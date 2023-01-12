Num_CPF = str(input('DIGITE O NUMERO DO SEU CPF: '))
# print(NoveDigitosCPF_1)

NoveDigitosCPF_1 = Num_CPF[:9]
ContadorR_1 = 10
ResultadoDigito1 = 0

for digito in NoveDigitosCPF_1:
    ResultadoDigito1 += int(digito)*ContadorR_1
    ContadorR_1 -= 1
    digito1 = (ResultadoDigito1 * 10) % 11
    digito1 = digito1 if digito1<= 9 else 0
print('O seu primeiro digito é {}'.format(digito1))

DezDigitosCPF = NoveDigitosCPF_1 + str(digito1)
ContadorR_2 = 11
ResultadoDigito2 = 0

for digito in DezDigitosCPF:
    ResultadoDigito2 += int(digito)*ContadorR_2
    ContadorR_2 -= 1
    digito2 = ResultadoDigito2 * 10 % 11
print('O seu segundo digito é {}'.format(digito2))


CPFGerado = f'{NoveDigitosCPF_1}{digito1}{digito2}'

if CPFGerado == Num_CPF:
    print('Seu CPF é VALIDO!')
else:
    print('Seu CPF Não é Valido!')