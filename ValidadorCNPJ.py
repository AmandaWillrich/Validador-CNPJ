cnpj = input('Digite um CNPJ: ')
#cnpj = '04.252.011/0001-10'

def remover(cnpj):
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    return cnpj

cnpj_numbers = remover(cnpj)

new_cnpj = cnpj_numbers[:-2]

sum1 = 0
acumulador1 = 0
sequence1 = 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2

for sum_first_digit in sequence1:
    sum1 += int(new_cnpj[acumulador1]) * sum_first_digit

    acumulador1 += 1

first_digit = 11 - (sum1 % 11)

def check_digit(first_digit):
    if first_digit >= 9:
        return 0
    else:
        return first_digit

final_first_digit = check_digit(first_digit)
cnpj_with_one_digit = f'{new_cnpj}{final_first_digit}'

sum2 = 0
acumulador2 = 0
sequence2 = 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2

for sum_second_digit in sequence2:
    sum2 += int(cnpj_with_one_digit[acumulador2]) * sum_second_digit

    acumulador2 += 1

second_digit = 11 - (sum2 % 11)

final_second_digit = check_digit(second_digit)

final_cnpj = f'{new_cnpj}{final_first_digit}{final_second_digit}'

def validate_cnpj(final_cnpj):
    if final_cnpj == cnpj_numbers:
        return f'O CNPJ {final_cnpj} é válido!'
    else:
        return f'O CNPJ {final_cnpj} não é válido! Digite um CNPJ válido.'

final = validate_cnpj(final_cnpj)
print(final)