# Ввод чисел вручную с клавиатуры
input_numbers = input()

# Преобразование введенной строки в список чисел
numbers = [int(num) for num in input_numbers.split()]

# Функция для проверки, является ли число простым
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Используем filter и lambda для фильтрации простых чисел
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)
