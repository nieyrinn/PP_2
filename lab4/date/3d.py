#write a python program to drop microseconds from datetime
import datetime
x = datetime.datetime.now()
y = x.replace(microsecond = 0)
print(y)