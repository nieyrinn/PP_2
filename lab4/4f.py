#task 4
def is_prime(n):  #функция принимает число n в качестве аргумента.
    if n < 2:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def filter_prime(numbers):  #функция принимает список чисел numbers
    return list(filter(is_prime, numbers)) 
#использует встроенную функцию filter, чтобы отфильтровать 
#только те числа, для которых is_prime возвращает 1 в виде списка. 
primes = input().split() 
#Запрашивает ввод чисел, разделенных пробелами, и разбивает строку на список строк с использованием split().
numbers = [int(n) for n in primes]

result = filter_prime(numbers) #для отфильтровывания 
print(result)