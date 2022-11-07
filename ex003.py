name = input('Digite seu nome: ')
range = len(name)
if range <= 4:
    print('Seu nome é curto')
elif range <= 6:
    print('seu nome é normal! ')
else:
    print('seu nome é grande')
