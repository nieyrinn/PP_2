#write a python program to calculate two date difference in seconds
import datetime
date1 = datetime.datetime(2022, 1, 1, 12, 0, 0)
date2 = datetime.datetime(2022, 1, 2, 12, 0, 0)
d = date2 - date1
seconds = d.total_seconds()
print(seconds)