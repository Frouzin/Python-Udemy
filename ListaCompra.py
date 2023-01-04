lista = []
listanum = enumerate(lista)

while True:
    condicao = input('selecione uma opção?\n[a]pagar  [l]istar  [i]nserir\n')
    if condicao == 'i':
        lista.append(input('Coloque um item na lista:'))
    if condicao == 'l':
        for i in lista:
            print(enumerate(lista))
    if condicao == 'a':
        lista.pop(input('escolha o indice que vc deseja apagar'))
