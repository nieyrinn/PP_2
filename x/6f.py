#task 6
def r(str):
    words = str.split()  # Разбиваем строку на слова
    res = ' '.join(reversed(words))  # Обратный порядок слов и объединяем их в предложение
    return res

s = input()
res = r(s)
print(res)
