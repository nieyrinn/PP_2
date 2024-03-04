import os
import string

for letter in string.ascii_uppercase:
    file_path = os.path.join("letters", letter + ".txt")
    
    # Проверяем, существует ли файл перед попыткой удаления
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Файл '{letter}.txt' удален.")
    else:
        print(f"Файл '{letter}.txt' не существует.")
