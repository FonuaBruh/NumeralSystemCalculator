# Список индексов
def transfer_number_into_index(n):
    digits = u'\u2080 \u2081 \u2082 \u2083 \u2084 \u2085 \u2086 \u2087 \u2088 \u2089'.split()
    index = ''
    for _, d in enumerate(str(n)):
        index += digits[int(d)]
    return index

# Конвертирует число с любым основанием
def convert_numeral_systems(from_base, n, to_base):
    n = base_to_dec(n, from_base)
    return dec_to_base(n, to_base)

# Конвертирует число в dec
def base_to_dec(n, base):
    return int(n, base)

# Конвертирует число из dec
def dec_to_base(n, base):
    abc = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x, y = divmod(n, base)
    return dec_to_base(x, base) + abc[y] if x else abc[y]

# Ввод числа
def input_n(base):
    abc = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while True:
        n = input()
        for c in n:
            if c.upper() not in abc:
                print('ОШИБКА: число может содержать только арабские цифры и символы английского алфавита.\n')
                break
            if c.upper() not in abc[:base]:
                print(f'ОШИБКА: число {n} не может быть в системе счисления с основанием {base}.\n')
                break
        break
    print()
    return n.upper()

# Ввод основания
def input_base():
    while True:
        base = input()
        if base.isdigit() and 2<= int(base) <= 36:
            break
        else:
            print('ОШИБКА: основание может быть целым числом от 2 до 36.\n')
    print()
    return int(base)

# Главное меню
def main_menu():
    print('- ' * 30)
    print('Добро пожаловать в конвертер систем счисления!')
    print('Программа поддерживает системы счисления с основаниями от 2 до 36.')
    print('- ' * 30 + '\n')
    print('Введите основание системы счисления числа, которое необходимо конвертировать.')
    from_base = input_base()
    print('Введите число, которое необходимо конвертировать.')
    n = input_n(from_base)
    print('Введите основание конечной системы счисления.')
    to_base = input_base()
    print('-  ' * 10)
    print('Число было успешно сконвертировано:')
    print(f'{n + transfer_number_into_index(from_base)} = {convert_numeral_systems(from_base, n, to_base) + transfer_number_into_index(to_base)}')

main_menu()