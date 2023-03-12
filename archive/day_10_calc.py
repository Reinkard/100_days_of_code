logo = """
       _..._                          _..._     
    .-'_..._''.           .---.    .-'_..._''.  
  .' .'      '.\          |   |  .' .'      '.\ 
 / .'                     |   | / .'            
. '                       |   |. '              
| |                 __    |   || |              
| |              .:--.'.  |   || |              
. '             / |   \ | |   |. '              
 \ '.          .`" __ | | |   | \ '.          . 
  '. `._____.-'/ .'.''| | |   |  '. `._____.-'/ 
    `-.______ / / /   | |_'---'    `-.______ /  
             `  \ \._,\ '/                  `   
                 `--'  `"                       
"""


def addition(num_1, num_2) -> float:
    """
    Додає два числа.
    Args:
        num_1 (float): Перше число.
        num_2 (float): Друге число.
    Returns:
        float: Сума num_1 та num_2.
    """
    return num_1 + num_2


def substraction(num_1, num_2) -> float:
    """
    Віднімає два числа.
    Args:
        num_1 (float): Перше число.
        num_2 (float): Друге число.
    Returns:
        float: Різниця num_1 та num_2.
    """
    return num_1 - num_2


def multiplication(num_1, num_2) -> float:
    """
    Множення між двома числами.
    Args:
        num_1 (float): Перше число.
        num_2 (float): Друге число.
    Returns:
        float: Добуток num_1 та num_2.
    """
    return num_1 * num_2


def division(num_1, num_2) -> float:
    """
    Ділить два числа.
    Args:
        num_1 (float): Перше число.
        num_2 (float): Друге число.
    Returns:
        float: Частка num_1 та num_2.
    """
    return num_1 / num_2


def modulus(num_1, num_2) -> float:
    """
    Виначає остачу між ділення двох чисел.
    Args:
        num_1 (float): Перше число.
        num_2 (float): Друге число.
    Returns:
        float: Остача між діленням num_1 та num_2.
    """
    return num_1 % num_2


def exponentiation(num_1, num_2) -> float:
    """
    Зведення числа num_1 в степінь num_2.
    Args:
        num_1 (float): Перше число.
        num_2 (float): Друге число.
    Returns:
        float: num_1 в степені num_2.
    """
    return num_1 ** num_2


operation = {'+': addition, '-': substraction, '*': multiplication,
             '/': division, '%': modulus, '**': exponentiation}

def calc():
    print(logo)
    calculator = True
    while calculator:
        first_number = float(input('What`s the first number?: '))
        calculate_1st_number = True
        while calculate_1st_number:
            for keys in operation.keys():
                print(*keys, sep='')
            choise = input('Pick an operation: ')
            second_number = float(input('What`s the next number?: '))
            funct = operation[choise]
            first_number = funct(first_number, second_number)
            choise_with_result = input(
                f'Type "y" to continue with {first_number}, "n" to a new calculation or "e" to exit: ')
            while choise_with_result not in ['y', 'n', 'e']:
                choise_with_result = input(
                    f'Type "y" to continue with {first_number}, "n" to a new calculation or "e" to exit: ')
            if choise_with_result == 'n':
                calculate_1st_number = False
            elif choise_with_result == 'e':
                calculate_1st_number = False
                calculator = False
    print('Goodbye!')


calc()