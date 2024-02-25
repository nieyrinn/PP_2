import re

s = input()
result = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

print(result)
