from typing import List

def show_menu():
    print('1. Citire Date. ')
    print('2. DeterminareDeterminare cea mai lunga secventa cu proprietatea ca numerele sunt ordonate crecator. ')
    print(
        '3. Determinare cea mai lunga secventa cu proprietatea ca toate numerele se pot scrie ca x**k, k citit, x întreg pozitiv. ')
    print('4. Iesire. ')


def read_list() -> List[int]:
    lista = []
    lista_str = input('Dati numerele separate prin spatiu: ')
    lista_str_split = lista_str.split(' ')
    for num_str in lista_str_split:
        lista.append(int(num_str))
    return lista


def get_longest_sorted_asc(lst: List[int]) -> List[int]:
    '''
    Determinare cea mai lunga secventa cu proprietatea ca numerele sunt ordonate crescator.
    :param lst: O lista in care se va gasi cea mai lunga secventa cu proprietatea respectiva.
    :return: Cea mai lunga lista cu acea proprietate.
    '''

    lungime = len(lst)
    result = []
    for st in range(lungime):
        for dr in range(st, lungime):
            sorted_asc = True
            for num in lst[st:dr+1]:
                if lst[num] < lst[num - 1]:
                    sorted_asc = False
                    break
                if sorted_asc:
                    if (dr - st + 1) > len(result):
                        result = lst[st:dr + 1]
    return result


def main():
    lista = []
    while True:
        show_menu()
        optiunea = input('Alegeti optiunea: ')
        if optiunea == '1':
            lista = read_list()
        elif optiunea == '2':
            cresc = get_longest_sorted_asc(lista)
            print('Lista cu cele mai multe numere in ordine crescatoare este: ', cresc)
        elif optiunea == '3':
            pass
        elif optiunea == '4':
            break
        else:
            print('Optiune invalida! Incercati alta optiune! ')


if __name__ == '__main__':
    main()
