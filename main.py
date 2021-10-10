from typing import List


def show_menu():
    print('1. Citire Date. ')
    print('2. Determinare cea mai lunga secventa cu proprietatea ca numerele sunt palindrome. ')
    print('3. Determinare cea mai lunga secventa cu proprietatea ca numerele sunt formate din cifre prime ')
    print('4. Iesire. ')


def read_list() :
    lista = []
    lista_str = input('Dati numerele separate prin spatiu: ')
    lista_str_split = lista_str.split(' ')
    for num_str in lista_str_split:
        lista.append(int(num_str))
    return lista


def is_palindrome(n: int) -> bool:
    '''
    Determina daca un numar dat n este palindrom
    :param n: nr. intreg
    :return: True daca numarul dat este palindrom, False in caz contrar
    '''
    n = abs(n)
    invers = 0
    copie_n = n
    while copie_n != 0:
        invers = invers * 10 + copie_n % 10
        copie_n = copie_n // 10
    while n != 0:
        if n % 10 != invers % 10:
            return False
        n = n // 10
        invers = invers // 10
    return True


def test_is_palindrome():
    assert is_palindrome(-7) == True
    assert is_palindrome(9) == True
    assert is_palindrome(21) == False
    assert is_palindrome(4554) == True
    assert is_palindrome(456) == False


def get_longest_all_palindromes(lst: List[int]) -> List[int]:
    '''

    :param lst:
    :return:
    '''
    lungime = len(lst)
    result = []
    for st in range(lungime):
        for dr in range(st, lungime):
            if is_palindrome(lst[dr]) == True and len(lst[st:dr + 1]) > len(result):
                result = lst[st:dr + 1]
    return result


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([5, 6, 7, 12, 11, 11, 44, 55, 45, 55, 33, 343]) == [11, 11, 44, 55]


def is_prime(n: int) -> bool:
    '''
    Determina daca un numar dat n este prim.
    :param n: numar intreg dat
    :return: Treu daca n este prime, False in caz contrar
    '''
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(11) == True
    assert is_prime(18) == False


def all_numbers_prime(lst: List(int)) -> bool:
    '''
    Determina daca fiecare cifra a numarului n este prima
    :param n: numarul dat
    :return: True daca fiecare cifra a lui n este prima, False in caz contrar
    '''
    for n in lst:
        while n != 0:
            if is_prime(n % 10) == False:
                return False
            n = n // 10
    return True


def test_all_numbers_prime():
    assert all_numbers_prime([25, 55, 77]) == True
    assert all_numbers_prime([12, 13, 14, 15]) == False
    assert all_numbers_prime([35, 37, 52]) == True
    assert all_numbers_prime([123, 124, 125, 126]) == False


def get_longest_prime_digits(lst: List[int]) -> List[int]:
    '''

    :param lst:
    :return:
    '''
    lungime = len(lst)
    result = []
    for st in range(lungime):
        for dr in range(st, lungime):
            if all_numbers_prime(lst[st:dr + 1]) == True and len(lst[st:dr + 1]) > len(result):
                result = lst[st:dr + 1]
    return result


def main():
    lista = []
    while True:
        show_menu()
        print()
        optiunea = input('Alegeti optiunea: ')
        print()
        if optiunea == '1':
            lista = read_list()
        elif optiunea == '2':
            print('Lista cu cele mai multe numere palindrom este: ', )
        elif optiunea == '3':
            print('Lista cu cele mai multe numere ale caror cifre sunt numere prime: ', get_longest_prime_digits(lista))
        elif optiunea == '4':
            break
        else:
            print('Optiune invalida! Incercati alta optiune! ')


if __name__ == '__main__':
    test_is_palindrome()
    test_is_prime()
    test_all_numbers_prime()
    main()
