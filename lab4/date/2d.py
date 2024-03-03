#write a python program to print yesterday,today,tomorrow
import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print(yesterday, "\n", today, "\n", tomorrow)
