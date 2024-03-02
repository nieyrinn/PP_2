#task 9
import math

def volume(R):
    volume = (4/3) * 3,14 * R**3
    return volume

R = float(input())
result = volume(R)

print(result)
