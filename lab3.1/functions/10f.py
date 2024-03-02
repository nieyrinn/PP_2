#task 10
def unique_elements(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

list = input().split()
list = [int(i) for i in list]

result = unique_elements(list)

print(result)

