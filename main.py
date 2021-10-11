from typing import List


def show_menu():
    print('1. Citire Date. ')
    print('2. Determinare cea mai lunga secventa cu proprietatea ca numerele sunt palindrome. ')
    print('3. Determinare cea mai lunga secventa cu proprietatea ca numerele sunt formate din cifre prime ')
    print('4. Iesire. ')


def read_list():
    lista = []
    lista_str = input('Dati numerele separate prin spatiu: ')
    lista_str_split = lista_str.split(' ')
    for num_str in lista_str_split:
        lista.append(int(num_str))
    return lista


def is_palindrome(lst: List[int]) -> bool:
    '''
    Determina daca un o lista data are toate elementele palindrom.
    :param lst: o lista data
    :return: True daca lista data are toate elementele palindrom, False in caz contrar.
    '''
    for n in lst:
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
    assert is_palindrome([5, 11, 44]) == True
    assert is_palindrome([5, 55, 555, 5555]) == True
    assert is_palindrome([1, 2, 12]) == False
    assert is_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert is_palindrome([11, 33, 44, 55, 66, 78]) == False


def get_longest_all_palindromes(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa cu elemente palindrom.
    :param lst:O lista data.
    :return: Cea mai lunga subsecventa cu elemente palindrom.
    '''
    lungime = len(lst)
    result = []
    for st in range(lungime):
        for dr in range(st, lungime):
            if is_palindrome(lst[st:dr + 1]) and len(lst[st:dr + 1]) > len(result):
                result = lst[st:dr + 1]
    return result


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([5, 6, 7, 12, 11, 11, 44, 55, 45, 55, 33, 343]) == [11, 11, 44, 55]
    assert get_longest_all_palindromes([11, 12, 13, 1, 2, 3, 42, 24, 1, 2, 3, 4]) == [1, 2, 3, 4]
    assert get_longest_all_palindromes([111, 121, 131, 212, 234, 333, 444, 545, 13]) == [111, 121, 131, 212]


def is_prime(n: int) -> bool:
    '''
    Determina daca un numar dat n este prim.
    :param n: numar intreg dat.
    :return: Treu daca n este prime, False in caz contrar.
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


def all_numbers_prime(lst: List[int]) -> bool:
    '''
    Determina daca fiecare cifra a elementelor unei liste sunt prime.
    :param lst: O lista data.
    :return: True daca fiecare cifra a elemntelor listei sunt prime, False in caz contrar.
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


def get_longest_prime_digits(lst):
    '''
    Determina cea mai lunga subsecventa a carei elemente are toate cifrele prime.
    :param lst: Lista data.
    :return:Cea mai lunga subsecventa a carei elemente are toate cifrele prime
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
            print('Lista cu cele mai multe numere palindrom este: ', get_longest_all_palindromes(lista))
        elif optiunea == '3':
            print('Lista cu cele mai multe numere ale caror cifre sunt numere prime: ', get_longest_prime_digits(lista))
        elif optiunea == '4':
            break
        else:
            print('Optiune invalida! Incercati alta optiune! ')


if __name__ == '__main__':
    test_is_palindrome()
    test_get_longest_all_palindromes()
    test_is_prime()
    test_all_numbers_prime()
    main()
