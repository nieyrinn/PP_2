def file_lengthy(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
                pass
    return i + 1

file = input()

print("Number of lines in the file:", file_lengthy(file))
