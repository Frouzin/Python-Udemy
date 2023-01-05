import os

lista = []

while True:
    condicao = input('selecione uma opção?\n[i]nserir [a]pagar  [l]istar \n')
    if condicao == 'i':
        os.system('cls')
        item = input('Coloque um item na lista:')
        lista.append(item)
    elif condicao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    elif condicao == 'a':
        indice_apagar = input('digite qual o numero do item que você quer apagar: ')
        
        try:
            indice = str(indice_apagar)
            del lista[indice]
        except:
            print('Não foi possivel apagar esse item!')


        # lista.pop(input('escolha o indice que vc deseja apagar'))
    else:
        os.system('cls')
        print('Escolha as letras [i], [a] ou [l]')
