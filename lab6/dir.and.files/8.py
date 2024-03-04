import os

file_path = input()

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print(f"The file '{file_path}' does not exist.")
