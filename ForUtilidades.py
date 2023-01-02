for i in range(10):
    if i == 2:
        print('i é igual a 2...')
        continue

    if i == 8:
        print('i igual a 8, parando agora...')
        break

    for j in range(1, 3):
        print(i, j)
    
else:
    print('For completo')

# for i in range(10):
#     if i == 2:
#         print('i é 2, pulando...')
#         continue

#     if i == 8:
#         print('i é 8, seu else não executará')
#         break

#     for j in range(1, 3):
#         print(i, j)
# else:
#     print('For completo com sucesso!')
