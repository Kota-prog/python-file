import sys


def calc_addition(first_number, second_number):
    addition_result = first_number + second_number

    return addition_result


def calc_subtraction(first_number, second_number):
    subtraction_result = first_number - second_number

    return subtraction_result


def calc_multiplication(first_number, second_number):
    multiplication_result = first_number * second_number

    return multiplication_result


def calc_division(first_number, second_number):
    division_result = first_number / second_number

    return division_result


def show_results(addition_result, subtraction_result, multiplication_result, division_result):

    print(f'addition : {addition_result}')
    print(f'subtraction : {subtraction_result}')
    print(f'multiplication : {multiplication_result}')
    print(f'division : {division_result}')


def main():
    imput_first_number = sys.argv[1]
    imput_second_number = sys.argv[2]

    imput_first_number = float(imput_first_number)
    imput_second_number = float(imput_second_number)

    addition_result = calc_addition(imput_first_number, imput_second_number)
    subtraction_result = calc_subtraction(imput_first_number, imput_second_number)
    multiplication_result = calc_multiplication(imput_first_number, imput_second_number)
    division_result = calc_division(imput_first_number, imput_second_number)

    show_results(addition_result, subtraction_result, multiplication_result, division_result)


if __name__ == '__main__':
    main()
