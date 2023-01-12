Num_CPF = str(input('DIGITE O NUMERO DO SEU CPF: '))
NoveDigitosCPF_1 = Num_CPF[:9]
DezDigitosCPF = Num_CPF[:10]
# print(NoveDigitosCPF_1)
ContadorR_1 = 10
ContadorR_2 = 11
print(DezDigitosCPF)
ResultadoDigito1 = 0
ResultadoDigito2 = 0
for digito in NoveDigitosCPF_1:
    ResultadoDigito1 += int(digito)*ContadorR_1
    ContadorR_1 -= 1
    digito1 = ResultadoDigito1 * 10 % 11
print('O seu primeiro digito é {}'.format(digito1))
for digito in DezDigitosCPF:
    ResultadoDigito2 += int(digito)*ContadorR_2
    ContadorR_2 -= 1
    digito2 = ResultadoDigito2 * 10 % 11
print('O seu segundo digito é {}'.format(digito2))