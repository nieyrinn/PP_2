import math
import time

number = float(input())
milliseconds = int(input())

time.sleep(milliseconds / 1000)

result = math.sqrt(number)

print(f"Square root of {number} after {milliseconds} is {result}")
