def cesar(op):
    cont = 0
    c = 0
    over = 0
    nova = ''

    if op == '1':
        alf = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z')
        palavra = input('Informe a palavra a ser codificada.\n')
        cod = int(input('Informe a quantidade de casas a serem avançadas.\n'))

    elif op == '2':
        alf = ('z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
        'd', 'c', 'b', 'a')
        palavra = input('Informe a palavra a ser decodificada.\n')
        cod = int(input('Informe a quantidade de casas a serem retrocedidas.\n'))

    cod2 = cod
    palavra = palavra.lower()
    palavra = normalize('NFKD', palavra).encode('ASCII', 'ignore').decode('ASCII')
    compr = len(palavra)

    while cont != compr:

        if palavra[cont] in alf:
            while alf[c] != palavra[cont]:
                c += 1

            while c + cod2 > 25:
                cod2 -= 1
                over += 1

            while over > 26:
                over -= 26

            if over != 0:
                subs = alf[over - 1]

            else:
                subs = alf[c + cod]

        elif(palavra[cont] == ' '):
            subs = ' '

        else:
            subs = palavra[cont]

        nova += subs
        cont += 1
        c = 0
        over = 0
        cod2 = cod

    return (nova)

from unicodedata import normalize

op = input('Qual operação deseja realizar? \n1 - Codificar \n2 - Decodificar \n')

while op != '1' and op != '2':
    op = input('Escolha uma operação válida.\n')

print(cesar(op))
