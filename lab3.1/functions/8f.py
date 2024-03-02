#task 8
def spy_game(numbers):
    code = [0, 0, 7]  # Шпионский код
    index = 0  # Индекс, используемый для проверки порядка чисел

    for num in numbers:
        if num == code[index]: 
            index += 1
            if index == len(code): #индекс достигает длины шпионского кода 
                return True

    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Вернет True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Вернет True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Вернет False