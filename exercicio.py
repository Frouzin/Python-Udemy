num1 = input("digite um numero inteiro: ")

if num1.isdigit():
    num1 = int(num1)
    if num1 % 2 == 0:
        print('este numero é par')
    else:
        print('este numero é impar')
else:
    print('esse valor é invalido, digite outro')
# if par == 0:
#     print('este numero é par')
# else:
#     print('este numero é impar')
