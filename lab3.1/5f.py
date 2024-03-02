#task 5
from itertools import permutations
#ипортируем эту функцию из библиотеки итертулс, потому что он нужен ту файнд перестановки 
class str:
    def __init__(self):
        self.str = ""
#создается арибут с для хранения строки
    def getString(self):
        self.str = input()
#ввод строки
    def get_permutations(self):
        for perm in permutations(self.str):
            print(''.join(perm))
#perm представляет собой кортеж символов (букв) из перестановки
#''.join(perm) объединяет эти символы в одну строку.
p = str()
p.getString()
p.get_permutations()
