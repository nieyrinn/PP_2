from datetime import datetime, timedelta

s = input()
user = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

d = user.replace(microsecond=0)

print("Original Datetime:", user)
print("Datetime without Microseconds:", d)
