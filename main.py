def get_longest_sorted_asc(lst: list[int]):
    '''
    Determinare cea mai lunga secventa cu proprietatea ca numerele sunt ordonate crescator.
    :param lst: O lista in care se va gasi cea mai lunga secventa cu proprietatea respectiva.
    :return: Cea mai lunga lista cu acea proprietate.
    '''
    lista_definitiva = []
    lista_temporara = []
    lista_definitiva.append(lst[0])
    contor = 1
    crescator = 1
    while crescator == 1:
        if lst[contor] >= lst[contor - 1]:
            lista_definitiva.append(lst[contor])
            contor += 1
        else:
            crescator = 0
    contor += 1
    while contor != len(lst):
        crescator = 1
        while crescator == 1:
            if lst[contor] >= lst[contor - 1]:
                lista_temporara.append(lst[contor])
                contor += 1
            else:
                crescator = 0
            if contor == len(lst):
                crescator = 0
        if len(lista_temporara) > len(lista_definitiva):
            lista_definitiva = lista_temporara
    return lista_definitiva


def test_get_longest_sorted_asc():
    lst = [1, 2, 3, 2, 3, 4, 5, 3, 4, 5, 6, 7]
    assert get_longest_sorted_asc(lst) == [3, 4, 5, 6, 7]


def main():
    lista_str = input('1. Citire date. Introduceti un sir de numere separate prin spatiu: ')
    lista_str_split = lista_str.split(' ')
    lista_int = []
    for lst_str in lista_str_split:
        lista_int.append(int(lst_str))
    print('2. Determinare cea mai lunga secventa cu proprietatea ca numerele sunt ordonate crecator: ')
    print(get_longest_sorted_asc(lista_int))
    print(
        '3. Determinare cea mai lunga secventa cu proprietatea ca toate numerele se pot scrie ca x**k, k citit, x întreg pozitiv')
    print('4. Iesire')


test_get_longest_sorted_asc()
main()
