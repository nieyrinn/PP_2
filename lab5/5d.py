from datetime import datetime

# Function to calculate the difference in seconds between two dates
def date_difference_in_seconds(date1, date2):
    if date1 > date2:
        date1, date2 = date2, date1  # Swap if date1 is later than date2
    difference = date2 - date1
    return difference.total_seconds()

# Take input for dates from the user
a = input()
b = input()

# Convert input to datetime objects
date1 = datetime.s(a, '%Y-%m-%d %H:%M:%S')
date2 = datetime.s(b, '%Y-%m-%d %H:%M:%S')

# Calculate and print the difference in seconds
difference_seconds = date_difference_in_seconds(date1, date2)
print(difference_seconds)
