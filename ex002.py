hora=input('Informe a hora do seu relogio: ')

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Horário deve estar entre 0 e 23 horas')
    else:
        if hora <= 11:
            print('Bom dia, são {} horas'.format(hora))
        elif hora <= 17:
            print('Boa Tarde, são {} horas'.format(hora))
        else:
            print('Boa Noite, são {} horas'.format(hora))
else:
    print('Valor Invalido, digite outro numero')


# if hora >= 0 or hora <=11:
#     print('Bom dia, são {} horas' .format(hora))
# else hora >= 12 or hora <= 17:
#     print('Boa Tarde, são {} horas' .format(hora))